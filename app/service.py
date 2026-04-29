notes = []

def add_note(text):
    from app.models import create_note

note = create_note(len(notes) + 1, text)

if not note:
    return {"error": "Invalid data"}
    notes.append(note)
    return note

def get_notes():
    return notes

def update_note(id, text):
    for n in notes:
        if n["id"] == id:
            if not text:
                return {"error": "Invalid text"}
            n["text"] = text.strip()
            return n
    return {"error": "Note not found"}

def delete_note(id):
    global notes
    notes = [n for n in notes if n["id"] != id]
