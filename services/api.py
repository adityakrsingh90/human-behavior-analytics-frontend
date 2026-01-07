import requests

BASE_URL = "https://human-behavior-analytics-backend.onrender.com/api/v1"

def signup(email, password):
    return requests.post(
        f"{BASE_URL}/auth/signup",
        json={"email": email, "password": password}
    )

def login(email, password):
    return requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": email, "password": password}
    )

def predict(token, features):
    return requests.post(
        f"{BASE_URL}/predict",
        headers={"Authorization": f"Bearer {token}"},
        json=features
    )

def explain(token, features):
    return requests.post(
        f"{BASE_URL}/explain",
        headers={"Authorization": f"Bearer {token}"},
        json=features
    )

def send_feedback(token, payload):
    return requests.post(
        f"{BASE_URL}/feedback",
        headers={"Authorization": f"Bearer {token}"},
        json=payload
    )
