print("Welcome to a simple quiz game!")

playing = input("Do you want to this small python program? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does WWWW stand for for? ")
if answer.lower() == "world wide web":
    print('Thats Right!')
    score += 1
else:
    print("wRONG!!")

answer = input("How many days in a week? ")
if answer.lower() == "7":
    print('Thats Right!')
    score += 1
else:
    print("WRONG!,Really!!??")

answer = input("who played Luke Skywalker? ")
if answer.lower() == "Mark Hamill":
    print('Correct! , Yay!')
    score += 1
else:
    print("Incorrect!,Come on..")

answer = input("Where is san antonio located in ? ")
if answer.lower() == "Texas":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")