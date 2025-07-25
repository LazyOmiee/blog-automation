import sys
import google.generativeai as genai

API_KEY = "AIzaSyCwsYkyXDRliZ51S-0eE4kAh7h2u10D08g"  # Your Google API key here
genai.configure(api_key=API_KEY)

def generate_blog(keyword):
    prompt = f"""
    Write a detailed blog post about '{keyword}'.
    Include:
    - Meta title
    - Meta description
    - Meta tags (comma separated)
    - Suggested URL slug
    - Blog content (with markdown for images if relevant)
    Respond in JSON with keys: meta_title, meta_description, meta_tags, url_slug, content.
    """
    model = genai.GenerativeModel('models/gemini-1.5-pro-latest')
    response = model.generate_content(prompt)
    return response.text

def main():
    print("=== Auto Blog Bot ===")
    keyword = input("Enter a keyword or blog title: ")
    print(f"You entered: {keyword}")
    print("Generating blog post using Gemini...")
    blog_json = generate_blog(keyword)
    print("\nGenerated Blog Post (raw JSON):\n")
    print(blog_json)
    # Next: Parse JSON, send to WordPress

if __name__ == "__main__":
    main() 