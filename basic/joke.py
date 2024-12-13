user_input = (str(input("what do you want:")))
def making_joke ():
    if user_input.lower() == "joke":
        print(" Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk,\n and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer\n asks why and Sophia replies: 'because they had eggs'")
    else:
        print("sorry i can only show you joke")
making_joke()