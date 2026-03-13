from groq import Groq
from dotenv import load_dotenv
import os
import re
import json

load_dotenv("api.env")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

TOPICS_BY_LEVEL = {
    1:  ["Addition", "Subtraction", "Counting", "Number Patterns", "Place Value"],
    2:  ["Multiplication", "Division", "Times Tables", "Word Problems", "Mental Maths"],
    3:  ["Fractions", "Decimals", "Rounding", "Negative Numbers", "Basic Geometry"],
    4:  ["Basic Algebra", "Percentages", "Ratios", "Area & Perimeter", "Data & Graphs"],
    5:  ["Linear Equations", "Geometry", "Probability", "Averages", "Sequences"],
    6:  ["Systems of Equations", "Functions", "Indices", "Circle Theorems", "Transformations"],
    7:  ["Quadratics", "Trigonometry", "Vectors", "Simultaneous Equations", "Inequalities"],
    8:  ["Statistics", "Advanced Algebra", "Surds", "Graph Sketching", "Proof"],
    9:  ["Pre-Calculus", "Logarithms", "Binomial Theorem", "Parametric Equations", "Numerical Methods"],
    10: ["Limits", "Differentiation", "Integration", "Differential Equations", "Complex Numbers"],
    11: ["Advanced Integration", "Series", "Further Calculus", "Mechanics", "Statistics 2"],
    12: ["Multivariable Calculus", "Linear Algebra", "Real Analysis", "Abstract Algebra", "Number Theory"]
}

def get_topics_for_level(level):
    return TOPICS_BY_LEVEL.get(level, TOPICS_BY_LEVEL[1])

BATCH_SYSTEM = """You are a mathematics question generator. Output ONLY a valid JSON array, nothing else.

RULES:
1. Solve every problem first to find the correct answer.
2. "answer" must be the letter (A/B/C/D) of the correct option.
3. Double-check your arithmetic before writing the answer field.
4. All four options must be plausible; exactly ONE is correct.
5. No preamble, no markdown fences, no extra text — pure JSON only."""

HINT_SYSTEM = """You are a friendly maths tutor giving a short hint to a student.

RULES:
- Be concise: 3-4 bullet points maximum.
- Do NOT show your thinking or reasoning process.
- Do NOT use <think> tags or any internal monologue.
- Do NOT give the answer directly.
- Guide the student through the METHOD only.
- Use plain language suitable for the student's level."""


def _strip_think_tags(text: str) -> str:
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"</?think>", "", text, flags=re.IGNORECASE)
    return text.strip()


def _extract_json(raw: str) -> str:
    """Pull out the first [...] JSON array from raw text."""
    raw = _strip_think_tags(raw)
    raw = re.sub(r"```(?:json)?", "", raw, flags=re.IGNORECASE).strip("` \n")
    m = re.search(r"\[.*\]", raw, re.DOTALL)
    return m.group(0) if m else raw



def generate_question_batch(topic: str, grade: int, n: int) -> list[tuple]:
    """
    Generate `n` questions for `topic` / `grade` in a SINGLE API call.
    Returns a list of (question, options_dict, answer_letter) tuples.
    Falls back to individual generation if the batch parse fails.
    """
    prompt = (
        f"Generate exactly {n} different {topic} questions for a Grade {grade} student.\n\n"
        f"Return a JSON array of exactly {n} objects. Each object:\n"
        '{\n'
        '  "question": "...",\n'
        '  "A": "...", "B": "...", "C": "...", "D": "...",\n'
        '  "answer": "A"   // letter of the ONE correct option\n'
        '}\n\n'
        "Solve each problem first. Double-check every answer before writing it.\n"
        "Output ONLY the JSON array — no markdown, no explanation."
    )

    for attempt in range(3):
        try:
            resp = client.chat.completions.create(
                model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
                messages=[
                    {"role": "system", "content": BATCH_SYSTEM},
                    {"role": "user",   "content": prompt},
                ],
                temperature=0.3,
            )
            raw  = resp.choices[0].message.content
            data = json.loads(_extract_json(raw))

            results = []
            for item in data:
                q   = str(item.get("question", "")).strip()
                ans = str(item.get("answer",   "")).strip().upper()
                opts = {
                    "A": str(item.get("A", "")).strip(),
                    "B": str(item.get("B", "")).strip(),
                    "C": str(item.get("C", "")).strip(),
                    "D": str(item.get("D", "")).strip(),
                }
                if q and ans in opts and all(opts.values()):
                    results.append((q, opts, ans))

            if len(results) >= n:
                return results[:n]

        except Exception:
            pass

    results = []
    for _ in range(n):
        raw = generate_question(topic, grade)
        q, opts, ans = parse_question(raw)
        if q and opts and ans in opts:
            results.append((q, opts, ans))
    return results


