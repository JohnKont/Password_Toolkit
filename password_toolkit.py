import random
import string

# ------------------ PASSWORD GENERATOR ------------------
def generate_password():
    length = int(input("Enter password length: "))
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))

    print(f"\nGenerated Password: {password}\n")


# ------------------ PASSWORD CHECKER ------------------
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include numbers")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Include special characters")

    return score, feedback


def run_password_checker():
    password = input("Enter password to check: ")
    score, feedback = check_password_strength(password)

    print(f"\nPassword Score: {score}/5")

    if score == 5:
        print("Strong password 💪")
    elif score >= 3:
        print("Moderate password ⚠️")
    else:
        print("Weak password ❌")

    if feedback:
        print("\nSuggestions:")
        for f in feedback:
            print(f"- {f}")
    print()


# ------------------ COMMON PASSWORD CHECK ------------------
def check_common_password(password):
    common_passwords = ["123456", "password", "qwerty", "abc123", "111111"]

    if password in common_passwords:
        print("\n⚠️ This is a very common and insecure password!\n")
    else:
        print("\n✅ This password is not in the common passwords list.\n")


def run_common_checker():
    password = input("Enter password to check: ")
    check_common_password(password)


# ------------------ MAIN MENU ------------------
def main():
    while True:
        print("=== Password Security Toolkit ===")
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Check Common Password")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            generate_password()
        elif choice == "2":
            run_password_checker()
        elif choice == "3":
            run_common_checker()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()