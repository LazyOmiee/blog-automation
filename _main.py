
import requests

# Replace with your actual Make.com webhook URL
webhook_url = ""
print("=== Auto Blog Bot ===")

while True:
    blog_topic = input("\nEnter a blog topic (or type 'exit' to quit): ")
    if blog_topic.lower() == 'exit':
        print("Exiting Auto Blog Bot.")
        break

    print(f"You entered: {blog_topic}")

    # Send to Make.com
    data = {"topic": blog_topic}
    response = requests.post(webhook_url, json=data)

    if response.status_code == 200:
        print(" Blog generation triggered successfully.")
    else:
        print(" Failed to trigger webhook. Status code:", response.status_code)
