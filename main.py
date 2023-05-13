# Basic moneyline arbitrage bet finder program 
# calculates the discrepancies in odds across different bookmakers provided by user input and returns the arbitrage opportunities
# for more info on arbitrage betting: https://en.wikipedia.org/wiki/Arbitrage_betting
import arbitrage
import betting_odds_calculator
import arbitrage_calculator


# variables
first_run = True
# create a collection of bet spaces
# create a collection of bets
# each bet is a list that has two dictionaries for the Team/Player:Odds 

# function to start program
def run():
    main_menu()

# function for displaying the first menu's options
def main_menu():
    global first_run
    # title which only appears the very first time the program is ran
    if first_run == True:
        print("\nARBITRAGE BOT\nSelect one of the following options:")
        first_run = False

    # display main menu options
    print("\n[1] Create Bet Space\n[2] Visit Bet Spaces\n[3] Bet Calculator\n[4] Quit\n")

    # list of valid inputs for each of the three options
    cbs_options = ["create bet space", "create", "1", "one"]
    vbs_options = ["visit bet space", "visit", "2", "two"]
    bet_options = ["3", "three", "bet", "bet calculator", "calculator", "calc"]
    quit_options = ["quit", "4", "four", "leave", "exit"]

    # forever loop prompts user input for the options, handles each option and repeats prompt on invalid input
    while True:
        # user input for the main menu option
        selected_main_option = input("")

        if selected_main_option in cbs_options:
            create_bet_space_menu()
        elif selected_main_option in vbs_options:
            visit_bet_space_menu()
        elif selected_main_option in bet_options:
            bet_calculator_menu()
        elif selected_main_option in quit_options:
            print("\nGoodbye.")
            quit()
        else:
            print("\nThat is not a valid option. Please try again.")
            print("\n[1] Create Bet Space\n[2] Visit Bet Spaces\n[3] Bet Calculator\n[4] Quit\n")
    
# function for entering the cbs menu and handling
def create_bet_space_menu():
    # ask for bet space name, or let user exit 
    print('\nWhat would you like your Bet Space to be named?\n\u001b[90m(type "exit" to leave)\u001b[0m')

# function for entering the vbs menu and handling
def visit_bet_space_menu():
    print("\n")

# function for bet calculator
def bet_calculator_menu():
    # 
    print("\nBET CALCULATORS\nSelect one of the following options:")
    print("\n[1] Betting Odds Calculator\n[2] Arbitrage Calculator\n[3] Exit\n")

    # list of valid inputs for each of the three options
    boc_options = ["betting odds calculator", "betting odds", "betting", "bet", "1", "one"]
    ac_options = ["arbitrage calculator", "arbitrage", "arb", "2", "two"]
    quit_options = ["quit", "3", "three", "leave", "exit"]
    # forever loop prompts user input for the options, handles each option and repeats prompt on invalid input
    while True:
        # user input for the calculator options
        selected_calc_option = input("")

        # handling user input for respective calculators
        if selected_calc_option in boc_options:
            betting_odds_calculator_menu()
        elif selected_calc_option in ac_options:
            arbitrage_calculator_menu()
        elif selected_calc_option in quit_options:
            # displays main menu options before ending function call and going back to main menu loop 
            print("\n[1] Create Bet Space\n[2] Visit Bet Spaces\n[3] Bet Calculators\n[4] Quit\n")
            return
        else:
            print("\nThat is not a valid option. Please try again.")
            print("\n[1] Betting Odds Calculator\n[2] Arbitrage Calculator\n[3] Exit\n")

# function for entering the betting odds calculator 
def betting_odds_calculator_menu():
    # declaring the initial odds, odds type, stake, and default enabling the odds loop
    odds = 0.0
    stake = 0.0
    odds_type = "decimal"
    odds_loop = True

    # confirm type of odds
    print("\nPlease enter the type of odds ('american' or 'decimal'):")
    while odds_loop:
        try:
            odds_type = input("\u001b[90m> \u001b[0m")
        except: pass
        # stopping the odds loop if type is either american or decimal
        if odds_type == "american":
            odds_loop = False 
        elif odds_type == 'decimal':
            odds_loop = False
        else: print("\nInvalid type of odds (must be 'american' or 'decimal'). Please try again:\n")

    # enter odds
    print("\nPlease enter the odds:")
    while True:
        try:
            odds = float(input("\u001b[90m> \u001b[0m"))
        except: pass
        # validates the odds in the user-input list
        if (odds_type == "decimal" and odds > 1) or (odds_type == 'american' and (odds < -100 or 100 < odds)):
            # enter stake
            print("\nPlease enter the stake amount:")
            while True:
                try:
                    stake = float(input("\u001b[90m> \u001b[0m"))
                except: pass
                if stake > 0:
                    # convert odds to decimal if odds type is american
                    if odds_type == 'american':
                        odds = american_to_decimal(odds)

                    # create new betting odds calculator object with given odds, stake
                    new_bet = betting_odds_calculator.BettingOddsCalculator(odds, stake)
                    
                    # calculate payout and put it in dollar form
                    payout = new_bet.calculate_payout()
                    formatted_payout = "${:,.2f}".format(payout)

                    # print results
                    print("\nPayout: \u001b[32m" + formatted_payout + "\u001b[0m")

                    # shows main menu options before going back
                    print("\n[1] Betting Odds Calculator\n[2] Arbitrage Calculator\n[3] Exit\n")
                    return
                else:
                    print("\nInvalid stake (must be a float greater than 0 with no dollar sign). Please try again:\n")
        else:
            if odds_type == "decimal":
                print("\nInvalid odds (decimal odds must be greater than 1). Please try again:\n")
            elif odds_type == "american":
                print("\nInvalid odds (american odds must be greater than 100 or less than -100). Please try again:\n")

