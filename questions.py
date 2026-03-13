from groq import Groq
from dotenv import load_dotenv
import os

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

def generate_question(topic, grade):
    prompt = f"""Generate a {topic} math question appropriate for a grade {grade} student.
Think through the problem carefully and verify the correct answer before formatting your response.
Format EXACTLY like this:
QUESTION: [the question]
A) [option]
B) [option]
C) [option]
D) [option]
ANSWER: [just the letter, A, B, C, or D]

Only output the formatted question in that exact format, nothing else."""
    response = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def parse_question(raw):
    if "QUESTION:" not in raw:
        return None, None, None
    raw = raw[raw.index("QUESTION:"):]
    lines = raw.strip().split("\n")
    question, options, answer = "", {}, ""
    for line in lines:
        line = line.strip()
        if line.startswith("QUESTION:"):
            question = line.replace("QUESTION:", "").strip()
        elif line.startswith("A)"):
            options["A"] = line[2:].strip()
        elif line.startswith("B)"):
            options["B"] = line[2:].strip()
        elif line.startswith("C)"):
            options["C"] = line[2:].strip()
        elif line.startswith("D)"):
            options["D"] = line[2:].strip()
        elif line.startswith("ANSWER:"):
            raw_answer = line.replace("ANSWER:", "").strip().upper()
            answer = raw_answer[0] if raw_answer else ""
    return question, options, answer

def get_hint(question, options):
    opts = "\n".join([f"{k}) {v}" for k, v in options.items()])
    prompt = f"""A student is stuck on this maths question and needs a hint.
Question: {question}
{opts}

Give a clear, friendly, step-by-step explanation of HOW to approach and solve this problem.
Do NOT just give the answer — guide them through the method. Keep it concise (3-5 steps max)."""
    response = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

