#script that uses a time module and the choice() function from the random module to return a random value
#The script will generate 6 integer values between 50 and 800.
import time
import random

currentime = time.localtime()
current_day = time.strftime("%A", currentime)
current_month = time.strftime("%B", currentime)
current_day1 = time.strftime("%d", currentime)
#for i in range(6):
    #value = random.randint(50, 80)
   # print(value)

winners= set(value for i in range(6) for value in [random.randint(50, 80)])

print(f"The lucky number for {current_day}, {current_month} {current_day1} are: {winners}.")
