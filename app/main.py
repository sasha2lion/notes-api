from app.routes import handle_request

if __name__ == "__main__":
    print(handle_request("POST", "/notes", {"text": "Hello"}))
    print(handle_request("GET", "/notes"))
