class Query:
    def __init__(self, id, text) -> None:
        self.id = id
        self.text = text
        
    def serialize(self):
        return {
            'id': self.id,
            'text': self.text
        }