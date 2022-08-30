name = input("Type t is yur name: ")
print("Welcome", name, "to this test")

answer = input(
    "you awake to th sound of flutes,blaring wildy as if maniacs were calling you with a chaotic siren.do you stay asleep ir get up and investigate? ").lower()

if answer == "investigate":
    answer = input(
        "u get out of bed and see three small dark clad figures hiding in the corner,barely visible,do you talk to them?: ")

    if answer ==" yes":
        print("You black out as their voice drives yu insane.")
    elif answer == "no":
        print("You decide to run out of the room in fear but trip and faed to black.")
    else:
        print('since you didnt care about the 3 ghouls, they attack you and you black out.')

elif answer == "attack":
    answer = input(
        "You attack the 3 ghouls but yuo still black out and wake up in your bed again. ")

    

print("Thank you for trying", name)