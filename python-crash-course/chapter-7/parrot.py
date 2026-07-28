message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
first_name = input(prompt)
prompt = "What is your last name? "
last_name = input(prompt)
full_name = f"{first_name} {last_name}"
print(f"\nHello, {full_name.title()}!")

number = input("Enter a number, and I will tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")