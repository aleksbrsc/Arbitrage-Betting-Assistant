# creates a bet with purpose to calculating wins or losses for bets
class BettingOddsCalculator:
    def __init__(self, odds, stake):
        self.odds = odds
        self.stake = stake
    
    def calculate_payout(self):
        payout = self.stake * self.odds
        return payout
