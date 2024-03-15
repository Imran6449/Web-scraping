import requests

# API endpoint for fetching posts
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
posts = response.json()  # Convert the response to JSON

# Open a file to write the posts
with open('posts.txt', 'w') as file:
    for post in posts:
        title = post['title']
        body = post['body']
        file.write(f"Title: {title}\nBody: {body}\n\n")

print("Posts have been saved to posts.txt.")

