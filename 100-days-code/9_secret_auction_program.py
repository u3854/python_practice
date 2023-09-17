import os
from secret_auction_art import logo

print(logo)
print('Welcome to the secret auction program. ')

# FUNCTION TO INPUT BIDDER NAMES AND THEIR RESPECTIE BIDS, RETURNS INFO AS A DICTIONARY
def bid_process(bidders):

    name = input('What is your name?: ')
    bid_amount = float(input('What\'s your bid?: $'))
    bidders[name] = bid_amount      # ADDING ENTRY TO DICT

    more_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n").strip().lower()
    os.system('cls' if os.name == 'nt' else 'clear') # CLEAR SCREEN

    if more_bid == "yes":
        return bid_process(bidders)     # RE_RUN FUNCTION AND TAKE ANOTHER ENTRY TO DICT
    else:
        return bidders      # RETURNING DICT WITH INFO OF ALL BIDDERS

# FUNCTION TO GET HIGHEST BIDDER AND BID AS A TUPLE
def sort_bids(bid_info):

    sorted_bids = sorted(bid_info.items(), key=lambda x:x[1], reverse=True)     # SORTING DICT ACCORDING TO VALUES (BIDS)

    # CHECKING FOR TIES
    if len(sorted_bids) > 1:
        if sorted_bids[0][1] == sorted_bids[1][1]:
            response = input("At least two bids have tied for the highest bid. Would you like to go for another round? Type 'yes' or 'no'\n")
            if response.lower() == 'yes':
                os.system('cls' if os.name == 'nt' else 'clear') # CLEAR SCREEN
                print(logo)
                print('Welcome to the secret auction program. ') # SHOWING STARTING SCREEN AGAIN FOR ANOTHER ROUND OF BIDS
                return sort_bids(bid_process({}))
            else:
                return (0,0)    # NO CLEAR WINNER OF BID
    else:
        return sorted_bids[0]   # TUPLE CONTAINING NAME AND BID OF HIGHEST BIDDER

highest_bidder, highest_bid = sort_bids(bid_process({}))    # TUPLE UNPACKING
os.system('cls' if os.name == 'nt' else 'clear') # CLEAR SCREEN

if highest_bid > 0:         # HIGHEST BID = 0 IMPLIES NO WINNER
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")