class Doc:
    def __init__(self, id, title, text) -> None:
        self.id = id
        self.title = title
        self.text = text
        
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text
        } 