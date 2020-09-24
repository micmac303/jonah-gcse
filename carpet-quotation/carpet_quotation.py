# splash screen
splash_screen = '''
   ___                      _       ___
  / __\\__ _ _ __ _ __   ___| |_    / _ \\_ __(_) ___(_)_ __   __ _  
 / /  / _` | '__| '_ \\ / _ \\ __|  / /_)/ '__| |/ __| | '_ \\ / _` |
/ /__| (_| | |  | |_) |  __/ |_  / ___/| |  | | (__| | | | | (_| |
\\____/\\__,_|_|  | .__/ \\___|\\__| \\/    |_|  |_|\\___|_|_| |_|\\__, |
                |_|                                         |___/
                '''
print('\n' + splash_screen)


def input_valid_number(message: str, min: float, max: float) -> float:
    error_message = "Please enter a number between " + str(min) + " and " + str(max)
    valid = False
    while not valid:
        try:
            number = float(input(message))
            if min <= number <= max:
                valid = True
            else:
                print(error_message)
                print()
        except ValueError:
            print(error_message)
            print()

    return number


def offer(message: str) -> bool:
    default_discount = input(message)
    return default_discount == "yes" or default_discount == "y"


def apply_discount(price: float, discount: float) -> float:
    discount_amount = price * (discount / 100)
    new_price = price - discount_amount
    return new_price


def calculate_discount_price(price: float, discount: float) -> float:
    discount_amount = price * (discount / 100)
    print("The discount amounts to £" + str(discount_amount) + "\n")
    new_price = price - discount_amount
    print("The new total price is: £" + str(new_price))
    return new_price


def create_quote():
    # Enter details
    customer_name = input("Enter customer name: ")
    customer_location = input("Enter customer location: ")
    print()

    # Enter length - valid number (type and range)
    length = input_valid_number('Enter length in metres: ', 1, 1000)
    print("You entered a length of", length, "metres.\n")

    # Enter width - valid number (type and range)
    width = input_valid_number('Enter width in metres: ', 1, 1000)
    print("You entered a width of", width, "metres.\n")

    # Calculate area
    area = width * length
    print("The area is: ", area)

    # Ask for area deductions
    if offer("Are there any area deductions? "):
        # Enter area deduction - valid number (type and range)
        deduction_area = input_valid_number("Enter deduction area in square metres: ", 0, area - 1)
        print("You entered a deduction area of", deduction_area)
        # Apply area deduction
        area = area - deduction_area
        print("The area with the deduction applied is", area, "square metres.")

    print()

    # Enter price - valid number (type and range)
    carpet_price = input_valid_number("Enter price of selected carpet (per square metre) in pounds: £", 1, 1000)
    print("You entered a price of", carpet_price, "per square metre")
    print()

    # Calculate price
    price = area * carpet_price
    print("The price of the carpet is", "£{:,.2f}".format(price))

    # Offer default discount
    if offer("Would you like to apply the default discount? "):
        # Calculate discount
        price = apply_discount(price, 10)
        print("The price with th discount applied is", price)

    # Offer custom discount
    elif offer("Would you like to apply a custom discount up to 20%? "):
        print()
        # Ask for password !!!!!!
        if "Manager2016" == input("Please enter the password: "):
            # Enter discount - valid number (type and range)
            discount = input_valid_number("Please enter a discount percentage: ", 10, 20)
            # Apply discount
            price = apply_discount(price, discount)
            print("The price with the discount applied is", "£{:,.2f}".format(price))
        else:
            print("You entered an incorrect password! No discount will be applied.")

    # Display quotation details
    print('''
   ___           _        _   _               _     _        _ _    
  / _ \ _  _ ___| |_ __ _| |_(_)___ _ _    __| |___| |_ __ _(_) |___
 | (_) | || / _ \  _/ _` |  _| / _ \ ' \  / _` / -_)  _/ _` | | (_-<
  \__\\_\\\_,_\\___/\\__\\__,_|\\__|_\\___/_||_| \\__,_\___|\\__\\__,_|_|_/__/''')
    print()
    print("=====================================================================")
    print("Name:", customer_name.capitalize())
    print("Location:", customer_location.capitalize())
    print("The length is:", length)
    print("The width is:", width)
    print("The area is:", area)
    print("The price of carpet per square meter is:", "£{:,.2f}".format(carpet_price))
    print("The total price of your carpet is:", "£{:,.2f}".format(price))
    print("=====================================================================")
    print()


again = 'yes'
while again == 'yes' or again == 'y':
    create_quote()
    print('Do you want to create another quote? (yes or no)')
    again = input()

print("Thank you, good bye!")
