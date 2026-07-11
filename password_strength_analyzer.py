import string
import random
print("=========================")
print("PASSWORD STRENGTH ANALYZER")
print("=========================") 

password=input("Enter your password:")

length= len(password)

has_upper=False
has_lower=False
has_digits=False
has_special=False



for char in password:
    if char.isupper():
        has_upper=True

    if char.islower():
        has_lower=True

    if char.isdigit():
        has_digits=True

    if char in string.punctuation:
            has_special=True

    print("uppercase:", has_upper)
    print("lowercase:", has_lower)
    print("digits:", has_digits)
    print("special characters:", has_special)

if not has_upper:
    print(" Add at least one uppercase letter.")

if not has_lower:
    print(" Add at least one lowercase letter.")

if not has_digits:
    print(" Add at least one number.")

if not has_special:
    print(" Add at least one special character.")

if length < 8:
    print("Password should be at least 8 characters long.")

if " " in password:
    print("⚠ Password should not contain spaces.")

common_passwords=[
    "123456","password","password123","123456789","qwerty","abc123","111111","12345678","password1","12345","admin","letmein","welcome","monkey","login","abc123456","starwars","dragon","passw0rd","master","abcdef"
    ]
if password.lower() in common_passwords:
    print(" This is a very common password.")

characters = string.ascii_letters + string.digits + string.punctuation

strong_password = ""

for i in range(12):
    strong_password += random.choice(characters)

print("Suggested Strong Password:", strong_password)

score=0

if length>=8:
        score+=1
if has_upper:
        score+=1 
if has_lower:
        score+=1
if has_digits:
        score+=1
if has_special:
        score+=1

        print("score:", score,"/5")

if score<=2:
        print("your password is weak")  
elif score<=4:
        print("your password is medium")
else:
        print("your password is strong:)")

print("Password Received Successfully!")