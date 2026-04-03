import streamlit as st
from src.values_data import VALUES_WORDS

st.set_page_config(
    page_title="AI Values Discovery Assistant",
    page_icon="🧭",
    layout="centered",
)

st.title("AI Values Discovery Assistant")
st.write(
    "Discover your core values and turn them into a draft personal values statement. "
    "This tool can also support advisor-client discovery conversations."
)

st.subheader("Step 1: Select values that resonate with you")
selected_values = st.multiselect(
    "Choose at least 5 values:",
    options=VALUES_WORDS,
)

if selected_values:
    st.subheader("Your selected values")
    st.write(selected_values)

    if len(selected_values) < 5:
        st.info("Select at least 5 values to continue.")
    else:
        st.success("Great. These are your core values:")
        st.write(selected_values)

        st.divider()

        # ---------------------------
        # STEP 2: REFLECTION
        # ---------------------------
        st.subheader("Step 2: Reflect on your values")

        st.write(
            "Answer a few short questions. These will help generate your personal values statement."
        )

        why_value = st.text_area(
            "Why are these values important to you?",
            placeholder="Example: I value freedom because I want to control my time and decisions...",
        )

        decision_example = st.text_area(
            "Describe a time when one of these values influenced a major decision:",
            placeholder="Example: I chose a career change because growth mattered more than stability...",
        )

        living_values = st.text_area(
            "What does living these values look like in your daily life?",
            placeholder="Example: I prioritize learning, act with integrity, and invest in my family...",
        )

        if why_value and decision_example and living_values:
            st.success("Perfect. Next step: generate your values statement.")

            if st.button("Generate Values Statement"):
                statement = f"My core values are {', '.join(selected_values)}. {why_value} {decision_example} {living_values}"
                st.write("Your Personal Values Statement:")
                st.write(statement)