# converts american odds to decimal odds
def american_to_decimal(odds):
    if odds >= 0:
        decimal_odds = 1 + (odds / 100)
    else:
        decimal_odds = 1 + (100 / abs(odds))
    return decimal_odds

# takes a list and returns new list in dollar form
def format_list_to_dollar(list):
    formatted_list = []
    for num in list:
        formatted_list.append("${:,.2f}".format(num))
    return formatted_list

# lets user figure out arbitrage information based on their bets with any set of odds and stake 
def arbitrage_calculator_menu():
    # declaring local variables
    stake = 0
    odds_list = []
    float_odds_list = []
    odds_type = "decimal"
    odds_type_loop = True
    stake_loop = True

    # confirm type of odds
    print("\nPlease enter the type of all odds ('american' or 'decimal'):")
    while odds_type_loop:
        try:
            odds_type = input("\u001b[90m> \u001b[0m")
        except: pass
        if odds_type == "american" or odds_type == 'a':
            odds_type = "american"
            odds_type_loop = False
        elif odds_type == 'decimal' or odds_type == 'd':
            odds_type = "decimal"
            odds_type_loop = False
        else: print("\nInvalid type of odds (must be 'american' or 'decimal'). Please try again:")

    # confirm stake
    print("\nPlease enter the stake:")
    while stake_loop:
        tried_stake = -1
        try:
            tried_stake = float(input("\u001b[90m> \u001b[0m"))
        except: pass
        if tried_stake > 0:
            stake = tried_stake
            stake_loop = False
        else: print("\nInvalid stake (must be greater than 0). Please try again:")

    # calculate arbitrage
    print("\nPlease enter the odds in a comma-separated list (e.g. 2.5, 3.2, ...)")
    while True:
        try:
            odds_string = input("\u001b[90m> \u001b[0m")
        except: pass
        # convert string to list
        odds_list = odds_string.split(", ")
        if len(odds_list) == 1:
            print(f"\nSet must contain at least 2 odds.")
        # validate each element of the list before proceeding
        num_of_odds = 0
        for odd in odds_list:
            try:
                odd_float = float(odd)
                if (odds_type == "decimal" and odd_float > 1) or (odds_type == 'american' and (odd_float < -100 or 100 < odd_float)):
                    num_of_odds += 1
                    float_odds_list.append(odd_float)
                    if num_of_odds > 1:
                        if num_of_odds == len(odds_list): # if all elements (odds) valid
                            # convert to decimal if american
                            if odds_type == "american":
                                for i in range(len(float_odds_list)):
                                    float_odds_list[i] = american_to_decimal(float_odds_list[i])
                            # create new calculator and calculated variables
                            arb_calc = arbitrage_calculator.ArbitrageCalculator(stake, float_odds_list)
                            
                            # perform the calculations on variables
                            total_implied_probability = arb_calc.calc_total_implied_probability()
                            hedged_stakes = arb_calc.calculate_hedged_stakes()
                            payout = arb_calc.calculate_payout()
                            pnl = arb_calc.calculate_pnl()
                            roi = arb_calc.calculate_roi()

                            # variable for whether arbitrage opportunity or not
                            is_arbitrage = "\u001b[31m(not an arbitrage opportunity)\u001b[0m" # default message
                            if total_implied_probability < 1:
                                is_arbitrage = "\u001b[32m(arbitrage opportunity)\u001b[0m"

                            # display formatted arb results
                            formatted_total_implied_probability = "{:.2%}".format(total_implied_probability)
                            # TODO: ADD FORMATTING HERE FOR HEDGED STAKES
                            formatted_payout = "${:.2f}".format(payout)
                            formatted_pnl = "${:.2f}".format(pnl)
                            formatted_roi = "{:.2%}".format(roi)
                            

                            print("\nTotal Implied Probability:", formatted_total_implied_probability, is_arbitrage)
                            print("Respective Hedged Stakes:", hedged_stakes) # TODO: REPLACE WITH FORMATTED HEDGED STAKES
                            print("Payout:", formatted_payout)
                            if pnl > 0:
                                print("PNL:\u001b[32m", formatted_pnl, "\u001b[0m")
                            elif pnl < 0:
                                print("PNL:\u001b[31m", formatted_pnl, "\u001b[0m")
                            else:
                                print("PNL:", formatted_pnl)
                            print("ROI:", formatted_roi)

                            # # display formatted arb results
                            # print(f"Arbitrage percentage: {arb_percentage:.2f}%")
                            # print(f"Implied probabilities: {implied_probabilities}")

                            # shows main menu options before going back
                            print("\n[1] Betting Odds Calculator\n[2] Arbitrage Calculator\n[3] Exit\n")
                            return
                else:
                    print(f"\nInvalid set of odds. Must be a valid {odds_type} odd and comma-separated in the list.")
                    if odds_type == 'american':
                        print("(e.g. 300, 340, -140)\n")
                    if odds_type == 'decimal':
                        print("(e.g. 1.2, 1.63, 3.5)\n")
                    break  
            except ValueError:
                print(f"\nInvalid odd value: {odd}. Must be a valid {odds_type} odd and comma-separated in the list.")
                if odds_type == 'american':
                    print("(e.g. 300, 340, -140)\n")
                if odds_type == 'decimal':
                    print("(e.g. 1.2, 1.63, 3.5)\n")
                break

# starts program
run()
