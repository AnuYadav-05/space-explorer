from google import genai
from dotenv import load_dotenv
import os

# Loaded the API key
load_dotenv()

def ask(prompt, model="gemini-2.5-flash-lite"):
    suffix = "The question might be related to space so please answer accordingly: "

    client = genai.Client(api_key=os.getenv("apiKey-Gem")) # Gem is short for gemini for if we decide on using any other api in the future

    response = client.models.generate_content(
        model=model,
        contents=suffix+prompt
    )

    return(response.text)


# Main (Very Temporary)
print(ask(input("Say Something: ")))