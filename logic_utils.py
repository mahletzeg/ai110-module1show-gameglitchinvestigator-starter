import random

#FIX: Moved logic from app.py to logic_utils.py — Copilot assisted
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."
    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📈 Go HIGHER!"
        else:
            return "Too Low", "📉 Go LOWER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📈 Go HIGHER!"
        return "Too Low", "📉 Go LOWER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


#FIX: Added a helper to reset all relevant session state when starting a new game — Copilot assisted
def reset_game_state(session_state: dict, low: int, high: int, difficulty: str):
    """
    Reset session-like dict to start a new game.
    - session_state can be st.session_state or a plain dict in tests.
    """
    session_state["attempts"] = 0
    session_state["secret"] = random.randint(low, high)
    session_state["score"] = 0
    session_state["history"] = []
    session_state["status"] = "playing"
    session_state["last_hint"] = None
    session_state[f"guess_input_{difficulty}"] = ""
