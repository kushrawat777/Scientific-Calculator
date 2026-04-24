import streamlit as st
import math
import random

st.set_page_config(page_title="Scientific Calculator", layout="centered")

st.markdown("""
<style>
    
.stApp {
    background-color: #ffffff;
}

.block-container {
    
    margin: auto;
    border: 2px solid black;
    padding: 10px;
    border-radius: 10px;
    background-color: grey;
    
}

/* Display (top screen) */
.display-box {
    background: black;
    padding: 30px 25px;
    border-radius: 18px;
    text-align: right;
    font-size: 48px;
    font-weight: 500;
    margin-bottom: 25px;
    color: white;

    /* subtle border */
    border: 1px solid #e5e5e5;

    /* soft shadow (premium look) */
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);

    /* smooth edges */
    transition: all 0.2s ease;
}
}

/* Base button */
div.stButton > button {
    width: 100%;
    height: 70px;
    border-radius: 50%;
    font-size: 22px;
    font-weight: 500;
    border: none;
    transition: 0.15s;
}

/* Number buttons */
button[kind="secondary"] {
    background-color: #e5e5ea !important;
    color: #000 !important;
}

/* Operator buttons (+ - × ÷ =) */
button[kind="primary"] {
    background-color: #ff9500 !important;
    color: white !important;
}

/* Function buttons (AC, CE, etc.) */
button[kind="tertiary"] {
    background-color: #d1d1d6 !important;
    color: black !important;
}

/* Hover effect */
div.stButton > button:hover {
    transform: scale(0.95);
}
</style>
""", unsafe_allow_html=True)

if "expr" not in st.session_state:
    st.session_state.expr = ""

if "error" not in st.session_state:
    st.session_state.error = False


def evaluate():
    try:
        e = st.session_state.expr

        e = e.replace("^", "**")
        e = e.replace("%", "/100")

        e = e.replace("sin", "math.sin(math.radians")
        e = e.replace("cos", "math.cos(math.radians")
        e = e.replace("tan", "math.tan(math.radians")

        e = e.replace("log", "math.log10")
        e = e.replace("ln", "math.log")
        e = e.replace("sqrt", "math.sqrt")
        e = e.replace("factorial", "math.factorial")
        e = e.replace("pi", "math.pi")
        e = e.replace("e", "math.e")

        open_brackets = e.count("math.radians")
        e = e + ")" * open_brackets

        result = eval(e)

        if type(result) == float and result.is_integer():
            result = int(result)

        st.session_state.expr = str(result)
        st.session_state.error = False

    except:
        st.session_state.expr = "Error"
        st.session_state.error = True


def handle_click(btn):
    if st.session_state.error:
        st.session_state.expr = ""
        st.session_state.error = False

    if btn == "AC":
        st.session_state.expr = ""

    elif btn == "CE":
        st.session_state.expr = st.session_state.expr[:-1]

    elif btn == "=":
        evaluate()

    elif btn == "sin":
        st.session_state.expr += "sin("

    elif btn == "cos":
        st.session_state.expr += "cos("

    elif btn == "tan":
        st.session_state.expr += "tan("

    elif btn == "log":
        st.session_state.expr += "log("

    elif btn == "ln":
        st.session_state.expr += "ln("

    elif btn == "sqrt":
        st.session_state.expr += "sqrt("

    elif btn == "x!":
        st.session_state.expr += "factorial("

    elif btn == "1/x":
        st.session_state.expr += "1/("

    elif btn == "nCr":
        st.session_state.expr += "math.comb("

    elif btn == "Ran#":
        st.session_state.expr += str(random.random())

    elif btn == "pi":
        st.session_state.expr += "pi"

    elif btn == "e":
        st.session_state.expr += "e"

    elif btn == "x^y":
        st.session_state.expr += "^"

    else:
        st.session_state.expr += btn


st.markdown(
    f'<div class="display-box">{st.session_state.expr if st.session_state.expr else "0"}</div>',
    unsafe_allow_html=True
)

buttons = [
    ["sin", "cos", "tan", "Ran#", "AC"],
    ["log", "ln", "sqrt", "1/x", "CE"],
    ["x!", "nCr", "pi", "e", "x^y"],
    ["7", "8", "9", "(", "/"],
    ["4", "5", "6", ")", "*"],
    ["1", "2", "3", "%", "-"],
    ["0", ".", "+", "="]
]

for row in buttons:
    cols = st.columns(5)

    for i in range(len(row)):
        btn = row[i]

        with cols[i]:

            if btn in ["+", "-", "*", "/", "=", "%"]:
                st.button(btn, on_click=handle_click, args=(btn,), use_container_width=True, type="primary")

            elif btn in ["AC", "CE", "sin", "cos", "tan", "log", "ln", "sqrt", "x!", "nCr", "pi", "e", "x^y", "Ran#"]:
                st.button(btn, on_click=handle_click, args=(btn,), use_container_width=True, type="tertiary")

            else:
                st.button(btn, on_click=handle_click, args=(btn,), use_container_width=True, type="secondary")