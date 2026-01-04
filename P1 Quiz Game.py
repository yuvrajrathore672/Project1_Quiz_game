print("Welcome To The Quiz Game")

start = input("Do You Want To Play? " )
print(start)

if start.lower() != "yes":
    print("We will play later !")
    quit()
    
else:
    print("Lets Play !!!")

score = 0

q1 = input("Ques 1 : What is capital of India? " )
if q1.lower() == "delhi":
    print("Correct Ans")
    score +=4
else:
    print("incorrect")
    score-=1

q2 = input("Ques 1 : Who is richest person of world? " )
if q2.lower() == "elon musk":
    print("Correct Ans")
    score +=4
else:
    print("incorrect")
    score-=1

q3 = input("Ques 3 : What is capital of Germany? " )
if q3.lower() == "berlin":
    print("Correct Ans")
    score +=4
else:
    print("incorrect")
    score-=1

q4 = input("Ques 4 : What we say mobile in german? " )
if q4.lower() == "handy":
    print("Correct Ans")
    score +=4
else:
    print("incorrect")
    score-=1


print("Your Final score is "+ str(score)+".")






