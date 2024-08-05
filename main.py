import os
from art import logo
import keyboard
import time
cls=lambda:os.system('cls') #Clear function cls()



bids_data={}
max_bid=0
another_one=True
while another_one:
    
    name=input("What is your name?\n")
    bid=int(input("Your bid:\n$"))
    bids_data[name]=bid
    print('If there are any other bidders press "ENTER", otherwise press "ESC"')
    
    while True:
        time.sleep(0.5)
        hotkey=keyboard.read_key(suppress=True)
        
        
        if hotkey!='esc' and hotkey!='enter':
            time.sleep(0.5)
            hotkey=keyboard.read_key(suppress=True)
            
        elif hotkey=='esc':
            another_one=False
            
            cls()
            break
        elif hotkey=='enter':
            another_one=True
            
            cls()
            break
            
for bidder in bids_data:
    if bids_data[bidder]>max_bid:
        max_bid=bids_data[bidder]
        winner=bidder
        
print(logo)        
print(f'Winner of this auction is {winner} with ${max_bid}!!!')

    

    
    




