import requests
import hashlib
import sys


# hashes the password using sha1
# sends the proper query string to the request_api_data function
# sends the data received to the get_password_leaks_count function
# returns the count
def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


# uses the API to send a query and returns the response
# uses K anonymity encryption to keep password secure
def request_api_data(query_string):
    url = 'https://api.pwnedpasswords.com/range/' + query_string
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {response.status_code}, check the API and try again')
    return response


# parses the data by line and compares the tail sent by pwned_api_check
# if there is a match, it returns the count; otherwise returns 0
def get_password_leaks_count(hashes, my_hash):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == my_hash:
            return count
    return 0


def main(args):
    password_found_dict = {}  # mapping leaked_password: times_found
    safe_passwords = []
    for password in args:
        count = pwned_api_check(password)
        if count:
            password_found_dict[password] = count
        else:
            safe_passwords.append(password)

    if password_found_dict:
        print('PASSWORDS THAT WERE LEAKED:\n')
        for k, v in password_found_dict.items():
            print(f'Password "{k}" was leaked {v} times')
        print('\n')

    if safe_passwords:
        print('SAFE PASSWORDS:\n')
        for password in safe_passwords:
            print(password)
        print('\n')

    return 'All done!\n'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
