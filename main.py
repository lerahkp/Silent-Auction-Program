from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
other_bidders=True
bid_dict={}
while other_bidders:
  name=input("\nWhat is your name?: ")
  bid= int(input("What is your bid? $"))
  ot_bid = input("Are there any other bids?  Type 'yes' or 'no' ").lower()
  bid_dict[name]=bid
  if ot_bid=="yes":
    clear()
    other_bidders=True
  elif ot_bid=="no":
    for i in bid_dict:
      amount=(bid_dict[i])
      highest_bid=max(bid_dict,key=bid_dict.get)
      bid_values=bid_dict.values()
      max_bid_value = max(bid_values)
    print(f"The winner is {highest_bid} with a bid of {max_bid_value}")
    other_bidders=False
  else:
    print("There is an error")