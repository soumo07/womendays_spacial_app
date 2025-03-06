import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Streamlit UI - Set Page Config
st.set_page_config(page_title="Women's Day Special", layout="wide")

# Custom CSS for styling and positioning elements properly
st.markdown(
    """
    <style>
        .main {
            background: white;
            color: black;
            text-align: center;
            padding: 10px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
        }
        .poem-box {
            background: rgba(255, 105, 180, 0.9);
            padding: 25px;
            border-radius: 15px;
            font-weight: bold;
            font-size: 22px;
            color: white;
            box-shadow: 5px 5px 12px rgba(0, 0, 0, 0.3);
            font-family: 'Georgia', serif;
            text-align: center;
            width: 80%;
            margin: auto;
        }
        .special-message {
            background: rgba(255, 182, 193, 0.9);
            padding: 20px;
            border-radius: 12px;
            font-size: 24px;
            font-weight: bold;
            color: darkred;
            box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);
            font-family: 'Verdana', sans-serif;
            text-align: center;
            width: 80%;
            margin: auto;
        }
        .label {
            font-size: 22px;
            font-weight: bold;
            color: purple;
            font-family: 'Arial', sans-serif;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            display: block;
            margin-bottom: 10px;
            text-align: center;
        }
        .input-container {
            text-align: center;
            margin-bottom: 20px;
            margin-top: 10px;
        }
        .title-container {
            text-align: center;
            font-size: 30px;
            font-weight: bold;
            color: #d63384;
            margin-top: 10px;
        }
        .fixed-image {
            text-align: center;
            margin-bottom: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the image at the top with centered alignment
st.markdown(
    "<div class='fixed-image'>"
    "<img src='https://motivationalspeakersagency.co.uk/sites/default/files/2021-01/International%20Women%26%23039%3Bs%20Day%20Blog%20Image_0.jpg' width='600'/>"
    "</div>",
    unsafe_allow_html=True
)

# Centered Title
st.markdown("<div class='title-container'>🌸 Happy Women's Day! 🌸</div>", unsafe_allow_html=True)

# Input Box (Visible without scrolling)
st.markdown("<div class='input-container'>", unsafe_allow_html=True)
st.markdown("<label class='label'>Enter your name:</label>", unsafe_allow_html=True)
name = st.text_input("", key="name_input")
st.markdown("</div>", unsafe_allow_html=True)

# Function to generate a Women's Day poem
def generate_poem(name):
    lines = [
        f"{name}, you shine like the morning light,",
        "Strong and fearless, bold and bright.",
        "On this Women's Day, we celebrate you,",
        "A soul so kind, a heart so true.",
        f"{name}, keep soaring, never sway,",
        "Happy Women's Day, enjoy your day!"
    ]
    return "<br>".join(lines)

# Function to plot a heart shape with the name inside
def plot_heart_with_name(name):
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    fig, ax = plt.subplots(figsize=(4, 4))  # Decreased size
    ax.plot(x, y, 'r', linewidth=3)
    ax.set_aspect(1)
    ax.axis("off")

    # Add text inside the heart
    ax.text(0, 0, name, fontsize=12, color='red', fontweight='bold', ha='center', va='center')

    return fig

if name:
    st.subheader(f"Hello, {name}! 💖")
    st.markdown("<label class='label'>Here is a special message for you:</label>", unsafe_allow_html=True)
    st.markdown("<div class='special-message'>You are strong, you are powerful, and you inspire the world!</div>",
                unsafe_allow_html=True)

    st.markdown("<label class='label'>Here's a poem just for you:</label>", unsafe_allow_html=True)
    st.markdown(f"<div class='poem-box'>{generate_poem(name)}</div>", unsafe_allow_html=True)

    st.markdown("<label class='label'>And a special love sign for you:</label>", unsafe_allow_html=True)
    st.pyplot(plot_heart_with_name(name))
