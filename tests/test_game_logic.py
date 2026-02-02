from logic_utils import check_guess, reset_game_state
import random


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert isinstance(message, str)


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_reset_game_state_resets_all(monkeypatch):
    state = {
        "attempts": 5,
        "secret": 13,
        "score": 42,
        "history": [1, 2, 3],
        "status": "lost",
        "last_hint": "old hint",
        "guess_input_Normal": "77",
    }

    # make randint deterministic
    monkeypatch.setattr(random, "randint", lambda low, high: 99)

    reset_game_state(state, low=1, high=100, difficulty="Normal")

    assert state["attempts"] == 0
    assert state["secret"] == 99
    assert state["score"] == 0
    assert state["history"] == []
    assert state["status"] == "playing"
    assert state["last_hint"] is None
    assert state["guess_input_Normal"] == ""
