# Basic moneyline arbitrage bet finder program 
# calculates the discrepancies in odds across different bookmakers provided by user input and returns the arbitrage opportunities
# for more info on arbitrage betting: https://en.wikipedia.org/wiki/Arbitrage_betting

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
    boc_options = ["betting odds calculator", "betting odds", "betting", "bet" "1", "one"]
    ac_options = ["arbitrage calculator", "arbitrage", "arb", "2", "two"]
    quit_options = ["quit", "3", "three", "leave", "exit"]
    # forever loop prompts user input for the options, handles each option and repeats prompt on invalid input
    while True:
        # user input for the calculator options
        selected_calc_option = input("")

        # handling user input for respective calculators
        if selected_calc_option in boc_options:
            create_bet_space_menu()
        elif selected_calc_option in ac_options:
            visit_bet_space_menu()
        elif selected_calc_option in quit_options:
            # displays main menu options before ending function call and going back to main menu loop 
            print("\n[1] Create Bet Space\n[2] Visit Bet Spaces\n[3] Bet Calculators\n[4] Quit\n")
            return
        else:
            print("\nThat is not a valid option. Please try again.")
            print("\n[1] Create Bet Space\n[2] Visit Bet Spaces\n[3] Bet Calculators\n[4] Quit\n")
    

# starts program
run()
