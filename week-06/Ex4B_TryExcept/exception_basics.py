try:
    number = int("twelve")
except ValueError:
    print("ValueError: The text cannot be converted to an integer.")
else:
    print(number)
finally:
    print("Let's try another one...")

try:
    result = unknown_variable
except NameError:
    print("NameError: The variable was not defined.")
else:
    print(result)
finally:
    print("Let's try another one...")

try:
    result = "5" + 5
except TypeError:
    print("TypeError: A string and an integer cannot be added together.")
else:
    print(result)
finally:
    print("Let's try another one...")

try:
    result = compile("if True print('Hello')", "<example>", "exec")
except SyntaxError:
    print("SyntaxError: The statement is missing required punctuation.")
else:
    print(result)
finally:
    print("Let's try another one...")
