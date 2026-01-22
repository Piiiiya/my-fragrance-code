import streamlit as st

st.set_page_config(page_title="My Fragrance Code", layout="centered")

st.title("✨ My Fragrance Code")
st.subheader("Which L’Oréal Luxury Fragrance Matches You?")

st.write("Your personality has a scent. Discover it below.")

vibe = st.selectbox(
    "Choose your vibe:",
    ["Bold & Confident", "Elegant & Romantic", "Mysterious & Powerful", "Fresh & Free-Spirited"]
)

if vibe == "Bold & Confident":
    st.success("🔥 Your Fragrance Match: **YSL Y**")
    st.write("For leaders, risk-takers, and modern achievers.")

elif vibe == "Elegant & Romantic":
    st.success("🌸 Your Fragrance Match: **Lancôme La Vie Est Belle**")
    st.write("Graceful, timeless, and beautifully feminine.")

elif vibe == "Mysterious & Powerful":
    st.success("🖤 Your Fragrance Match: **Armani Code**")
    st.write("Intense, magnetic, and unforgettable.")

elif vibe == "Fresh & Free-Spirited":
    st.success("🌿 Your Fragrance Match: **Maison Margiela Replica**")
    st.write("Clean, modern, and effortlessly cool.")

st.markdown("---")
st.caption("Concept Project | Luxury Branding | L’Oréal Inspired")
