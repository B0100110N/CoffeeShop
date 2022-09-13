# coffee shop program :)

print("\n\n\nHello, welcome to Ben's Coffee House!")
name = (input("What is your name?\n"))
print("\nHello, " + name + ", thank you so much for coming in today!\n")

menu = "1. Dark Roast\n" "2. Medium Roast\n" "3. Light Roast"
print("Here is our menu:\n" + menu + "\n")
print("Which roast of coffee would you like today " + name + "?" + "\n")

order = input("\n")
print("Okay, and how many " + order + " coffee's will you have?\n")

#requesting an input from the user to see if coffee should be singular or plural. My first ifelse statement! <---
 
amount = input()
if int(amount) == 1:
    print("Okay. " + amount + " " + order + " coffee. Got it!")
elif int(amount) != 1:
    print("Okay. " + amount + " " + order + " coffee's. Got it!\n")

#end of Amnt request --->


size = "1. Small\n" "2. Medium\n" "3. Large"
print("Which size would you like? These are the sizes we offer:\n" + size + "\n")
SizeRequest = input("\n")
print("Okay. Can you confirm again how many " + SizeRequest + " " + order + " coffees you would like, please?")

#requesting another input from the user to see if plural or singular vocabulary is needed. Proud about this one! <---

SizeRequestAmount = input()
if int(SizeRequestAmount) == 1:
    print("Okay. " + SizeRequestAmount + " " + SizeRequest + ", " + order + " coffee. Would you like anything else?")
elif int(SizeRequestAmount) != 1:
    print("Okay. " + amount + " " + SizeRequest + ", " + order + " coffee's.\n")

#not finished here <---
AddToOrder = input("Would you like anything else?")
if AddToOrder == "yes":
    print("Okay, what else would you like?")
elif AddToOrder == "no":
    print("Okay!")

#end to unfished code --->

#end of SRA input request --->


response = input("\n")

price: int = 8
total = price * int(amount); dlr = "$"
print("That will be " + dlr + str(total) + "\n")
print("Will you be paying with cash or a card?\n")
CorC = input()
print(CorC + "," + " roger that!\n\n")
cash = "cash"; card = "card"; 

if CorC == "cash" and int(amount) == 1:
    print("Okay. I (the computer), will make you " + amount + " cup of our " + order + " coffee.\n\n")
elif CorC == "cash" and int(amount) != 1:
     print("Payment is processing...\n\n\nOkay, your payment has gone through successfully and I (the computer), will make you " + amount + " cups of our " + order + " coffee.\n\n") 
if CorC == "card" and int(amount) == 1: 
    print("Okay. I (the computer), will make you " + amount + " cup of our " + order + " coffee.\n\n")
elif CorC == "card" and int(amount) != 1:
    print("Payment is processing...\n\n\nOkay, your payment has gone through successfully and I (the computer), will make you " + amount + " cups of our " + order + " coffee.\n\n") 


#below is beginning on RandNum guess game <---

print("Now, to kill some time, can you guess the number I'm thinking of between 1 and 10?")
x = 5; num = "num"
while num != x:
    num = (int(input(f"Go on, guess a number between 1 and 10: ")))
    if int(num) < x:
        print("Sorry, " + name + "." + " I'm afraid that number is too low. Try again! ")
    elif int(num) > x:
        print("Sorry, " + name + "." + " I'm afraid that number is too high. Try again!")
    elif int(num) == x:
        print("Woah there, " + name + "!" + " Are you a psychic?\n")
        print("I'm only kidding, LOL. Only a nincompoop would have trouble finding a random number between 1 and 10. Nevertheless, this marks the end of our game.\n\n")

#end of RandNum guess game --->


print("Say... do you happen to have a 3D printer, because I can't actually make these coffee orders.\
" " You see, I'm just a computer, so the best thing I can do is have coffee delivered to you, show you where the nearest and best rated coffee shop is located, or reccomend the best coffee to buy online if you have a coffee maker. :)\n\n")
print("With that being said, I can only do that if Ben (my programmer) programms me to do so. :) :) :)\n\n")
print("Do you have a 3D printer?")
Ans = input()
if Ans == "yes":
    print("Cool. Please tell Ben (my programmer) to find a way to make that work!")
elif Ans != "yes":
    print("Well... now what?")

