import streamlit as st
import random

# Initialize session state variables
if 'secret' not in st.session_state:
    st.session_state.secret = str(random.randint(100, 999))
    st.session_state.attempt = 1
    st.session_state.history = []
    st.session_state.game_over = False

# Uncomment for testing:
# st.write("Secret Number (for testing):", st.session_state.secret)

# --- Title and Instructions ---
st.title("🎮 Deductive Logic Game")
st.markdown("""
**🎯 Goal:** Guess the secret **3-digit number** within **10 attempts**.  
**✅ Feedback for each digit:**  
- **👌** Right digit & right place  
- **👍** Right digit but wrong place  
- **❌** Wrong digit  
""")

# --- Progress and Attempt Counter ---
progress = (st.session_state.attempt - 1) / 10
st.progress(progress, text=f"Attempt {st.session_state.attempt} of 10")

# --- User Input ---
col1, col2 = st.columns([3, 1])
with col1:
    guess = st.text_input("🔢 Enter your 3-digit guess:", max_chars=3, disabled=st.session_state.game_over).strip()

# with col2:
#     submit = st.button("✅ Submit", disabled=st.session_state.game_over)

# --- Guess Handling ---
if (guess) and not st.session_state.game_over:
    if len(guess) != 3 or not guess.isdigit():
        st.warning("⚠️ Please enter **exactly 3 digits** (numbers only).")
    else:
        if guess == st.session_state.secret:
            st.success(f"🎉 **Congratulations!** You guessed it right: `{st.session_state.secret}`")
            st.balloons()
            st.session_state.game_over = True
        else:
            # Generate feedback
            result = ''
            for i in range(3):
                if guess[i] == st.session_state.secret[i]:
                    result += '👌 '
                elif guess[i] in st.session_state.secret:
                    result += '👍 '
                else:
                    result += '❌ '
            # Save to history
            st.session_state.history.append((guess, result.strip()))
            st.session_state.attempt += 1

            # Check if game over
            if st.session_state.attempt > 10:
                st.error(f"💥 **Game Over!** The secret number was: `{st.session_state.secret}`")
                st.session_state.game_over = True

# --- Attempts History ---
if st.session_state.history:
    st.subheader("📝 Attempts History")
    for idx, (g, r) in enumerate(st.session_state.history, 1):
        st.write(f"**Attempt {idx}:** `{g}` → {r}")

# --- Reset Button ---
if st.button("🔄 New Game"):
    st.session_state.secret = str(random.randint(100, 999))
    st.session_state.attempt = 1
    st.session_state.history = []
    st.session_state.game_over = False
    st.success("✅ Game reset! Ready to play again.")

# --- Footer Message ---
if not st.session_state.game_over:
    st.info("💡 **Tip:** Think logically based on feedback to guess better next time!")
else:
    st.info("🔄 Click **New Game** to play again!")
