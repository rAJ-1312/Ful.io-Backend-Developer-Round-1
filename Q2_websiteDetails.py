import requests
from bs4 import BeautifulSoup
import re

def social_links(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    social_links = []

    
    social_media_patterns = {
        "facebook": r".*facebook\.com.*",
        "linkedin": r".*linkedin\.com.*",
        "twitter": r".*twitter\.com.*",
        "instagram": r".*instagram\.com.*"
    }

    for a_tag in soup.find_all('a', href=True):
        for platform, pattern in social_media_patterns.items():
            if re.match(pattern, a_tag['href'], re.IGNORECASE):
                social_links.append(a_tag['href'])
                break

    social_links = [link if link.startswith("http") else f"{base_url}{link}" for link in social_links]
    return social_links

def email_contacts(html_content):
    
    email_pattern = r'mailto:[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}'
    email_addresses = re.findall(email_pattern, html_content)

    phone_pattern = r'tel:(?:\d{10}|(?:\d{3}-){2}\d{4}|\(\d{3}\)\d{3}-\d{4}|\(\d{3}\)-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4}|\d{3} \d{3} \d{4}|\+\d{11,13}|\+1\s\d{3}\.\d{3}\.\d{4}|\+1\s\d{3}\s\d{3}\s\d{4}|\+\d{3}-\d{3}-\d{4}|1-\d{3}-\d{3}-\d{4})'
    phone_numbers = re.findall(phone_pattern, html_content)

    return email_addresses, phone_numbers



website_url = input("Enter the website URL: ")
base_url = "/".join(website_url.split("/")[:-1]) + "/"

print(base_url)


response = requests.get(base_url)
html_content = response.text



social_links = social_links(html_content, base_url)
email_addresses, phone_numbers = email_contacts(html_content)



print("Social Links:")
for link in social_links:
    print(link)

print("\nEmail Addresses:")
for email in email_addresses:
    print(email[7:])

print("\nPhone Numbers:")
for phone in phone_numbers:
    print(phone[4:])
