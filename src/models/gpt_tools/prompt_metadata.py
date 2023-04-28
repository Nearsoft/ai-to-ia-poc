"""Prompt to obtain the metadata for a question."""

PROMPT = """
Read the following examples, that contain a question and its metadata, generate the metadata JSON for the next question,
and return as content the generated metadata JSON as the LONE output.

The metadata object is a JSON with the following structure:

{"Metadata": {"input_type": "text", "answer_type": "multiple_choice", "domain": "technology", "skill": "Compare", "difficulty": "1"}}

# The options for input_type are: text, number, image, audio, video, math, code, and select.
# The options for answer_type are: multiple_choice, boolean, image, open_answer, and number.
# The options for skill: Compare, Describe, Explain, Identify, Predict, and Summarize.
# The options for difficulty are: 1, 2, 3, 4, and 5. Where 1 is the easiest and 5 is the hardest.


Example one:

Question: Which property do a computer and a cellphone have in common?

Options: (A) Size (B) Internet Access

Metadata JSON: {"Metadata": {"input_type": "text", "answer_type": "multiple_choice", "domain": "technology", "skill": "Compare", "difficulty": "1"}}


Example two:

Question: What is the speed of light in a vacuum?

Metadata JSON: {"Metadata": {"input_type": "text", "answer_type": "open_answer", "domain": "physics", "skill": "Explain", "difficulty": "1"}}



Now generate the metadata object for the following question:

Question: """
