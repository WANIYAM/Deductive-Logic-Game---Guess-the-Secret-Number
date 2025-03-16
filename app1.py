import streamlit as st
import random

# Initialize session state variables
if 'secret' not in st.session_state:
    st.session_state.secret = str(random.randint(100, 999))
    st.session_state.attempt = 1
    st.session_state.history = []

# Uncomment for testing:
# st.write("Secret Number (for testing):", st.session_state.secret)

# Title and instructions
st.title("🔢 Deductive Logic Game")
st.write("🎯 **Goal:** Guess the secret 3-digit number.")
st.write("🕐 You have **10 attempts** to guess correctly.")
st.write("✅ Feedback for each digit:\n- **👌** Correct digit and position\n- **👍** Correct digit, wrong position\n- **❌** Incorrect digit")

# User input
guess = st.text_input(f"Attempt {st.session_state.attempt}: Enter your 3-digit guess", max_chars=3)

# Handle guess submission
if st.button("Submit Guess"):
    if len(guess) != 3 or not guess.isdigit():
        st.warning("⚠️ Please enter exactly 3 digits (numbers only).")
    elif st.session_state.attempt > 10:
        st.error("❌ No more attempts left! Refresh the page to play again.")
    else:
        if guess == st.session_state.secret:
            st.success(f"🎉 Congratulations! You guessed it right: {st.session_state.secret}")
            st.balloons()
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
            # Save attempt and feedback
            st.session_state.history.append((guess, result.strip()))
            st.session_state.attempt += 1

            # Show history
            st.subheader("📝 Attempts History")
            for idx, (g, r) in enumerate(st.session_state.history, 1):
                st.write(f"**Attempt {idx}:** {g} → {r}")

            # If last attempt
            if st.session_state.attempt > 10:
                st.error(f"💥 Game Over! The secret number was: **{st.session_state.secret}**")
                st.info("🔄 Refresh the page to play again.")

# Reset game button
if st.button("🔄 Reset Game"):
    st.session_state.secret = str(random.randint(100, 999))
    st.session_state.attempt = 1
    st.session_state.history = []
    st.success("🔁 Game has been reset. Start guessing!")
