import re

def is_valid_contact_number(number):
    # Define regular expression patterns for different formats
    # patterns = [
    #     r'^\d{10}$',                            # 2124567890
    #     r'^\d{3}-\d{3}-\d{4}$',                # 212-456-7890
    #     r'^\(\d{3}\)\d{3}-\d{4}$',             # (212)456-7890
    #     r'^\(\d{3}\)-\d{3}-\d{4}$',            # (212)-456-7890
    #     r'^\d{3}\.\d{3}\.\d{4}$',              # 212.456.7890
    #     r'^\d{3} \d{3} \d{4}$',                # 212 456 7890
    #     r'^\+\d{11,13}$',                      # +12124567890
    #     r"\+1\s\d{3}\.\d{3}\.\d{4}$",          # +1 212.456.7890
    #     r"\+1\s\d{3}\s\d{3}\s\d{4}$",          # +1 212 456 7890
    #     r'^\+\d{3}-\d{3}-\d{4}$',              # +212-456-7890
    #     r'^1-\d{3}-\d{3}-\d{4}$'               # 1-212-456-7890
    # ]

    pattern = r'^(\d{10}|(\d{3}-){2}\d{4}|\(\d{3}\)\d{3}-\d{4}|\(\d{3}\)-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4}|\d{3} \d{3} \d{4}|\+\d{11,13}|\+1\s\d{3}\.\d{3}\.\d{4}|\+1\s\d{3}\s\d{3}\s\d{4}|\+\d{3}-\d{3}-\d{4}|1-\d{3}-\d{3}-\d{4})$'


    if re.match(pattern, number):
        return True
    else:
        return False


numbers = [
    '2124567890',
    '212-456-7890',
    '(212)456-7890',
    '(212)-456-7890',
    '212.456.7890',
    '212 456 7890',
    '+12124567890',
    '+1 212.456.7890',
    '+1 212 456 7890',
    '+212-456-7890',
    '1-212-456-7890'
]

for number in numbers:
    if is_valid_contact_number(number):
        print(f"{number} is a valid contact number.")
    else:
        print(f"{number} is an invalid contact number.")
