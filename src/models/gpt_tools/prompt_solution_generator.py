"""Prompt to obtain the solution to a question."""

PROMPT = """
Given an input that contains a question to solve, a metadata object, and a Retrieved Knowledge object.
To response, first review if the question it's a multiple question, if that's the case,
then make sure to select the answer from the given options ["A", "B", "C", "D", "E"].
Please response as the follow json format:
{
    "Solution": [Solution],
    "Answer": [Answer]
}
Where [Solution] is a list of strings, each string is a step of the solution, and [Answer] is the answer to the question,
that follows STRICTLY this format:
"The answer is [ANSWER]", where [ANSWER] is the correct option from ["A", "B", "C", "D", "E"].
If the answer is not in the options, select the most possible option.

On the other hand, if the question is an open-ended question, follow the same json format to responde, but the answer should be a string:
"The answer is [ANSWER]", where [ANSWER] is the answer to the question.

The response SHOULD ONLY CONTAIN the previously described JSON. DO NOT include the question in the response, neither the metadata,
neither retrived knowledge, neither any other information, ONLY the JSON, otherwise the response will be wrong.


Input example of a multiple-choice question:
Question: Which property do a computer and a cellphone have in common?
Options: (A) Size (B) Internet Access

Metadata JSON: {"Metadata": {"input_type": "text", "answer_type": "multiple_choice", "domain": "technology", "skill": "Compare", "difficulty": "1"}}

Retrieved knowledge:
- This question is about identifying a common property between two electronic devices: a computer and a cellphone.
- Computers and cellphones are both examples of electronic devices that use digital technology.
- They are both used for communication and information sharing, as well as for entertainment and productivity.
- The size of electronic devices can vary widely, depending on their intended use and the technology they use.
- Internet access is a common feature of many modern electronic devices, including computers and cellphones.

Response JSON: 
{
    "Solution": [
        "An object has different properties.",
        "A property of an object can tell you how it looks, feels, tastes, or smells.",
        "Different objects can have the same properties.",
        "You can use these properties to put objects into groups.",
        "Look at each object. For each object, decide if it has that property.",
        "The size of electronic devices can vary widely, depending on their intended use and the technology they use.",
        "The property that both objects have in common is internet access."
    ],
    "Answer": "The answer is option B: Internet Access"
}

Input example of a open-ended question:
Question: What is the speed of light in a vacuum?

Metadata JSON: {"Metadata": {"input_type": "text", "answer_type": "open_ended", "domain": "physics", "skill": "Explain", "difficulty": "1"}}

Retrieved knowledge:
- This question is about the speed of light in a vacuum, which is a fundamental concept in physics.
- The speed of light is defined as the distance light travels in a vacuum in a given amount of time.
- The speed of light in a vacuum is constant and is approximately 299,792,458 meters per second (m/s).
- The speed of light is denoted by the symbol "c" and is considered to be the fastest possible speed in the universe.
- The speed of light has important implications for many areas of physics, including relativity, optics, and quantum mechanics.
- The speed of light can be measured using various experimental techniques, including interferometry and time-of-flight measurements.

Response JSON:
{
    "Solution": [
        "This question is about the speed of light in a vacuum, which is a fundamental concept in physics.",
        "The speed of light is defined as the distance light travels in a vacuum in a given amount of time.",
        "The speed of light in a vacuum is constant and is approximately 299,792,458 meters per second (m/s).",
        "The speed of light is denoted by the symbol 'c' and is considered to be the fastest possible speed in the universe.",
        "The speed of light has important implications for many areas of physics, including relativity, optics, and quantum mechanics.",
        "The speed of light can be measured using various experimental techniques, including interferometry and time-of-flight measurements."
    ],
    "Answer": "The answer is 299,792,458 m/s."
}


Now answer the following question:

"""
