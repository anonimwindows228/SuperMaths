from datetime import date

BADGES = {
    "first_step": {
        "name": "First Step",
        "desc": "Answer your first question",
        "icon": "👣",
        "color": "#10b981"
    },
    "ten_questions": {
        "name": "Getting Going",
        "desc": "Answer 10 questions total",
        "icon": "🔟",
        "color": "#10b981"
    },
    "century": {
        "name": "Century",
        "desc": "Answer 100 questions total",
        "icon": "💯",
        "color": "#8b5cf6"
    },
    "five_hundred": {
        "name": "Five Hundred",
        "desc": "Answer 500 questions total",
        "icon": "🚀",
        "color": "#3b82f6"
    },
    "perfect_quiz": {
        "name": "Perfect Score",
        "desc": "Score 5/5 on any quiz",
        "icon": "⭐",
        "color": "#10b981"
    },
    "level_up": {
        "name": "Level Up",
        "desc": "Advance to the next level",
        "icon": "⬆️",
        "color": "#8b5cf6"
    },
    "level_5": {
        "name": "Halfway There",
        "desc": "Reach Level 5",
        "icon": "🏅",
        "color": "#3b82f6"
    },
    "level_10": {
        "name": "Expert",
        "desc": "Reach Level 10",
        "icon": "🏆",
        "color": "#3b82f6"
    },
    "level_12": {
        "name": "Grandmaster",
        "desc": "Reach the maximum level",
        "icon": "👑",
        "color": "#ffffff"
    },
    "sharpshooter": {
        "name": "Sharpshooter",
        "desc": "Maintain 90%+ accuracy over 20+ questions",
        "icon": "🎯",
        "color": "#8b5cf6"
    },
    "daily_10": {
        "name": "Daily Grind",
        "desc": "Answer 10 questions in a single day",
        "icon": "🔥",
        "color": "#10b981"
    },
    "daily_30": {
        "name": "On Fire",
        "desc": "Answer 30 questions in a single day",
        "icon": "🌋",
        "color": "#8b5cf6"
    },
    "level_tester": {
        "name": "Speed Runner",
        "desc": "Pass a Level Test",
        "icon": "⚡",
        "color": "#3b82f6"
    },
    "hint_free": {
        "name": "No Hints Needed",
        "desc": "Complete a full quiz without using a hint",
        "icon": "🧠",
        "color": "#ffffff"
    },
}

def check_badges(p, score=None, total=None, quiz_score=None,
                 level_test_passed=False, used_hint=False, daily_answered=0):
    """Return list of newly earned badge keys given current progress state."""
    earned = set(p.get("badges", []))
    newly_earned = []

    def award(key):
        if key not in earned:
            newly_earned.append(key)
            earned.add(key)

    total_answered = p.get("total_answered", 0)
    total_correct  = p.get("total_correct", 0)
    level          = p.get("level", 1)

    if total_answered >= 1:        award("first_step")
    if total_answered >= 10:       award("ten_questions")
    if total_answered >= 100:      award("century")
    if total_answered >= 500:      award("five_hundred")
    if level >= 5:                 award("level_5")
    if level >= 10:                award("level_10")
    if level >= 12:                award("level_12")
    if level_test_passed:          award("level_tester")

    if total_answered >= 20 and total_correct / total_answered >= 0.9:
        award("sharpshooter")

    if quiz_score == 5:            award("perfect_quiz")
    if not used_hint and quiz_score is not None:
        award("hint_free")

    if daily_answered >= 10:       award("daily_10")
    if daily_answered >= 30:       award("daily_30")

    return newly_earned