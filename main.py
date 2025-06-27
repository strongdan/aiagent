import os, sys
from google import genai
from google.genai import types
from dotenv import load_dotenv

if len(sys.argv) < 2 or not sys.argv[1]:
    print("Error: invalid input", file=sys.stderr)
    sys.exit(1)

query = sys.argv[1]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

messages = [
    types.Content(role="user", parts=[types.Part(text=query)]),
]

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)

if len(sys.argv) >= 3 and sys.argv[2] == '--verbose':
    print('User prompt: ' + query)
    print('Prompt tokens: ' + str(response.usage_metadata.prompt_token_count))
    print('Response tokens: ' + str(response.usage_metadata.candidates_token_count))

print(response.text)
