from app.service import add_note, get_notes

def test_add_note():
    add_note("Test")
    assert len(get_notes()) > 0

from app.service import update_note

def test_update():
    note = update_note(1, "New")
    assert note["text"] == "New"
