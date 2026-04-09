from datetime import datetime

VALID_EMOTIONS = {
    "happy", "sad", "anxious", "motivated",
    "angry", "calm", "excited", "nostalgic"
}


def validate_date(date: str):
    try:
        datetime.strptime(date.strip(), "%Y-%m-%d")
        return True, ""
    except ValueError:
        return False, "Invalid date format. Use YYYY-MM-DD"


def validate_description(desc: str):
    desc = desc.strip()

    if not desc:
        return False, "Description cannot be empty"
    if len(desc) < 3:
        return False, "Description too short"
    if len(desc) > 300:
        return False, "Description too long"

    return True, ""


def validate_emotion(emotion: str):
    if emotion.lower() not in VALID_EMOTIONS:
        return False, f"Invalid emotion. Options: {', '.join(VALID_EMOTIONS)}"
    return True, ""


def validate_memory(date, description, emotion):
    errors = []

    ok, msg = validate_date(date)
    if not ok: errors.append(msg)

    ok, msg = validate_description(description)
    if not ok: errors.append(msg)

    ok, msg = validate_emotion(emotion)
    if not ok: errors.append(msg)

    return len(errors) == 0, errors