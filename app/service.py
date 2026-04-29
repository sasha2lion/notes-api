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
            n["text"] = text
            return n

def delete_note(id):
    global notes
    notes = [n for n in notes if n["id"] != id]
