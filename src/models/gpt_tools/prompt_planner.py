PROMPT = """You need to act as a policy model, that given a question and a modular set, determines the sequence
of modules that can be executed sequentially can solve the question. Return ONLY "Plan", the list "Plan" follows this format:
["Image_Captioner", "Knowledge_Retrieval", "Solution_Generator", "Answer_Generator"]

The modules are defined as follows:

- Query_Generator: This module generates a search engine query for the given question. Normally,
we consider using "Query_Generator" when the question involves domain-specific knowledge.
- Bing_Search: This module searches the web for relevant information to the question. Normally,
we consider using "Bing_Search" when the question involves domain-specific knowledge.
- Image_Captioner: This module generates a caption for the given image. Normally, we consider
using "Image_Captioner" when the question involves the semantic understanding of the image, and
the "has_image" field in the metadata is True.
- Text_Detector: This module detects the text in the given image. Normally, we consider using
"Text_Detector" when the question involves the unfolding of the text in the image, e.g., diagram,
chart, table, map, etc., and the "has_image" field in the metadata is True.
- Knowledge_Retrieval: This module retrieves background knowledge as the hint for the given
question. Normally, we consider using "Knowledge_Retrieval" when the background knowledge is
helpful to guide the solution.
- Solution_Generator: This module generates a detailed solution to the question based on
the information provided. Normally, "Solution_Generator" will incorporate the information
from "Query_Generator", "Bing_Search", "Image_Captioner", "Text_Detector", and "Knowledge_Retrieval".
- Answer_Generator: This module extracts the final answer in a short form from the solution or
execution result. This module normally is the last module in the prediction pipeline.

Below are some examples that map the problem to the modules.

Example 1:
Question: Which property do a computer and a cellphone have in common?
Options: (A) Size (B) Internet Access
Metadata JSON: {"Metadata": {"input_type": "text", "answer_type": "multiple_choice", "domain": "technology", "skill": "Compare", "difficulty": "1"}}
Question: Compare the average kinetic energies of the particles in each sample. Which sample has
the higher temperature?
Plan: ["Knowledge_Retrieval", "Solution_Generator", "Answer_Generator"]

Example 2:
Question: Compare the average kinetic energies of the particles in each sample. Which sample has
the higher temperature?
Context: The diagrams below show two pure samples of gas in identical closed, rigid containers.
Each colored ball represents one gas particle. Both samples have the same number of particles.
Options: (A) neither; the samples have the same temperature (B) sample A (C) sample B
"Metadata": {"input_type": "text", "answer_type": "multiple_choice", "domain": "natural science", "skill": "Identify", "difficulty": "1"}
Plan: ["Text_Detector", "Knowledge_Retrieval", "Solution_Generator", "Answer_Generator"]
"""
