def check_password(pw):
    length = len(pw)
    upper = any(c.isupper() for c in pw)
    lower = any(c.islower() for c in pw)
    digit = any(c.isdigit() for c in pw)
    special = any(not c.isalnum() for c in pw)
    score = sum([upper, lower, digit, special])

    if length >= 12 and score == 4:
        return "Very Strong"
    elif length >=8 and score == 4:
        return "Strong"
    elif length >=6 and score >= 2:
        return "Medium"
    else:
        return "Weak"
		
import random
import string

def generate_password(length=8):
    if length < 12:
        length = 12
    
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)  ]
    
    chars = string.ascii_letters + string.digits + string.punctuation
    
    password += [random.choice(chars) for _ in range(length - 4)]
    
    random.shuffle(password)
    
    return "".join(password)

def save_password(pw):
	strength = check_password(pw)
	with open("password.txt", "a") as f:
		import datetime
		
		f.write(f"{datetime.datetime.now()} | password: {pw} | Strength: {strength}\n")
	
def view_passwords():
    try:
        with open("password.txt", "r") as f:
            print("\nSaved Passwords:")
            print(f.read())
    except:
        print("No passwords saved yet.")
        
        
while True:
    print("\n1. Generate Password")
    print("2. Check Password Strength")
    print("3. Save Password")
    print("4. View Saved Passwords")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        try:
        	length = int(input("Enter length: "))
        except:
        	print("invalid input")
        	continue	
        pw = generate_password(length)
        print("Generated:", pw)
        save = input("Save this password? (yes/no): ")
        if save.lower() == "yes":
        	save_password(pw)

    elif choice == "2":
        pw = input("Enter password: ")
        print("Strength:", check_password(pw))

    elif choice == "3":
        pw = input("Enter password to save: ")
        save_password(pw)
        print("Saved successfully!")

    elif choice == "4":
        view_passwords()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid input") 
        