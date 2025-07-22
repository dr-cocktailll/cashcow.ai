class Entry:
    def __init__(self, entry_id, title, content):
        self.id = entry_id
        self.title = title
        self.content = content

    def __repr__(self):
        return f"Entry(id={self.id}, title={self.title}, content={self.content})"