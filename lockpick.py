import argparse
import requests
from bs4 import BeautifulSoup

banner = """
░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░  
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
Created by therealslimshady
https://github.com/therealslimshady0
https://x.com/dare4lslimshady
"""

def scan_forms(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    forms = soup.find_all('form')
    return forms

def get_form_details(form):
    details = {}
    details['action'] = form.get('action')
    details['method'] = form.get('method', 'post').lower()
    details['inputs'] = []

    for input_tag in form.find_all('input'):
        input_type = input_tag.get('type', 'text')
        input_name = input_tag.get('name')
        details['inputs'].append((input_type, input_name))

    return details

def bruteforce_form(url, form_details, data, verbose):
    if form_details['method'] == 'post':
        response = requests.post(url + form_details['action'], data=data)
    else:
        response = requests.get(url + form_details['action'], params=data)

    if verbose:
        print(f"Trying with data: {data}")
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text[:200]}")  # Print the first 200 characters of the response

    return response.ok, response

def main():
    print(banner)
    parser = argparse.ArgumentParser(description='Bruteforce a form on a webpage.')
    parser.add_argument('-u', '--url', required=True, type=str, help='The URL of the form to bruteforce')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    args = parser.parse_args()

    forms = scan_forms(args.url)

    if not forms:
        print('No forms found on the page.')
        return

    for i, form in enumerate(forms):
        print(f'Form {i+1}')
        form_details = get_form_details(form)
        print(f'Action: {form_details["action"]}')
        print(f'Method: {form_details["method"].upper()}')

        input_data = {}

        for input_type, input_name in form_details['inputs']:
            if input_name:
                user_input = input(f'Enter a value for {input_name} or a file path for multiple values: ')
                try:
                    with open(user_input, 'r', encoding='latin-1') as file:
                        input_data[input_name] = file.read().splitlines()
                except FileNotFoundError:
                    input_data[input_name] = [user_input]

        for values in zip(*input_data.values()):
            data = dict(zip(input_data.keys(), values))
            success, response = bruteforce_form(args.url, form_details, data, args.verbose)
            if success:
                print(f"Form submission successful with data: {data}")
                print(f"Response text: {response.text[:200]}")  # Print the first 200 characters of the response
                break
            else:
                print(f"Form submission failed with data: {data}")

if __name__ == '__main__':
    main()
