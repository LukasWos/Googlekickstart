#A company named Gooli has issued a new policy that their employees account
#passwords must contain:

#1. At least 7 characters.
#1. At least $7$ characters.
#2. At least one uppercase English alphabet letter.
#3. At least one lowercase English alphabet letter.
#4. At least one digit.

def is_valid_password(password):
    # Check if the password has at least 7 characters
    if len(password) < 7:
        return False
    # Check if the password has at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False
    # Check if the password has at least one lowercase letter
    if not any(char.islower() for char in password):
        return False
    # Check if the password has at least one digit
    if not any(char.isdigit() for char in password):
        return False
    # If all the conditions are met, return True
    return True

# Test the function with some examples
print(is_valid_password("Gooli123")) # True
print(is_valid_password("gooli123")) # False
print(is_valid_password("GOOLI123")) # False
print(is_valid_password("GooLi12")) # True
print(is_valid_password("GooLi")) # False