from dotenv import load_dotenv
from langchain_groq import Chartgroq
import os

load_dotenv()

# Fixing typo in 'os.getenv' and 'GROQ_API_KEY'
llm = Chartgroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.2-90b-vision-preview")

if __name__ == "__main__":  # Corrected the condition
    response = llm.invoke("what are the two main ingredients in samosa")
    print(response.content)  # Fixed the typo 'respose' -> 'response'
