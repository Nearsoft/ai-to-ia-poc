
# 
prompt = """
Read the following example, that contain a question and it's metadata, and generate the metadata object for the next question.

Example:
Question: Which property a computer and a celphone have in common?

Options: (A) Size (B) Internet Access

Metadata: {'input_type': 'text', 'answer_type': 'multiple_choice', 'domain': 'technology', 'skill': 'Compare', difficulty: 1}
# The options for input_type are: text, number, image, audio, video, math, code, and select.
# The options for answer_type are: multiple_choice, boolean, image, open_answer, and number.
# The options for skill: Compare, Describe, Explain, Identify, Predict, and Summarize.
# The options for difficulty are: 1, 2, 3, 4, and 5.


Now generate the metadata for the following question:

Question: Is the following statement about our solar system true or false? Jupiter's volume is more than ten times as large as Saturn's volume. 

Options: (A) true (B) false

"""