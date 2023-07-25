print ("Welcome To My Computer Game ")

player = input("Are You Want To Play A Game ? ")
if player.lower() != "yes":
    quit()
    
print ("Okay let's go :) ")
score = 0

question = input("what is CPU stand for ? ")
if question == "Central Processing Unit":
    print("Correct")
    score +=1
else:
    print("Incorrect !")

question = input("what is GPU stand for ? ")
if question == "Graphics Processing Unit":
    print("Correct")
    score +=1
else:
    print("Incorrect !")

question = input("what is RAM stand for ? ")
if question == "Random access memory":
    print("Correct")
    score +=1
else:
    print("Incorrect !")

question = input("what is PSU stand for ? ")
if question == "Power supply":
    print("Correct")
    score +=1
else:
    print("Incorrect !")

print ("Yours Total Correct Answer is " + str(score) )
print ("Yours Total Correct Answer is " + str((score / 4 )* 100) )
