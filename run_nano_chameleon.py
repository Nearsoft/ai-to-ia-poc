"""
Run the NanoChameleon demo.
"""
import streamlit as st
from dotenv import load_dotenv
from src.core.plan_generator import PlanGenerator
from src.core.orchestrator import Orchestrator

load_dotenv()

if __name__ == "__main__":
    PROMPT = (
        "Question: What is Jupiter's volume in cubic kilometers?\n"
        "Options: (A) 1,431,281,810,739,360 cubic kilometers"
        "  (B) 2,039,471,207,872,154 cubic kilometers"
    )

    st.title("NanoChameleon Demo")
    st.markdown("A plug-and-play compositional reasoning framework")
    st.image("chamaleon.png")
    st.divider()
    st.subheader("Ask us a question:")
    question_container = st.text_input(label="Question", value="Example: What is Jupiter's volume in cubic kilometers?")
    enable_answer = st.radio(label='Do you want to provide any options?', options=("Yes", "No"), index=1)
    enable_options = True
    if enable_answer == 'Yes':
        enable_options = False
    options_container = st.text_input("Options", "A) 1,431,281,810,739,360 cubic kilometers B) 2,039,471,207,872,154 cubic kilometers", disabled=enable_options)
    left_column, right_column = st.columns(2)
    button = left_column.button(label='Send')
    st.divider()
    st.subheader("Answer:")
    
    if button:
        print("starting")
        plan = PlanGenerator.generate_plan(question_container)
        answer = Orchestrator.execute_plan(plan)
        print(f"\nResult: {answer}\n")
        st.text(answer)