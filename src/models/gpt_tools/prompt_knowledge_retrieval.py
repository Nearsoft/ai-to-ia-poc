"""???"""

PROMPT = """
Read the following question, and generate the background knowledge as the context information
that could be helpful for answering the question.


Example one:

Question: Which property do handkerchief, slippers, and leisure suit have in common?

Options: (A) hard (B) soft (C) yellow

Knowledge: 
- This question is about comparing the properties of three objects: a handkerchief, slippers, and a
leisure suit.
- The objects are related to the topic of physics and the skill of comparing properties of objects.
- Properties of objects can include physical characteristics such as color, texture, shape, size, weight,
and material.

Example two:

Question: When you bring two magnets close to each other, how do North poles and Sout pole interact?

Knowledge: 
-Magnets interact based on the polarity of their magnetic poles.
-Opposite poles attract each other.
-The attractive force increases as the magnets get closer together.
-The attractive force decreases as the magnets move further apart.
-This magnetic interaction is governed by the fundamental principles of magnetism.

Read the following question, generate the background knowledge as the context information that could be helpful for answering the question.
Provide the response as a bulleted point list followed by the word Knowkedge.
Question: """
