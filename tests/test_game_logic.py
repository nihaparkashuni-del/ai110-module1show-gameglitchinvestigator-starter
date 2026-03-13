import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_hint_go_lower():
    # When guess is too high, hint should say Go LOWER
    outcome, message = check_guess(80, 50)
    assert "LOWER" in message


def test_hint_go_higher():
    # When guess is too low, hint should say Go HIGHER
    outcome, message = check_guess(20, 50)
    assert "HIGHER" in message


def test_parse_guess_valid():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42


def test_parse_guess_empty():
    ok, value, err = parse_guess("")
    assert ok is False


def test_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100


def test_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20