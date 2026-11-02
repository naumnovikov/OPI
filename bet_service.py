class BetService:
    def __init__(self):
        self.bets = []

    def place_bet(self, user_id, amount, event_id):
        bet = {"user": user_id, "amount": amount, "event": event_id}
        self.bets.append(bet)
        return bet

    def get_user_bets(self, user_id):
        return [b for b in self.bets if b["user"] == user_id]
