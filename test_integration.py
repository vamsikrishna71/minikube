import requests

def test_frontend_response():
    frontend_url = "http://127.0.0.1:11329"  # Replace with the Minikube URL
    response = requests.get(frontend_url)
    
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert "Hello" in response.text, "Greeting message not found in the frontend response."

if __name__ == "__main__":
    test_frontend_response()
    print("Integration test passed!")
