from dataclasses import asdict
from typing import List, Dict

import requests

from app.domain.value_objects import GeneratedQuestions, Evaluation, Review
from app.drivers.llama.llama_client import LlamaClient

llama_client = LlamaClient()


def check_llama_status():
    """Check if LLaMA API is running."""
    try:
        response = requests.get(llama_client.api_url)
        if response.status_code == 200:
            return {"status": "LLaMA is running"}
        else:
            raise Exception("LLaMA API is not responding correctly.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error connecting to LLaMA API: {e}")


def ask_llama_questions(employee_role: str):
    """Send a prompt to LLaMA API and return the generated response."""
    prompt = (
        f"Write 5 questions which you ask a manager about an employee who is a {employee_role}. The questions should "
        "be designed to gather enough detail to write a review. Questions need to be simple, short, and general. "
        "Avoid using any specific names, roles, or project titles. These questions will be shown to the manager. "
        "Write it in the JSON format."
    )

    json_format = {
        "type": "object",
        "properties": {
            "questions": {
                "type": "array",
                "items": {"type": "string"}
            }
        },
        "required": ["questions"]
    }

    try:
        response = llama_client.call_model(prompt, json_format)
        return GeneratedQuestions.from_json(response)
    except Exception as e:
        raise Exception(f"Error generating questions from LLaMA API: {e}")


def generate_review_based_on_evaluation(evaluation: Evaluation):
    """Generate a review based on the evaluation."""
    try:
        prompt = (
            f"Write a review of an employee based on the following evaluation: {asdict(evaluation)}. "
            "The review should be written in the second person singular, addressing the employee directly using 'you'. "
            "The review should be constructive and provide feedback on the employee's performance. "
            "Write it in the JSON format. Don't add any additional text, output must be only in the JSON format. "
        )

        json_format = {
            "type": "object",
            "properties": {
                "review": {
                    "type": "string"
                }
            },
            "required": ["review"]
        }

        response = llama_client.call_model(prompt, json_format)
        review = Review.from_json(response)

        return review.review.replace("\n", " ").strip()
    except Exception as e:
        raise Exception(f"Error connecting to LLaMA API: {e}")


def make_answers_from_evaluation_neutral(evaluation: Evaluation):
    """Make the answers in the evaluation neutral."""
    prompt = (
        f"Make the answers in the following evaluation neutral: {Evaluation.to_json(evaluation)}. "
        "The answers should be neutral and not contain any positive or negative sentiment. "
        "You should only change the answers, not the questions. "
        "Modify only the answers that contain expressive language or strong opinions. "
        "Other questions should be left unchanged. "
        "Your output must be strictly in the JSON format."
    )

    json_format = {
        "type": "object",
        "properties": {
            "evaluation": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "question": {"type": "string"},
                        "answer": {"type": "string"}
                    },
                    "required": ["question", "answer"]
                }
            }
        },
        "required": ["evaluation"]
    }

    try:
        response = llama_client.call_model(prompt, json_format)
        print(response)
        return Evaluation.from_json(response)
    except Exception as e:
        raise Exception(f"Error connecting to LLaMA API: {e}")


def ask_llama_to_change_review(messages: List[Dict[str, str]]):
    """Ask LLaMA to change the review based on the messages."""
    try:
        json_format = {
            "type": "object",
            "properties": {
                "review": {
                    "type": "string"
                }
            },
            "required": ["evaluation"]
        }

        response = llama_client.call_chat_model(messages, json_format)

        return response
    except Exception as e:
        raise Exception(f"Error connecting to LLaMA API: {e}")
