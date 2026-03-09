import art
print(art.logo)
def find_highest_bidder(record_highest_bidder):
    highest_bidder = 0
    winner=""
    for bids in record_highest_bidder:
        bidding_amount=record_highest_bidder[bids]
        if bidding_amount > highest_bidder:
            highest_bidder=bidding_amount
            winner=bids
    print(f"The Winner is {winner} with the highest bidding amount {highest_bidder}")
    print(record_highest_bidder)
bidders={}
continue_bids = True
while continue_bids:
    name = input("What is your name?:").lower()
    bid = int(input("What is your bid?:"))
    bidders[name] = bid
    want_continue=input("Whether there are more bidders type y for yes and n for no:").lower()
    if want_continue == "n":
        print("\n"*20)
        continue_bids=False
        find_highest_bidder(bidders)
    else :
        continue_bids=True
        print("\n"*20)
