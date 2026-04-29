notes = []

def add_note(text):
    from app.models import create_note
import time

note["created"] = int(time.time())
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
n["updated"] = int(time.time())
def delete_note(id):
    global notes
    before = len(notes)
    notes = [n for n in notes if n["id"] != id]

    if len(notes) == before:
        return {"error": "Note not found"}

    return {"status": "deleted"}
def clear():
    global notes
    notes = []

def get_notes_sorted():
    return sorted(notes, key=lambda x: x["id"])
return success(get_notes_sorted())
def search_notes(query):
    return [n for n in notes if query.lower() in n["text"].lower()]
"""note"""
