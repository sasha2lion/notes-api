from app.service import add_note, get_notes, update_note, delete_note

def handle_request(method, path, data=None):
    if method == "GET" and path == "/notes":
        return get_notes()

    if method == "POST" and path == "/notes":
        return add_note(data["text"])

    if method == "PUT" and path.startswith("/notes/"):
        id = int(path.split("/")[-1])
        return update_note(id, data["text"])

    if method == "DELETE" and path.startswith("/notes/"):
        id = int(path.split("/")[-1])
        delete_note(id)
        return {"status": "deleted"}

    return {"error": "not found"}
