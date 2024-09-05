from transformers import pipeline

# Load a pre-trained GPT-2 model for text generation
chatbot = pipeline('text-generation', model='gpt2')

def generate_response(image_objects, user_query):
    # Combine the image objects and user query into a prompt
    prompt = f"I see the following objects in the image: {', '.join([obj[1] for obj in image_objects])}. User asks: {user_query}"
    
    # Generate a response
    response = chatbot(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']
    
    return response

# Test the function
user_query = "What can you tell me about this image?"
response = generate_response(recognized_objects, user_query)
print(response)
