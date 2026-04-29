from app.service import add_note, get_notes

def test_add_note():
    add_note("Test")
    assert len(get_notes()) > 0
