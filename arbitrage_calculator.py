class ArbitrageCalculator:
    def __init__(self, odds_list):
        self.odds_list = odds_list

    def calculate_arbitrage(self):
        implied_probabilities = []
        total_implied_probability = 0
        for odds in self.odds_list:
            implied_probability = 1 / odds
            total_implied_probability += implied_probability
            implied_probabilities.append(implied_probability)
        arb_percentage = (1 - total_implied_probability) * 100
        return arb_percentage, implied_probabilities
