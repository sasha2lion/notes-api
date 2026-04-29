notes = []

def add_note(text):
    note = {"id": len(notes) + 1, "text": text}
    notes.append(note)
    return note

def get_notes():
    return notes
