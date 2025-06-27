import os, sys
from google import genai
from dotenv import load_dotenv

if not sys.argv[1]:
    print("Error: invalid input", file=sys.stderr)
    sys.exit(1)
else:
    query = sys.argv[1]
    
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=query
)
print(response.text)
print('Prompt tokens: ' + str(response.usage_metadata.prompt_token_count))
print('Response tokens: ' + str(response.usage_metadata.candidates_token_count))
