def generate_prompt(question, options, metadata):

    prompt = """
        Read the following example, that contain a question and it's metadata, and generate the metadata object for the next question.

        Example:
        Question: Which property a computer and a celphone have in common?

        Options: (A) Size (B) Internet Access
        "Metadata" {"input_type": "text", "answer_type": "multiple_choice", "domain": "technology", "skill": "Compare", "difficulty": "1"}
        # The options for input_type are: text, number, image, audio, video, math, code, and select.
        # The options for answer_type are: multiple_choice, boolean, image, open_answer, and number.
        # The options for skill: Compare, Describe, Explain, Identify, Predict, and Summarize.
        # The options for difficulty are: 1, 2, 3, 4, and 5. Where 1 is the easiest and 5 is the hardest.


        Now generate the metadata for the following question:

        Question: {question}

        Options: {options}

        """
    return prompt.format(question=question, options=options, metadata=metadata)

