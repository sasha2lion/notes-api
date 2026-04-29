from app.models import create_note
import time

notes = []

def add_note(text):
    note = create_note(len(notes) + 1, text)

    if not note:
        return {"error": "Invalid data"}

    note["created"] = int(time.time())
    notes.append(note)

    return note

def get_notes():
    return notes

def get_notes_sorted():
    return sorted(notes, key=lambda x: x["id"])

def update_note(id, text):
    for n in notes:
        if n["id"] == id:
            if not text:
                return {"error": "Invalid text"}

            n["text"] = text.strip()
            n["updated"] = int(time.time())
            return n

    return {"error": "Note not found"}

def delete_note(id):
    global notes
    before = len(notes)

    notes = [n for n in notes if n["id"] != id]

    if len(notes) == before:
        return {"error": "Note not found"}

    return {"status": "deleted"}

def search_notes(query):
    return [n for n in notes if query.lower() in n["text"].lower()]

def clear():
    global notes
    notes = []
