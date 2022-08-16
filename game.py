print("hello welcome to game ")

playing = input("do you wanna play ? ")

if playing != "yes":
    quit()
    
    
    print("ok , lets play then :)")
    
    answer = input("what does cpu stand for? ")
    if answer == "central processing unit":
        print("correct")
    else:
        print("incorrect")