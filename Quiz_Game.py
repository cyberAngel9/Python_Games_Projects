print("Welcome to my compter quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play:)")
score = 0
answer = input("What does APT stand for? ")
if answer.lower() == "advanced persistent threat": 
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does MTBF stand for? ")
if answer.lower() == "mean time between failures": 
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does IoT stand for? ")
if answer.lower() == "internet of things": 
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does IP stand for? ")
if answer.lower() == "internet protocol": 
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
