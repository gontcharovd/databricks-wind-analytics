def fun_response(input_text):
    responses = {
        "cat": "Meow! Cats are purr-fect!",
        "dog": "Woof! Dogs are pawsome!",
        "pizza": "Yum! Who doesn't love pizza?",
        "python": "Slithering into some coding fun!",
        "space": "To infinity and beyond!"
    }
    return responses.get(input_text.lower(), "That's interesting! Tell me more!")

# Example usage
if __name__ == "__main__":
    user_input = input("Enter something fun: ")
    print(fun_response(user_input))