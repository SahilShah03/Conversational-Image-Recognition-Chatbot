def chatbot_pipeline(image_path, user_query):
    # Recognize objects in the image
    recognized_objects = recognize_image(image_path)
    
    # Generate a response based on recognized objects and the user's query
    response = generate_response(recognized_objects, user_query)
    
    return response

# Example usage
image_path = 'sample_image.jpg'  # Replace with your image path
user_query = "What do you see in this image?"
chatbot_response = chatbot_pipeline(image_path, user_query)
print(chatbot_response)