def generate_question_batch_mixed(topics: list, grade: int, n: int) -> list[tuple]:
    """
    Like generate_question_batch but cycles through multiple topics (for level tests).
    Generates a mini-batch per topic then interleaves results.
    """
    per_topic = max(1, (n + len(topics) - 1) // len(topics))
    all_qs: list[tuple] = []

    for topic in topics:
        batch = generate_question_batch(topic, grade, per_topic)
        all_qs.extend(batch)
        if len(all_qs) >= n:
            break

    # If still short, top up with the first topic
    while len(all_qs) < n:
        extra = generate_question_batch(topics[0], grade, n - len(all_qs))
        all_qs.extend(extra)

    return all_qs[:n]


# ── Single-question generation (kept for compatibility / hints) ──────────────

QUESTION_SYSTEM = """You are a mathematics question generator. Output ONLY the formatted question, nothing else.

RULES:
1. Solve the problem first to find the correct answer.
2. ANSWER: must contain the letter of the correct option.
3. Check your arithmetic. Never mark a wrong answer correct.
4. All four options must be plausible; only ONE is correct.
5. No preamble, no explanation, no extra text whatsoever."""


def generate_question(topic, grade, max_retries=3):
    prompt = (
        f"Generate a {topic} math question for a grade {grade} student.\n\n"
        "STEP 1: Solve it to find the correct answer.\n"
        "STEP 2: Write four options (A-D); exactly one must equal your answer.\n"
        "STEP 3: Set ANSWER: to that letter.\n\n"
        "Output format (nothing else):\n"
        "QUESTION: [the question]\n"
        "A) [option]\nB) [option]\nC) [option]\nD) [option]\n"
        "ANSWER: [A, B, C, or D]"
    )
    raw = ""
    for _ in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
                messages=[
                    {"role": "system", "content": QUESTION_SYSTEM},
                    {"role": "user",   "content": prompt},
                ],
                temperature=0.3,
            )
            raw = _strip_think_tags(response.choices[0].message.content)
            question, options, answer = parse_question(raw)
            if (question and options and len(options) == 4
                    and answer in options
                    and all(k in options for k in ["A", "B", "C", "D"])):
                return raw
        except Exception:
            pass
    return raw


def parse_question(raw):
    """Parse raw AI output → (question_str, options_dict, answer_letter)."""
    if not raw or "QUESTION:" not in raw:
        return None, None, None

    raw = _strip_think_tags(raw)
    raw = raw[raw.index("QUESTION:"):]
    lines = [l.strip() for l in raw.split("\n") if l.strip()]

    question, options, answer = "", {}, ""

    for line in lines:
        if line.upper().startswith("QUESTION:"):
            question = line[len("QUESTION:"):].strip()
        elif re.match(r"^[Aa][)\.\:]", line):
            options["A"] = re.sub(r"^[Aa][)\.\:]\s*", "", line).strip()
        elif re.match(r"^[Bb][)\.\:]", line):
            options["B"] = re.sub(r"^[Bb][)\.\:]\s*", "", line).strip()
        elif re.match(r"^[Cc][)\.\:]", line):
            options["C"] = re.sub(r"^[Cc][)\.\:]\s*", "", line).strip()
        elif re.match(r"^[Dd][)\.\:]", line):
            options["D"] = re.sub(r"^[Dd][)\.\:]\s*", "", line).strip()
        elif line.upper().startswith("ANSWER:"):
            raw_ans = line[len("ANSWER:"):].strip().upper()
            m = re.search(r"[A-D]", raw_ans)
            answer = m.group(0) if m else ""

    return question, options, answer


def verify_question(question: str, options: dict, claimed_answer: str) -> bool:
    """Ask the LLM to independently verify the answer. Returns True if confirmed."""
    opts_str = "\n".join(f"{k}) {v}" for k, v in options.items())
    prompt = (
        f"Question: {question}\n{opts_str}\n\n"
        f"Claimed correct answer: {claimed_answer}) {options.get(claimed_answer, '')}\n\n"
        "Solve independently. Reply ONLY: CORRECT or WRONG"
    )
    try:
        response = client.chat.completions.create(
            model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
            messages=[
                {"role": "system", "content": "You are a strict maths checker. Reply only CORRECT or WRONG."},
                {"role": "user",   "content": prompt},
            ],
            temperature=0.0,
            max_tokens=10,
        )
        verdict = _strip_think_tags(response.choices[0].message.content).strip().upper()
        return verdict.startswith("CORRECT")
    except Exception:
        return True  # accept on API error


def get_hint(question, options):
    opts = "\n".join([f"{k}) {v}" for k, v in options.items()])
    prompt = (
        f"A student needs a hint for this maths question:\n"
        f"Question: {question}\n{opts}\n\n"
        "Give 3-4 short bullet points explaining HOW to solve it. "
        "Do NOT give the final answer. Be clear and concise."
    )
    response = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
        messages=[
            {"role": "system", "content": HINT_SYSTEM},
            {"role": "user",   "content": prompt},
        ],
        temperature=0.3,
    )
    raw = _strip_think_tags(response.choices[0].message.content)
    return raw
