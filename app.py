import streamlit as st
from src.values_data import VALUES_WORDS
from src.hf_client import generate_values_statement


# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="AI Values Discovery Assistant",
    page_icon="🧭",
    layout="centered",
)

# ---------------------------
# TITLE
# ---------------------------
st.title("AI Values Discovery Assistant")
st.write(
    "Discover your core values and turn them into a polished personal values statement. "
    "This tool can also support advisor-client discovery conversations."
)

# ---------------------------
# STEP 1: SELECT VALUES
# ---------------------------
st.subheader("Step 1: Select values that resonate with you")

selected_values = st.multiselect(
    "Choose at least 5 values:",
    options=VALUES_WORDS,
)

# ---------------------------
# STEP 2: NARROW TO TOP 5
# ---------------------------
if selected_values:
    st.subheader("Step 2: Narrow down to your Top 5 values")

    if len(selected_values) < 5:
        st.warning("Please select at least 5 values to continue.")
    else:
        st.write("Select the **5 most important values** from your list:")

        top_values = st.multiselect(
            "Your Top 5 Values:",
            options=selected_values,
            max_selections=5,
        )

        if len(top_values) < 5:
            st.info("Select exactly 5 values to continue.")
        else:
            st.success("Great. These are your core values:")
            st.write(", ".join(top_values))  # cleaned display

            st.divider()

            # ---------------------------
            # STEP 3: REFLECTION
            # ---------------------------
            st.subheader("Step 3: Reflect on your values")

            st.write(
                "Answer a few short questions. These will help generate your personal values statement."
            )

            why_value = st.text_area(
                "Why are these values important to you?",
                placeholder="Example: I value growth because I want to continuously improve...",
            )

            decision_example = st.text_area(
                "Describe a time when one of these values influenced a major decision:",
                placeholder="Example: I chose a more challenging path because growth mattered more than comfort...",
            )

            living_values = st.text_area(
                "What does living these values look like in your daily life?",
                placeholder="Example: I prioritize learning, take on challenges, and treat others with respect...",
            )

            # ---------------------------
            # STEP 4: GENERATE
            # ---------------------------
            if why_value.strip() and decision_example.strip() and living_values.strip():
                st.success("Ready to generate your values statement.")

                if st.button("Generate Values Statement"):
                    with st.spinner("Generating your statement..."):
                        result = generate_values_statement(
                            top_values=top_values,
                            why=why_value,
                            decision=decision_example,
                            living=living_values,
                        )

                    st.markdown(result)
                    
                   