def border_decorator(func):
    def wrapper(message):
        border = '*' * (len(message) + 4)
        return f"{border}\n* {func(message)} *\n{border}"
    return wrapper

def emoji_decorator(func):
    def wrapper(message):
        return f"😎 {func(message)} 😎"
    return wrapper

def wave_pattern_decorator(func):
    def wrapper(message):
        wave = "~" * (len(message) + 6)
        return f"{wave}\n~~ {func(message)} ~~\n{wave}"
    return wrapper

def boxed_uppercase_decorator(func):
    def wrapper(message):
        upper_msg = func(message).upper()
        box_width = len(upper_msg) + 4
        top_bottom = '+' + '-' * (box_width - 2) + '+'
        middle = f"| {upper_msg} |"
        return f"{top_bottom}\n{middle}\n{top_bottom}"
    return wrapper

def rainbow_decorator(func):
    def wrapper(message):
        colors = ['🟥', '🟧', '🟨', '🟩', '🟦', '🟪']
        decorated = ''.join(colors[i % len(colors)] + ch for i, ch in enumerate(func(message)))
        return decorated
    return wrapper

# Base function
def get_message(msg):
    return msg

# Example Usage:

@border_decorator
@emoji_decorator
def decorated_message_1(msg):
    return get_message(msg)

@wave_pattern_decorator
@boxed_uppercase_decorator
def decorated_message_2(msg):
    return get_message(msg)

@rainbow_decorator
def decorated_message_3(msg):
    return get_message(msg)

if __name__ == "__main__":
    message = "Welcome to Python Decorators!"
    print(decorated_message_1(message))
    print()
    print(decorated_message_2(message))
    print()
    print(decorated_message_3(message))
