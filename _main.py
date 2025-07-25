# import requests

# print("=== Auto Blog Bot ===")
# blog_topic = input("Enter a blog topic: ")
# print(f"You entered: {blog_topic}")

# # Replace with your actual Make.com webhook URL
# #webhook_url = "https://hook.eu2.make.com/qomzvs47n7phfvxplslnb8mlp79hgqur"
# webhook_url = "https://hook.eu2.make.com/o7fu4gtqw61v1z3d37cjl23tlky3abks"
#


# # Send to Make.com
# data = {"topic": blog_topic}
# response = requests.post(webhook_url, json=data)

# if response.status_code == 200:
#     print(" Blog generation triggered successfully.")
# else:
#     print("Failed to trigger webhook. Status code:", response.status_code)

#---------------------------------------------------------------------------------------

import requests

# Replace with your actual Make.com webhook URL
webhook_url = "https://hook.eu2.make.com/o7fu4gtqw61v1z3d37cjl23tlky3abks"
# webhook_url = "https://hook.eu2.make.com/90gzdsalfby7u2bulg8rfi9ntld982ie"
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
