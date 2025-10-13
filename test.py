import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # loads .env

api_key = os.getenv("GEMINI_API_KEY")  # <- this gets the actual key
print(api_key)  # optional, just to verify

genai.configure(api_key=api_key)

for m in genai.list_models():
    print(m.name)


# from dotenv import load_dotenv
# import os
# import google.generativeai as genai
#
# load_dotenv()  # <- this loads your .env
# api_key = os.getenv("GEMINI_API_KEY")
# print(api_key)  # check that it prints your actual key
#
# genai.configure(api_key=api_key)
