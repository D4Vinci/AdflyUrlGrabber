#Author:D4Vinci
import base64 ,urllib2

def crack(code):
    zeros = ''
    ones = ''
    for n,letter in enumerate(code):
        if n%2 == 0:
            zeros += code[n]
        else:
            ones =code[n] + ones
    key = zeros + ones
    key = base64.b64decode(key.encode("utf-8"))
    return key[2:]

print " - - AdflyUrlGrabber - - By D4Vinci"
url = raw_input("\n Adfly url : ")
if "http" not in url:
    url = "http://"+url
print " [+] Grabbing the url Source . . ."
adfly_data = urllib2.urlopen(url).read()
print " [+] Searching for url code . . ."
ysmm = adfly_data.split("ysmm = \'")[1].split("\';")[0]
print " [+] Cracking the encryption . . ."
print "\n ### The Final Url Is : "+crack(ysmm)
