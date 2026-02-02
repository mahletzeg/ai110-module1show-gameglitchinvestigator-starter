# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  When I first launched the game, it opened correctly in the browser, but several things didn’t behave the way I expected. I expected the game to start with 8 full attempts as per what it said on the left sidebar, but it immediately showed only 7 attempts remaining without me making a guess. The number of attempts also didn't update after the first attempt, and it didn't start updating until after my first attempt, so I ultimately did have 8 attempts. For the hints, the game told me to “go higher” even though when the secret number was revealed to me my guess was already higher, and it would tell me to "go lower" when my guess was lower. This made the hints confusing and incorrect. At one point, it said I was out of attempts even though the display still showed 1 attempt left. When the game ended and I tried to start a new game by pressing New Game, it still showed a “Game over. Start a new game to try again” message, even though I had already clicked the new game button. Ultimately, I wasn't able to start a new game unless I reloaded the page.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion you accepted and why.
- Give one example of an AI suggestion you changed or rejected and why.

I used ChatGPT and GitHub Copilot in VS Code while working on this project. One AI suggestion I accepted was changing the code related to starting a new game, because it helped reset the game state more consistently and fixed some of the repeated “game over” messages. One AI suggestion I changed was installing Streamlit using pip install streamlit, because that didn’t solve the problem in my case. I realized the real issue was that pip and python were using different paths, so I used python -m pip install streamlit instead, which correctly installed Streamlit in the active Python environment.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I considered a bug fixed when the relevant pytest passed and manual interaction with the running app showed the expected behavior, such as the attempts updating immediately after submit, hints persisting across the rerun, and the New Game button fully reseting the game. One test I ran was test_reset_game_state_resets_all, which uses monkeypatch to make random.randint deterministic and asserts all session keys are reset, and running the pytest confirmed the reset helper works. I also ran the app locally and verified that submitting a guess updates the "Attempts left" display immediately, hints are shown after the rerun, and pressing New Game resets secret, attempts, history, and input. I used AI (Copilot/ChatGPT) to suggest the reset_game_state helper, add the method into logic_utils.py, and to design the unit test. Then, I adapted the suggestions to match the app's session-state keys and UI flow.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
