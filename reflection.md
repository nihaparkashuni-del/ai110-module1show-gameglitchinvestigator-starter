# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the game, it looked polished but behaved strangely. The hints were completely backwards — guessing higher than the secret told me to go higher instead of lower. The attempts counter started at 7 even though the sidebar said 8 were allowed. The submit button required two clicks to register a guess, and numbers outside the 1-100 range were accepted without any error.

Bug 1: Hints are backwards. Guessing 120 when secret is 1 showed "Go HIGHER!" instead of "Go LOWER!"

Bug 2: Out of range numbers accepted. Guessing 120 when range is 1-100 should be rejected but wasn't.

Bug 3: Attempts mismatch. Sidebar shows 8 allowed but game starts with 7 attempts left.

Bug 4: Double click required. Submit button needs two clicks to register a guess.

---

## 2. How did you use AI as a teammate?

I used Claude (AI assistant) to help identify and fix bugs in this project.

Correct suggestion:
Claude correctly identified that check_guess returns a tuple like ('Win', 'Correct!') but the original tests were comparing the whole tuple to just the string 'Win'. It suggested unpacking the tuple with outcome, message = check_guess() so only the outcome string was compared. I verified this by running pytest and seeing all 9 tests pass after the fix.

Incorrect or misleading suggestion:
Claude first suggested the double-click bug was a logic error inside the Python code. This was misleading because the real cause was how Streamlit handles text input and button clicks separately. The actual fix was wrapping the input and button inside st.form so they submit together in one click. I verified this by testing the app in the browser and confirming one click was enough.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed when the app behaved correctly in the browser AND the pytest tests passed. For each fix I had a specific test case in mind before checking the result, like "guess 80 when secret is 50, hint should say Go LOWER."

I ran pytest tests/test_game_logic.py -v and all 9 tests passed. The tests checked that check_guess returns the correct outcome for winning, too high, and too low guesses, and also verified that the hint messages contained the right direction words LOWER and HIGHER.

AI helped me understand why the tests were failing by explaining that check_guess returns a tuple, not a plain string. Once I understood that, I was able to fix the tests myself by unpacking the tuple correctly.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the entire Python script from top to bottom every time a user interacts with the app, like clicking a button or typing in a box. This means normal variables reset every time, so Streamlit provides session_state to store values that should persist across reruns, like the secret number, score, and attempt count.

I would explain it to a friend like this: imagine every button click refreshes the whole page, so anything you stored in a regular variable disappears. Session state is like a sticky notepad that survives each refresh and remembers your values.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is writing specific test cases before fixing a bug, not after. Knowing exactly what correct behavior looks like made it much easier to verify that my fix actually worked and did not break anything else.

Next time I work with AI on a coding task I would ask it to explain the root cause of a bug before asking for a fix. In this project, jumping to the fix too early led to a misleading suggestion about the double-click bug.

This project changed the way I think about AI generated code because I realized that AI can write code that looks correct and runs without crashing but still has wrong logic hidden inside. You have to actually test the behavior, not just check that it runs.