from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids = {}
bid_finished = True


def highest(bidder_record):
    highestbid = 0
    winner = ""
    for bidder in bidder_record:
        bid_amount = bidder_record[bidder]
        if bid_amount > highestbid:
            highestbid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highestbid}")


while bid_finished:
    name = input("What is the bidder name?\n")
    bid = int(input("What is the bid amount?\n"))
    bids[name] = bid
    should_continue = input("Is there any bid (yes/no)\n")
    if should_continue == "yes":
        clear()
    else:
        bid_finished = False
        highest(bids)