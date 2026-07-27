from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)
st.write(response.text)

print(response.text)