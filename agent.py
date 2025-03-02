import logging, openai, re
from config import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY
logging.basicConfig(level=logging.INFO)

class AIAgent:
    def __init__(self):
        self.prompts = {
            "demo_scheduling": {
                "initial": "Namaste {customer_name}, {company_name} se bol raha hoon. {product_name} demo ke liye call kiya hai. Suitable slot batayein?",
                "farewell": "Dhanyavaad, aapse phir baat hogi."
            },
            "candidate_interviewing": {
                "initial": "Namaste, {company_name} se bol raha hoon. {position} interview shuru karte hain. Apne baare mein batayein?",
                "farewell": "Dhanyavaad, interview complete hua."
            },
            "payment_followup": {
                "initial": "Namaste {customer_name}, order #{order_id} ka payment ₹{amount} due hai, {due_date} tak. Payment status batayein?",
                "farewell": "Dhanyavaad, aapse baat karke accha laga."
            }
        }

    def get_initial_prompt(self, scenario, **kwargs):
        return self.prompts.get(scenario, {}).get("initial", "").format(**kwargs)

    def generate_response(self, scenario, context):
        sys_prompt = {
            "demo_scheduling": "You are a professional sales agent speaking in Hinglish.",
            "payment_followup": "You are a polite accounts agent speaking in Hinglish."
        }.get(scenario, "You are a helpful agent in Hinglish.")
        try:
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": context}
                ],
                temperature=0.7, max_tokens=100
            )
            return res.choices[0].message['content'].strip()
        except Exception as e:
            logging.error(e)
            return "Kuch technical problem hai, baad mein try karein."

    def generate_interview_question(self, stage, context):
        try:
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"Interview question on {stage} in Hinglish."},
                    {"role": "user", "content": context}
                ],
                temperature=0.7, max_tokens=50
            )
            return res.choices[0].message['content'].strip()
        except Exception as e:
            logging.error(e)
            return "Kripya apna introduction dein."

    def generate_farewell(self, scenario):
        return self.prompts.get(scenario, {}).get("farewell", "Dhanyavaad, alvida.")
