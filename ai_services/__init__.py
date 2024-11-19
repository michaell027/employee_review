# import torch
# from transformers import pipeline
#
# model_id = "meta-llama/Llama-3.2-3B-Instruct"
# pipe = pipeline(
#     "text-generation",
#     model=model_id,
#     torch_dtype=torch.bfloat16,
#     device_map="auto",
# )
# messages = [
#     {"role": "system", "content": "You are an assistant designed to generate specific questions regarding to a web developer employee for a managerial review."},
#     {"role": "user", "content": "Write 5 questions which you ask manager about the employee who is web developer. The questions should be designed to gather enough detail to write a review. Questions need to be simple and short. No additional information. These questions will be shown to manager. Write it in the JSON format: {questions:[...]}, no additional text."},
# ]
#
# outputs = pipe(
#     messages,
#     max_new_tokens=256,
# )
# print(outputs)

from .client import AIClient
from .llama_handler import generate_manager_questions

__all__ = ["AIClient", "generate_manager_questions"]
