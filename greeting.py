def greet(name):
    return f"Hello, {name}, How are you?"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    message = greet(user_name)
    print(message)