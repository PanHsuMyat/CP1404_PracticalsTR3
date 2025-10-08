PASSWORD_LENGTH = 9

def main():
    """"Get and print password using functions."""
    user_password = get_password()
    print_asterisks(user_password)


def print_asterisks(user_password):
    """Print asterisks as the length of characters in password."""
    print("*" * user_password)


def get_password():
    """Get password meeting the required characters in password length."""
    user_password = len(input("Enter your password: "))
    while user_password <= PASSWORD_LENGTH:
        print("Invalid Password")
        user_password = len(input("Enter your password: "))
    return user_password

main()