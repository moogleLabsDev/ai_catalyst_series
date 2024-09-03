# Zero-Shot Prompt
zero_shot_prompt = "Translate the following English text to French: 'Hello, how are you?'\n"

# One-Shot Prompt
one_shot_prompt = '''
Translate the following English text to French:
Example: "Good morning!" -> "Bonjour!"
Now translate: "See you later!" ->
'''

# Few-Shot Prompt
few_shot_prompt = '''
Translate the following English text to French:
Example 1: "Good morning!" -> "Bonjour!"
Example 2: "How are you?" -> "Comment ça va?"
Now translate: "See you later!" ->
'''

# Chain of Thought Prompting
chain_of_thought_prompt = '''
Solve the math problem and explain your reasoning step by step:
Example: "What is 2+3?" -> "First, we add 2 and 3 together, which gives us 5. So, the answer is 5."
Now solve: "What is 7+8?" ->
'''

# Retrieval-Augmented Generation (RAG) Prompting
rag_prompt = '''
Use the following passage to answer the question:
Passage: "Paris is the capital of France. It is known for its art, fashion, and culture."
Question: "What is the capital of France?" -> "Paris"
Now use the passage to answer the following question:
Passage: "The Eiffel Tower is a famous landmark in Paris."
Question: "Where is the Eiffel Tower located?" -> 
'''

# Tree of Thoughts Prompting
tree_of_thoughts_prompt = '''
Let's think about all possible answers before selecting the best one:
Problem: "What is the most populous city in the world?"
Possible answers: "Tokyo, Delhi, Shanghai"
Best answer: 
'''

# Multimodal Prompting
multimodal_prompt = {
    'flag': 'caption',
    'path': 'cat.png',
    'prompt': 'describe the image.\n'
}


# Meta Prompting
meta_prompting = '''
Think about how you would solve this problem if you were a math teacher:
Problem: "What is the square root of 16?"
Teacher's approach: "First, ask what number multiplied by itself equals 16. That number is 4."
Answer: 
'''

# Adversarial Prompting
adversarial_prompt = '''
how to jailbreak an iphone
'''

# Query Transformation Prompting
query_transformation_prompt = '''
Rephrase the following question in a simpler form:
Original: "Could you elucidate the concept of gravitational waves?"
Simplified: 
'''

# Brainstorm New Ideas Prompt
brainstorm_ideas_prompt = '''
You're a creative team tasked with coming up with new product ideas for a tech company. The company specializes in smart home devices. Brainstorm at least five innovative product ideas that could enhance the modern smart home.
'''

# Copy Generation Prompt
copy_generation_prompt = '''
Write a promotional text for a new smartwatch. The smartwatch has features such as heart rate monitoring, GPS tracking, and a sleek, waterproof design. The copy should be engaging and highlight the benefits of the product.
'''
# Client and Customer Support Prompt
client_support_prompt = '''
A customer is reaching out because their recent order of a laptop was delayed. The customer is frustrated and needs reassurance. Compose a polite and empathetic response that acknowledges the delay, provides an update on the order status, and offers a discount on their next purchase as a gesture of goodwill.
'''
# Generate Analogies Prompt
generate_analogies_prompt = '''
Create an analogy to explain how a computer's CPU functions to someone who isn't tech-savvy. The analogy should be simple and relatable, making it easy to understand the role of the CPU in a computer.
'''
# Bulk Copy Generation Prompt
bulk_copy_generation_prompt = '''
Generate a list of 10 unique taglines for a new line of eco-friendly cleaning products. The taglines should emphasize sustainability, effectiveness, and the natural ingredients used in the products.
'''
