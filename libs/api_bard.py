from bardapi import BardCookies
import os
from dotenv import load_dotenv

load_dotenv()

cookie_dict = {
    "__Secure-1PAPISID" : os.environ.get('__Secure-1PAPISID', ''),
    "__Secure-1PSID": os.environ.get('__Secure-1PSID', ''),
    "__Secure-1PSIDCC": os.environ.get('__Secure-1PSIDCC', ''),
    "__Secure-1PSIDTS": os.environ.get('__Secure-1PSIDTS', ''),
}

bard = BardCookies(cookie_dict=cookie_dict)

def bard_get_answer(input):
    try:
        bard_output = bard.get_answer(input)['content']
        return bard_output
    except Exception as e:
        print(f'An error occurred while requesting an answer from Bard! Error: {e}')