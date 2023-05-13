class ArbitrageCalculator:
    def __init__(self, stake, odds_list):
        self.odds_list = odds_list
        self.stake = stake

    def calc_total_implied_probability(self):
        total_implied_probability = 0
        for odd in self.odds_list:
            total_implied_probability += 1 / odd
        return total_implied_probability

    def calculate_hedged_stakes(self):
        total_implied_probability = self.calc_total_implied_probability()
        hedged_stakes = []
        for odd in self.odds_list:
            implied_probability = 1 / float(odd)
            stake = round((self.stake * implied_probability) / total_implied_probability, 2)
            hedged_stakes.append(stake)
        return hedged_stakes
