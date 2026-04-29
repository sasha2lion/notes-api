from app.service import add_note, get_notes, update_note, delete_note, clear

def test_add():
    clear()
    add_note("Hello")
    assert len(get_notes()) == 1

def test_update():
    clear()
    add_note("Old")
    updated = update_note(1, "New")
    assert updated["text"] == "New"

def test_delete():
    clear()
    add_note("Test")
    delete_note(1)
    assert len(get_notes()) == 0
