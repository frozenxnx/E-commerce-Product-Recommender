import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def explain_recommendation(user_id, product):
    prompt = f"""
    User recently viewed or interacted with items in the {product['category']} category.
    Product: {product['title']} ({product['tags']})
    Price: {product['price']}

    Write 2 short sentences explaining why this product might be recommended to the user.
    Be factual, concise, and friendly. Do not invent user preferences.
    """
    response = model.generate_content(prompt)
    return response.text.strip()
