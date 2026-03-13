# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation
You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.
- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the fixed app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission
1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.**
   - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

### Game Purpose
This is a number guessing game where the player tries to guess a secret number within a limited number of attempts. The game gives hints after each guess to guide the player toward the correct answer. The difficulty setting changes the number range and attempt limit.

### Bugs Found
1. **Hints were backwards** — guessing higher than the secret showed "Go HIGHER!" instead of "Go LOWER!" The greater than and less than logic in check_guess was flipped.
2. **Out of range guesses accepted** — typing 120 when the range is 1-100 was accepted without any error message. There was no validation check on the input.
3. **Attempts mismatch** — the sidebar showed 8 attempts allowed but the game started with only 7 attempts left. The attempts counter was initialized to 1 instead of 0.
4. **Double click required** — the submit button needed two clicks to register a guess because Streamlit was processing the text input and button click as separate events.
5. **Secret randomly converted to string** — on every even attempt, the secret number was converted to a string, which broke the comparison and caused wrong hints.

### Fixes Applied
1. Swapped the hint logic in check_guess so guess > secret returns "Go LOWER!" and guess < secret returns "Go HIGHER!"
2. Added range validation to reject guesses outside the allowed range and show an error message.
3. Changed the attempts initialization from 1 to 0 so the count starts correctly.
4. Wrapped the text input and submit button inside st.form so both submit together in one click.
5. Removed the string conversion bug that was randomly turning the secret into a string on even attempts.
6. Refactored all game logic functions into logic_utils.py and updated app.py to import from there.
7. Added 9 pytest tests in tests/test_game_logic.py covering winning, too high, too low, hints, parsing, and difficulty ranges.

## 📸 Demo

All 9 pytest tests passing:

```
tests/test_game_logic.py::test_winning_guess PASSED
tests/test_game_logic.py::test_guess_too_high PASSED
tests/test_game_logic.py::test_guess_too_low PASSED
tests/test_game_logic.py::test_hint_go_lower PASSED
tests/test_game_logic.py::test_hint_go_higher PASSED
tests/test_game_logic.py::test_parse_guess_valid PASSED
tests/test_game_logic.py::test_parse_guess_empty PASSED
tests/test_game_logic.py::test_range_normal PASSED
tests/test_game_logic.py::test_range_easy PASSED
9 passed in 0.01s
```

## 🚀 Stretch Features
- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]