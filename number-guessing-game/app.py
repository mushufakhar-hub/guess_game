import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon="🎲")

if 'initialized' not in st.session_state:
    st.session_state.initialized = False
    st.session_state.num = None
    st.session_state.attempts = 0
    st.session_state.max_attempts = 6
    st.session_state.game_over = False
    st.session_state.history = []
    st.session_state.won = False

if st.button("🎮 New Game", use_container_width=True):
    st.session_state.num = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.history = []
    st.session_state.won = False
    st.session_state.initialized = True
    st.rerun()

st.title("🎲 Number Guessing Game")
st.write("Guess the number between **1 and 100**. You have **6 attempts**!")

if not st.session_state.initialized:
    st.info("👆 Click 'New Game' to start!")
elif st.session_state.game_over:
    if st.session_state.won:
        st.success(f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts!")
    else:
        st.error(f"💥 Game Over! The number was **{st.session_state.num}**.")
    st.info("Play again? Click 'New Game' above.")
else:
    guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, step=1)
    
    if st.button("Submit Guess", use_container_width=True) and guess:
        st.session_state.attempts += 1
        st.session_state.history.append(guess)
        
        if guess == st.session_state.num:
            st.session_state.won = True
            st.session_state.game_over = True
        elif st.session_state.attempts >= st.session_state.max_attempts:
            st.session_state.game_over = True
        st.rerun()
    
    if st.session_state.history:
        st.subheader("📊 Game History")
        for i, g in enumerate(st.session_state.history, 1):
            if i == st.session_state.attempts:
                col1, col2, col3 = st.columns([1, 2, 2])
                with col1:
                    st.write(f"**Attempt {i}/6**")
                with col2:
                    if g < st.session_state.num:
                        st.error("📉 Too low!")
                    elif g > st.session_state.num:
                        st.warning("📈 Too high!")
                    else:
                        st.success("✅ Correct!")
                with col3:
                    st.write(f"Guess: **{g}**")
            else:
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.write(f"Attempt {i}/6")
                with col2:
                    st.write(f"Guess: {g}")

        remaining = st.session_state.max_attempts - st.session_state.attempts
        if not st.session_state.game_over:
            st.info(f"Remaining attempts: **{remaining}/6**")

