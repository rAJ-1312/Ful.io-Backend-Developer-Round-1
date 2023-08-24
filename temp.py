import re
import requests


url = "https://ful.io/"  


response = requests.get(url)
html_text = response.text


phone_pattern = r'tel:(?:\d{10}|(?:\d{3}-){2}\d{4}|\(\d{3}\)\d{3}-\d{4}|\(\d{3}\)-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4}|\d{3} \d{3} \d{4}|\+\d{11,13}|\+1\s\d{3}\.\d{3}\.\d{4}|\+1\s\d{3}\s\d{3}\s\d{4}|\+\d{3}-\d{3}-\d{4}|1-\d{3}-\d{3}-\d{4})'


matched_phone_numbers = re.findall(phone_pattern, html_text)



for phone_number in matched_phone_numbers:
    print("Matched Phone Number:", phone_number)


# Regular expression patterns for extracting email addresses and phone numbers
email_pattern = r'mailto:[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}'
# phone_pattern = r'tel:\+1\s\d{3}\s\d{3}\s\d{4}'

# Extract emails and phone numbers
emails = re.findall(email_pattern, html_text)
# phones = re.findall(phone_pattern, html_text)


for email in emails:
    print("Extracted Email : ", email[7:])
    
# for number in phones:
#     print("Extracted Number : ", number[4:])
