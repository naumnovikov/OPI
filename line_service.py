class LineService:
    def __init__(self):
        self.lines = {}

    def add_line(self, event_id, odds):
        self.lines[event_id] = odds
        return True

    def get_odds(self, event_id):
        return self.lines.get(event_id, "Not found")
