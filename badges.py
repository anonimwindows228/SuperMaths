from datetime import date

BADGES = {
    "first_step": {
        "name": "First Step",
        "desc": "Answer your first question",
        "icon": "👣", "color": "#10b981", "category": "Progress",
    },
    "ten_questions": {
        "name": "Getting Going",
        "desc": "Answer 10 questions total",
        "icon": "🔟", "color": "#10b981", "category": "Progress",
    },
    "century": {
        "name": "Century",
        "desc": "Answer 100 questions total",
        "icon": "💯", "color": "#8b5cf6", "category": "Progress",
    },
    "five_hundred": {
        "name": "Five Hundred",
        "desc": "Answer 500 questions total",
        "icon": "🚀", "color": "#3b82f6", "category": "Progress",
    },
    "one_thousand": {
        "name": "The Thousand",
        "desc": "Answer 1000 questions total",
        "icon": "🌟", "color": "#f59e0b", "category": "Progress",
    },

    "level_up": {
        "name": "Level Up",
        "desc": "Advance to the next level",
        "icon": "⬆️", "color": "#8b5cf6", "category": "Levels",
    },
    "level_3": {
        "name": "Getting Serious",
        "desc": "Reach Level 3",
        "icon": "📈", "color": "#10b981", "category": "Levels",
    },
    "level_5": {
        "name": "Halfway There",
        "desc": "Reach Level 5",
        "icon": "🏅", "color": "#3b82f6", "category": "Levels",
    },
    "level_7": {
        "name": "Advanced Scholar",
        "desc": "Reach Level 7",
        "icon": "🎓", "color": "#8b5cf6", "category": "Levels",
    },
    "level_10": {
        "name": "Expert",
        "desc": "Reach Level 10",
        "icon": "🏆", "color": "#3b82f6", "category": "Levels",
    },
    "level_12": {
        "name": "Grandmaster",
        "desc": "Reach the maximum level",
        "icon": "👑", "color": "#f59e0b", "category": "Levels",
    },

    "perfect_quiz": {
        "name": "Perfect Score",
        "desc": "Score 5/5 on any quiz",
        "icon": "⭐", "color": "#10b981", "category": "Skill",
    },
    "three_perfects": {
        "name": "Hat-Trick Ace",
        "desc": "Score 5/5 on three quizzes",
        "icon": "🌠", "color": "#8b5cf6", "category": "Skill",
    },
    "hint_free": {
        "name": "No Hints Needed",
        "desc": "Complete a quiz without using a hint",
        "icon": "🧠", "color": "#3b82f6", "category": "Skill",
    },
    "sharpshooter": {
        "name": "Sharpshooter",
        "desc": "90%+ accuracy over 20+ questions",
        "icon": "🎯", "color": "#8b5cf6", "category": "Skill",
    },
    "iron_accuracy": {
        "name": "Iron Accuracy",
        "desc": "95%+ accuracy over 50+ questions",
        "icon": "🔩", "color": "#f59e0b", "category": "Skill",
    },
    "level_tester": {
        "name": "Speed Runner",
        "desc": "Pass a Level Test",
        "icon": "⚡", "color": "#3b82f6", "category": "Skill",
    },
    "three_level_tests": {
        "name": "Test Crusher",
        "desc": "Pass 3 Level Tests",
        "icon": "💥", "color": "#8b5cf6", "category": "Skill",
    },

    # ── Daily & streaks ──────────────────────────────────────────────────────
    "daily_10": {
        "name": "Daily Grind",
        "desc": "Answer 10 questions in a day",
        "icon": "🔥", "color": "#10b981", "category": "Consistency",
    },
    "daily_30": {
        "name": "On Fire",
        "desc": "Answer 30 questions in a day",
        "icon": "🌋", "color": "#8b5cf6", "category": "Consistency",
    },
    "daily_50": {
        "name": "Unstoppable",
        "desc": "Answer 50 questions in a day",
        "icon": "⚡", "color": "#f59e0b", "category": "Consistency",
    },
    "streak_3": {
        "name": "Hat-Trick",
        "desc": "Answer questions 3 days in a row",
        "icon": "🎩", "color": "#f59e0b", "category": "Consistency",
    },
    "streak_7": {
        "name": "Week Warrior",
        "desc": "7-day answer streak",
        "icon": "📅", "color": "#f59e0b", "category": "Consistency",
    },
    "streak_30": {
        "name": "Monthly Master",
        "desc": "30-day answer streak",
        "icon": "🗓️", "color": "#f59e0b", "category": "Consistency",
    },

    # ── Topic mastery (Level 9–12 topics) ───────────────────────────────────
    "calculus_master": {
        "name": "Calculus Master",
        "desc": "Complete all Differentiation & Integration quizzes",
        "icon": "∫", "color": "#3b82f6", "category": "Mastery",
    },
    "maclaurin_master": {
        "name": "Series Master",
        "desc": "Complete all Series & Further Calculus quizzes",
        "icon": "Σ", "color": "#8b5cf6", "category": "Mastery",
    },
    "algebra_master": {
        "name": "Algebra Master",
        "desc": "Complete all Advanced Algebra & Abstract Algebra quizzes",
        "icon": "α", "color": "#10b981", "category": "Mastery",
    },
    "geometry_master": {
        "name": "Geometry Master",
        "desc": "Complete all Geometry & Circle Theorems quizzes",
        "icon": "📐", "color": "#3b82f6", "category": "Mastery",
    },
    "stats_master": {
        "name": "Stats Master",
        "desc": "Complete all Statistics & Probability quizzes",
        "icon": "📊", "color": "#10b981", "category": "Mastery",
    },
    "number_theory_master": {
        "name": "Number Theorist",
        "desc": "Complete all Number Theory quizzes",
        "icon": "🔢", "color": "#8b5cf6", "category": "Mastery",
    },
    "trig_master": {
        "name": "Trig Master",
        "desc": "Complete all Trigonometry quizzes",
        "icon": "📡", "color": "#3b82f6", "category": "Mastery",
    },
    "linear_algebra_master": {
        "name": "Linear Algebra Master",
        "desc": "Complete all Linear Algebra & Vectors quizzes",
        "icon": "🧮", "color": "#f59e0b", "category": "Mastery",
    },
    "mechanics_master": {
        "name": "Mechanics Master",
        "desc": "Complete all Mechanics quizzes",
        "icon": "⚙️", "color": "#10b981", "category": "Mastery",
    },
    "proof_master": {
        "name": "Proof Master",
        "desc": "Complete all Proof & Real Analysis quizzes",
        "icon": "📜", "color": "#8b5cf6", "category": "Mastery",
    },
    "multivariable_master": {
        "name": "Multivariable Master",
        "desc": "Complete all Multivariable Calculus quizzes",
        "icon": "🌐", "color": "#f59e0b", "category": "Mastery",
    },
}

