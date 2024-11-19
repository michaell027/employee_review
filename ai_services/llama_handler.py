from .client import AIClient

def generate_manager_questions():
    """
    Generates specific questions for a managerial review of a web developer.
    Returns:
        dict: A dictionary containing the generated questions.
    """
    client = AIClient()
    messages = [
        {"role": "system", "content": "You are an assistant designed to generate specific questions regarding to a web developer employee for a managerial review."},
        {"role": "user", "content": "Write 5 questions which you ask manager about the employee who is web developer. The questions should be designed to gather enough detail to write a review. Questions need to be simple and short. No additional information. These questions will be shown to manager. Write it in the JSON format: {questions:[...]}, no additional text."},
    ]

    response = client.call_model(messages)
    return response[0] if response else {"error": "No output generated"}

# Example of usage:
# result = generate_manager_questions()
# print(result)