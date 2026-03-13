from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import date, datetime, timedelta
import hashlib
import os

load_dotenv("api.env")

mongo       = MongoClient(os.getenv("MONGO_URI"))
db          = mongo["mathapp"]
users       = db["users"]
progress    = db["user_progress"]
assignments = db["assignments"]


def _hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def create_user(username, password, ip="Unknown", user_agent="Unknown"):
    if users.find_one({"username": username}):
        return False, "Username already exists"
    users.insert_one({
        "username":          username,
        "password":          _hash_password(password),
        "registered_at":     datetime.utcnow().isoformat(),
        "registered_ip":     ip,
        "registered_device": user_agent,
    })
    return True, "Account created"


def login_user(username, password):
    return users.find_one({
        "username": username,
        "password": _hash_password(password),
    }) is not None


def get_progress(username):
    return progress.find_one({"username": username})


def create_progress(username, grade, level):
    today = str(date.today())
    progress.insert_one({
        "username":           username,
        "grade":              grade,
        "level":              level,
        "streak":             0,
        "last_active":        today,
        "total_answered":     0,
        "total_correct":      0,
        "daily_date":         today,
        "daily_answered":     0,
        "daily_correct":      0,
        "badges":             [],
        "perfect_quizzes":    0,
        "level_tests_passed": 0,
    })


def update_progress(username, correct, total):
    """Increment answered/correct counts and maintain daily + streak stats."""
    today = str(date.today())
    p     = get_progress(username)

    last_active = p.get("last_active", "")
    yesterday   = str(date.today() - timedelta(days=1))

    if last_active == today:
        streak_update = {}
    elif last_active == yesterday:
        streak_update = {"$inc": {"streak": 1}}
    else:
        streak_update = {"$set": {"streak": 1}}

    if p.get("daily_date") != today:
        progress.update_one(
            {"username": username},
            {"$set": {
                "daily_date":     today,
                "daily_answered": total,
                "daily_correct":  correct,
                "last_active":    today,
            },
             "$inc": {"total_answered": total, "total_correct": correct}}
        )
    else:
        progress.update_one(
            {"username": username},
            {"$set":  {"last_active": today},
             "$inc": {
                "total_answered": total, "total_correct": correct,
                "daily_answered": total, "daily_correct": correct,
            }}
        )

    if streak_update:
        progress.update_one({"username": username}, streak_update)


def award_badges(username, new_badges):
    """Add newly earned badges to the user's progress document."""
    if not new_badges:
        return
    progress.update_one(
        {"username": username},
        {"$addToSet": {"badges": {"$each": new_badges}}}
    )


def get_assignments(username):
    return list(assignments.find({"username": username}))


def create_assignments(username, level, topics):
    for topic in topics:
        assignments.insert_one({
            "username":    username,
            "level":       level,
            "topic":       topic,
            "quiz_1_done": False, "quiz_1_score": 0,
            "quiz_2_done": False, "quiz_2_score": 0,
        })


def complete_quiz(username, topic, quiz_num, score):
    field = f"quiz_{quiz_num}"
    assignments.update_one(
        {"username": username, "topic": topic},
        {"$set": {f"{field}_done": True, f"{field}_score": score}}
    )
    if score == 5:
        progress.update_one({"username": username}, {"$inc": {"perfect_quizzes": 1}})


def increment_level_tests(username):
    progress.update_one({"username": username}, {"$inc": {"level_tests_passed": 1}})


def get_completed_topics(username):
    """Return set of topic names where both quizzes are done."""
    docs = assignments.find({"username": username, "quiz_1_done": True, "quiz_2_done": True})
    return {d["topic"] for d in docs}


def all_assignments_complete(username, level):
    return assignments.find_one({
        "username": username,
        "level":    level,
        "$or": [{"quiz_1_done": False}, {"quiz_2_done": False}]
    }) is None


def advance_level(username):
    p         = get_progress(username)
    new_level = p["level"] + 1
    progress.update_one({"username": username}, {"$set": {"level": new_level}})
    return new_level


def delete_assignments(username, level):
    assignments.delete_many({"username": username, "level": level})
