print("Welcome to quiz game in computer")
playing=input("Do you want play? ")
if playing.lower() !="yes":
    quit()
else:
    print(" Okay Let's play the quiz :)")
score=0
answer=input("1.what does CPU stand for? " )
if answer.lower() =="central processing unit":
    score+=1 
    print("correct!")
else:
    print("Incorrect!")

answer=input("2.who was creator in python? ")
if answer.lower() =="guiddo van roosum":
    score+=1
    print("correct!")
else:
    print("Incorrect!")

answer=input("3.what does GPU stand for? ")
if answer.lower() =="graphics processing unit":
    score+=1
    print("correct!")
else:
    print("Incorrect!")
    
answer=input("4.what does RAM stand for? ")
if answer.lower() =="random access memory":
    score+=1
    print("correct!")
else:
    print("Incorrect!")
    
answer=input("5.what does PSU stand for? ")
if answer.lower() =="power supply" :
    score+=1
    print("correct!")
else:
    print("Incorrect!")
    
print("You got"+ str(score)  + "question correct!")
print("You got"+str((score/5)*100)+"%.")

    
             
