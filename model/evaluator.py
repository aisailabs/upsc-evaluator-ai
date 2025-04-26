import openai
import json

# Load model answers (later you can store this in DB)
with open("data/model_answers.json") as f:
    model_answers = json.load(f)

def evaluate_answer(question_id: str, user_answer: str) -> dict:
    model_answer = model_answers.get(question_id, "No model answer found.")
    prompt = f"""
You are a UPSC examiner. Compare the student's answer with the model answer and grade it out of 15.

Model Answer:
{model_answer}

Student's Answer:
{user_answer}

Return your response in this format:
Score: X/15
Strengths: ...
Areas of Improvement: ...
Suggestions: ...
"""

    response = openai.ChatCompletion.create(
        model = "gpt-4-turbo",
        messages = [{"role": "user", "content": prompt}],
        temperature = 0.4,
    )

    return {"feedback": response["choices"][0]["message"]["content"]}
