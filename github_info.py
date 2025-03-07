import requests
import pandas as pd

BASE_URL = "https://api.github.com/users/"

def get_github_user(username):
    response = requests.get(BASE_URL + username)
    data = response.json()
    
    if response.status_code == 200:
        print(f"Name: {data.get('name', 'N/A')}")
        print(f"Public Repos: {data.get('public_repos', 0)}")
        print(f"Followers: {data.get('followers', 0)}")
    else:
        print("Error:", data["message"])

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    get_github_user(username)
