class MemoryNode:
    def __init__(self, date: str, description: str, emotion: str):
        self.date = date
        self.description = description
        self.emotion = emotion

        self.next = None
        self.prev = None

    def __str__(self):
        return f"[{self.date}] {self.emotion.upper()} - {self.description}"