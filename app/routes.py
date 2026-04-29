from app.service import add_note, get_notes, update_note, delete_note

def handle_request(method, path, data=None):
    if method == "GET" and path == "/notes":
       return success(get_notes())

    if method == "POST" and path == "/notes":
        result = add_note(data.get("text") if data else None)
        return success(get_notes())

    if method == "PUT" and path.startswith("/notes/"):
        id = int(path.split("/")[-1])
        result = update_note(id, data.get("text") if data else None)
       return success(get_notes())

    if method == "DELETE" and path.startswith("/notes/"):
        id = int(path.split("/")[-1])
        return delete_note(id)

return error("Route not found")

def success(data):
    return {"status": "ok", "data": data}

def error(msg):
    return {"status": "error", "message": msg}
if method == "GET" and path.startswith("/search"):
    q = path.split("=")[-1]
    return success(search_notes(q))
try:
    id = int(path.split("/")[-1])
except:
    return error("Invalid ID")
