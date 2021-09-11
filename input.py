import time
import random
wordCount =1 
t=3

def countdown(t):
    while t:
        mins, sec = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,sec)
        print(timer, end="\r")
        time.sleep(1)
        t-=1
    

print(type(wordCount))
ready = input("""Welcome to the word guessing game. 
      You will get 3 secconds to guess how many words are in a random phrase!
      If you guess how many correctly you win a PRIZE!
      If ready type "yes": 
      """)

if(ready=="yes"):
    boom = ["I'm heading back to Colorado tomorrow after being down in Santa Barbara over the weekend for the festival there. I will be making October plans once there and will try to arrange so I'm back here for the birthday if possible. I'll let you know as soon as I know the doctor's appointment schedule and my flight plans.", "It was a scrape that he hardly noticed. Sure, there was a bit of blood but it was minor compared to most of the other cuts and bruises he acquired on his adventures. There was no way he could know that the rock that produced the cut had alien genetic material on it that was now racing through his bloodstream. He felt perfectly normal and continued his adventure with no knowledge of what was about to happen to him.", "I'm heading back to Colorado tomorrow after being down in Santa Barbara over the weekend for the festival there. I will be making October plans once there and will try to arrange so I'm back here for the birthday if possible. I'll let you know as soon as I know the doctor's appointment schedule and my flight plans.", "She asked the question even though she didn't really want to hear the answer. It was a no-win situation since she already knew. If he told the truth, she'd get confirmation of her worst fears. If he lied, she'd know that he wasn't who she thought he was which would be almost as bad. Yet she asked the question anyway and waited for his answer."]
    var = boom[random.randint(0,2)]
   
    
    for words in var:
        if(words == " "):
            wordCount = wordCount + 1
    
    print(var)
    print(wordCount)
    countdown(int(t))
    guess = input("Enter the word count you think it is: ")
    if(int(guess) == wordCount):
        print("Correct, you win $10,000!")
    else:
        print("Incorrect try again next time!")
else:
    print("Come back when you are ready!")        

##print(random.randint(0,2))


