from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv
from model.evaluator import evaluate_answer

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class AnswerInput(BaseModel):
    question_id: str
    user_answer: str

@app.post("/evaluate/")
async def evaluate(input_data: AnswerInput):
    result = evaluate_answer(input_data.question_id, input_data.user_answer)
    return result
