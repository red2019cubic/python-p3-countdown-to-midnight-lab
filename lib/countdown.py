# your code goes here!
import time

def countdown(num):
    while num >= 0:
        
        if num > 0:
            print(f"{num} SECOND(S)!")
            
        elif num == 0:
            print("HAPPY NEW YEAR!")
            break
        num -= 1
def countdown_with_sleep(num):
    while num >= 0:
        
        if num == 0:
            print("HAPPY NEW YEAR!")
            break
        elif num > 0 :
            print(f"{num} SECOND(S)!")
            time.sleep(1)
        num -= 1
        
    
# countdown(5)
countdown_with_sleep(5)