def create_note(id, text):
    if not text or not isinstance(text, str):
        return None

    return {
        "id": id,
        "text": text.strip()
    }
if len(text) > 200:
    return None
text = text.strip()
