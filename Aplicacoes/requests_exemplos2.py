import requests

#Persistencia de parametros por meio de requisicoes
s = requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')
print(r.text)

#Default data para o metodo de requisicoes
s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'login': 'exemplo'}) # both 'x-test' and 'x-test2' are sent
r = s.get('https://httpbin.org/headers', headers={'senha': 'exemplo2'})
print(r.text)