# Map topics → mastery badge keys
_TOPIC_MASTERY = {
    "Differentiation":       "calculus_master",
    "Integration":           "calculus_master",
    "Series":                "maclaurin_master",
    "Further Calculus":      "maclaurin_master",
    "Advanced Algebra":      "algebra_master",
    "Abstract Algebra":      "algebra_master",
    "Geometry":              "geometry_master",
    "Basic Geometry":        "geometry_master",
    "Circle Theorems":       "geometry_master",
    "Statistics":            "stats_master",
    "Statistics 2":          "stats_master",
    "Probability":           "stats_master",
    "Number Theory":         "number_theory_master",
    "Trigonometry":          "trig_master",
    "Vectors":               "linear_algebra_master",
    "Linear Algebra":        "linear_algebra_master",
    "Mechanics":             "mechanics_master",
    "Proof":                 "proof_master",
    "Real Analysis":         "proof_master",
    "Multivariable Calculus":"multivariable_master",
}

# How many distinct quizzes must be completed per mastery badge
_MASTERY_REQUIRED = {
    "calculus_master":       2,
    "maclaurin_master":      2,
    "algebra_master":        2,
    "geometry_master":       2,
    "stats_master":          2,
    "number_theory_master":  1,
    "trig_master":           1,
    "linear_algebra_master": 2,
    "mechanics_master":      1,
    "proof_master":          2,
    "multivariable_master":  1,
}


def check_badges(p, score=None, total=None, quiz_score=None,
                 level_test_passed=False, used_hint=False,
                 daily_answered=0, level_advanced=False,
                 completed_topics=None):
    """Return list of newly earned badge keys given current progress state."""
    earned       = set(p.get("badges", []))
    newly_earned = []

    def award(key):
        if key not in earned and key in BADGES:
            newly_earned.append(key)
            earned.add(key)

    total_answered  = p.get("total_answered", 0)
    total_correct   = p.get("total_correct", 0)
    level           = p.get("level", 1)
    streak          = p.get("streak", 0)
    perfect_quizzes = p.get("perfect_quizzes", 0)
    level_tests     = p.get("level_tests_passed", 0)

    # Volume
    if total_answered >= 1:    award("first_step")
    if total_answered >= 10:   award("ten_questions")
    if total_answered >= 100:  award("century")
    if total_answered >= 500:  award("five_hundred")
    if total_answered >= 1000: award("one_thousand")

    # Levels
    if level >= 3:  award("level_3")
    if level >= 5:  award("level_5")
    if level >= 7:  award("level_7")
    if level >= 10: award("level_10")
    if level >= 12: award("level_12")
    if level_advanced: award("level_up")

    # Level tests
    if level_test_passed:
        award("level_tester")
        if level_tests >= 3: award("three_level_tests")

    # Accuracy
    if total_answered >= 20 and total_correct / total_answered >= 0.90:
        award("sharpshooter")
    if total_answered >= 50 and total_correct / total_answered >= 0.95:
        award("iron_accuracy")

    # Quiz performance
    if quiz_score == 5:
        award("perfect_quiz")
        if perfect_quizzes >= 3: award("three_perfects")
    if not used_hint and quiz_score is not None:
        award("hint_free")

    # Daily
    if daily_answered >= 10: award("daily_10")
    if daily_answered >= 30: award("daily_30")
    if daily_answered >= 50: award("daily_50")

    # Streaks
    if streak >= 3:  award("streak_3")
    if streak >= 7:  award("streak_7")
    if streak >= 30: award("streak_30")

    # Topic mastery — completed_topics is a set of topic names with both quizzes done
    if completed_topics:
        # Count how many distinct topics map to each mastery badge
        counts: dict[str, set] = {}
        for t in completed_topics:
            badge_key = _TOPIC_MASTERY.get(t)
            if badge_key:
                counts.setdefault(badge_key, set()).add(t)
        for badge_key, topics_done in counts.items():
            required = _MASTERY_REQUIRED.get(badge_key, 1)
            if len(topics_done) >= required:
                award(badge_key)

    return newly_earned
