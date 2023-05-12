# Basic moneyline arbitrage bet finder program 
# calculates the discrepancies in odds across different bookmakers provided by user input and returns the arbitrage opportunities
# for more info on arbitrage betting: https://en.wikipedia.org/wiki/Arbitrage_betting

first_run = True

# create a collection of bet spaces
# create a collection of bets 

# function to start program
def run():
    main_menu()



# function for displaying the first menu's options
def main_menu():
    # title which only appears the very first time the program is ran
    if first_run == True:
        print("\nARBITRAGE BOT\nSelect one of the following options:")
        first_run = False

    # display main menu options
    print("\n[1] Create Bet Space\n[2] Visit Bet Spaces\n[3] Quit\n")

    # list of valid inputs for each of the three options
    cbs_options = ["create bet space", "create", "1", "one"]
    vbs_options = ["visit bet space", "visit", "2", "two"]
    quit_options = ["quit", "3", "three", "leave", "exit"]

    # forever loop prompts user input for the options, handles each option and repeats prompt on invalid input 
    while True:
        # user input for the main menu option
        selected_main_option = input("")

        if selected_main_option in cbs_options:
            create_bet_space_menu()
        elif selected_main_option in vbs_options:
            visit_bet_space_menu()
        elif selected_main_option in quit_options:
            print("\nGoodbye.")
            quit()
        else:
            print("\nThat is not a valid option. Please try again.")
            print("\n[1] Create Bet Space\n[2] Visit Bet Spaces\n[3] Quit\n")
    

def create_bet_space_menu():
    print("\n")

# 
def visit_bet_space_menu():
    print("\n")

# starts program
run()
