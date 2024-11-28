import requests

post_id = 1
base_URL = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"

post_response = requests.get(base_URL)

if post_response.status_code == 200:
    data = post_response.json()
    
    new_comment = {
        "id": len(data) + 1,
        "post_id": post_id,
        "name": "John Doe",
        "email": "example@email.com",
        "body": "This is a new comment"}
    post_response = requests.post(base_URL, json=new_comment)
    if post_response.status_code == 201:
        print("Comment added successfully")
    else:
        print(f"Error: {post_response.status_code}")
        
new_comment["body"] = "This is an updated comment"
        
put_response = requests.put(f"{base_URL}/{new_comment['id']}", json=new_comment)

if put_response.status_code == 200:
    print("Comment updated successfully")
else:
    print(f"Error: {put_response.status_code}")