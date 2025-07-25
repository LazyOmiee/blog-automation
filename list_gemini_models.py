import google.generativeai as genai

API_KEY = "AIzaSyCwsYkyXDRliZ51S-0eE4kAh7h2u10D08g"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

models = genai.list_models()
for model in models:
    print(model.name)