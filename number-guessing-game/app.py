import streamlit as st

import random

# Page config
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎯",
    layout="wide"
)

# Modern CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.3rem;
        color: #64748b;
        text-align: center;
        margin-bottom: 2rem;
    }
    .game-container {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        max-width: 600px;
        margin: 0 auto;
    }
    .footer {
        text-align: center;
        padding: 2rem;
        color: #64748b;
        font-size: 0.9rem;
        border-top: 1px solid #e2e8f0;
        margin-top: 3rem;
    }
    .stButton > button {
        border-radius: 12px;
        font-weight: 600;
        font-size: 1.1rem;
        height: 50px;
    }
    </style>
""", unsafe_allow_html=True)

if 'initialized' not in st.session_state:
    st.session_state.initialized = False
    st.session_state.num = None
    st.session_state.attempts = 0
    st.session_state.max_attempts = 6
    st.session_state.game_over = False
    st.session_state.history = []
    st.session_state.won = False

# Sidebar instructions
with st.sidebar:
    st.header("📖 How to Play")
    st.write("1. Click **New Game**")
    st.write("2. Guess number **1-100**")
    st.write("3. **6 attempts** max")
    st.write("4. Get **hints**: 📉 low / 📈 high")
    st.space(20)
    st.balloons() if st.session_state.get('won') else None

# Header
st.markdown('<h1 class="main-header">🎯 Number Guessing Game</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Challenge yourself to guess the secret number in 6 tries or less!</p>', unsafe_allow_html=True)

# Game container
with st.container():
    st.markdown('<div class="game-container">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3,1])
    with col2:
        if st.button("🔄 New Game", use_container_width=True):
            st.session_state.num = random.randint(1, 100)
            st.session_state.attempts = 0
            st.session_state.game_over = False
            st.session_state.history = []
            st.session_state.won = False
            st.session_state.initialized = True
            st.rerun()
    
    if not st.session_state.initialized:
        st.info("🚀 **Click New Game to start!**")
    elif st.session_state.game_over:
        if st.session_state.won:
            st.balloons()
            st.success(f"🏆 **Congratulations!** 🎉 You won in **{st.session_state.attempts}** attempts!")
        else:
            st.error(f"😵 **Game Over!** The number was **{st.session_state.num}**")
        st.info("🔄 **Start a new game above!**")
    else:
        col_guess, col_remaining = st.columns(2)
        with col_guess:
            guess = st.number_input("🎲 Your Guess:", min_value=1, max_value=100, step=1, key="guess", label_visibility="collapsed")
        with col_remaining:
            remaining = st.session_state.max_attempts - st.session_state.attempts
            st.metric("⏳ Remaining", f"{remaining}/6")
        
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            if st.button("🔍 Submit Guess", use_container_width=True) and guess:
                st.session_state.attempts += 1
                st.session_state.history.append(guess)
                
                if guess == st.session_state.num:
                    st.session_state.won = True
                    st.session_state.game_over = True
                elif st.session_state.attempts >= st.session_state.max_attempts:
                    st.session_state.game_over = True
                st.rerun()
        
        st.caption("💡 **Tip**: Press Enter after typing your guess or click Submit!")
        
        # History
        if st.session_state.history:
            with st.expander("📜 Guess History", expanded=True):
                for i, g in enumerate(st.session_state.history, 1):
                    if i == st.session_state.attempts:
                        feedback = "✅ Correct!" if g == st.session_state.num else ("📉 Too Low!" if g < st.session_state.num else "📈 Too High!")

                        st.markdown(f"**Attempt {i}/6** | {feedback} | Guess: **{g}**")
                    else:
                        st.write(f"Attempt {i}: {g}")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Professional footer
st.markdown("""
<div class="footer">
    <p>Built with ❤️ using <a href="https://streamlit.io" target="_blank">Streamlit</a> | 
    Deployed on <a href="https://streamlit.io/cloud" target="_blank">Streamlit Cloud</a> | 
    Original console game converted for web play</p>
</div>
""", unsafe_allow_html=True)

