"""Prompt to obtain the solution to a question."""

PROMPT = """
Given the question, check if it's a multiple question, if it is select the answer from the options ["A", "B", "C", "D", "E"].
You should give concise and step-by-step solutions. Finally, conclude the answer in the format of
"the answer is [ANSWER]", where [ANSWER] is one from the options ["A", "B", "C", "D", "E"].
For example, "the answer is A", "the answer is B", "the answer is C", "the answer is D", or "the
answer is E". If the answer is not in the options, select the most possible option.

If the question is an open-ended question, you should give concise and step-by-step solutions. Finally, conclude the answer in the format of
"the answer is [ANSWER]", where [ANSWER] is the answer to the question.

Example of a multiple-choice question:
Question: Which property do a computer and a cellphone have in common?
Options: (A) Size (B) Internet Access

Metadata JSON: {"Metadata": {"input_type": "text", "answer_type": "multiple_choice", "domain": "technology", "skill": "Compare", "difficulty": "1"}}

Retrieved knowledge:
- This question is about identifying a common property between two electronic devices: a computer and a cellphone.
- Computers and cellphones are both examples of electronic devices that use digital technology.
- They are both used for communication and information sharing, as well as for entertainment and productivity.
- The size of electronic devices can vary widely, depending on their intended use and the technology they use.
- Internet access is a common feature of many modern electronic devices, including computers and cellphones.

Solution: An object has different properties. A property of an object can tell you how it looks,
feels, tastes, or smells. Different objects can have the same properties. You can use these properties
to put objects into groups. Look at each object. For each object, decide if it has that property.
The size of electronic devices can vary widely, depending on their intended use and the technology they use.
The property that both objects have in common is internet access. Therefore, the answer is B.

Example of a open-ended question:
Question: What is the speed of light in a vacuum?

Metadata JSON: {"Metadata": {"input_type": "text", "answer_type": "open_ended", "domain": "physics", "skill": "Explain", "difficulty": "1"}}

Retrieved knowledge:
- This question is about the speed of light in a vacuum, which is a fundamental concept in physics.
- The speed of light is defined as the distance light travels in a vacuum in a given amount of time.
- The speed of light in a vacuum is constant and is approximately 299,792,458 meters per second (m/s).
- The speed of light is denoted by the symbol "c" and is considered to be the fastest possible speed in the universe.
- The speed of light has important implications for many areas of physics, including relativity, optics, and quantum mechanics.
- The speed of light can be measured using various experimental techniques, including interferometry and time-of-flight measurements.

Solution:
The speed of light in a vacuum is approximately 299,792,458 meters per second (m/s). Therefore, the answer is 299,792,458 m/s.

"""
