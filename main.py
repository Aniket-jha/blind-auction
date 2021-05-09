from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

bid_dictionary={}
adding=True
winner=""
def highest_bidder(bidding_records) :
  highest_bid=0
  for record in bidding_records :
    bid_amount= bidding_records[record]
    if bid_amount > highest_bid :
      highest_bid=bid_amount
      winner= record
  print(f"Winner is {winner}, bid is ${bid}")


while adding :
  name=input("What is your name: \n")
  bid=int(input("What is your bid:\n $"))
  bid_dictionary[name]=bid
  continue_working = input("Is there anyone else Say 'yes' if there 'no' if not there: \n")
  if continue_working == "yes" :
    clear()
    
  else : 
    adding = False
    highest_bidder(bid_dictionary)





