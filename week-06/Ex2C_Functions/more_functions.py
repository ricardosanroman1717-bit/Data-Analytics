def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(f"{city}, {state} {zip}")


def add_numbers(*numbers):
    result = sum(numbers)
    expression = " + ".join(str(number) for number in numbers)
    print(f"{expression} = {result}")


def display_receipt(total_due, amount_paid):
    change_due = max(amount_paid - total_due, 0)
    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")
    print(f"Change Due: ${change_due:.2f}")
    if amount_paid < total_due:
        print(f"Remaining Balance: ${total_due - amount_paid:.2f}")


display_mailing_label("Ricardo", "123 Example Street", "Sample City", "DE", "00000")
print()
display_mailing_label("Alex Rivera", "456 Sample Avenue", "Example Town", "PA", "11111")
print()
add_numbers(8)
add_numbers(8, 12)
add_numbers(2, 4, 6, 8)
print()
display_receipt(25.00, 30.00)
print()
display_receipt(25.00, 25.00)
print()
display_receipt(25.00, 20.00)
