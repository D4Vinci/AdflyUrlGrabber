# Contributor(s): nigella (@nig)

from base64 import b64decode
from urllib.request import urlopen
from sys import argv, exit

__author__ = 'D4Vinci'

def decrypt(code):
    ''' decrypt the given encrypted code '''

    zeros, ones = '', ''

    for num, letter in enumerate(code):
        if num % 2 == 0: zeros += code[num]
        else: ones = code[num] + ones

    key = zeros + ones
    key = b64decode(key.encode("utf-8"))

    return key[2:].decode('utf-8')


if __name__ == '__main__':
    ''' when script run directly '''

    try: url = argv[1]
    except: print('usage: python(3) AdflyURLGrabber.py <URL>'); exit()

    if "http" not in url: url = "http://" + url

    adfly_data = urlopen(url).read()
    ysmm = adfly_data.split(b"ysmm = '")[1].split(b"';")[0] # Find encrypted URL code in URL source

    decrypted_url = decrypt(ysmm.decode('utf-8')) # Decrypt the URL

    print(decrypted_url)
