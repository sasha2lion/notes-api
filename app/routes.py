from app.service import (
    add_note,
    get_notes_sorted,
    update_note,
    delete_note,
    search_notes
)

def success(data):
    return {"status": "ok", "data": data}

def error(msg):
    return {"status": "error", "message": msg}

def handle_request(method, path, data=None):

    if method == "GET" and path == "/notes":
        return success(get_notes_sorted())

    if method == "POST" and path == "/notes":
        result = add_note(data.get("text") if data else None)
        return success(result)

    if method == "PUT" and path.startswith("/notes/"):
        try:
            id = int(path.split("/")[-1])
        except:
            return error("Invalid ID")

        result = update_note(id, data.get("text") if data else None)
        return success(result)

    if method == "DELETE" and path.startswith("/notes/"):
        try:
            id = int(path.split("/")[-1])
        except:
            return error("Invalid ID")

        return delete_note(id)

    if method == "GET" and path.startswith("/search"):
        q = path.split("=")[-1]
        return success(search_notes(q))

    return error("Route not found")
