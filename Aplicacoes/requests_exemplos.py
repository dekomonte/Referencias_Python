# Requests is an elegant and simple HTTP library for Python, built for human beings.
import requests

#==========Exemplo - PokeAPI==========
r = requests.get('https://pokeapi.co/api/v2/pokemon/')

# print('Status Code: ',r.status_code)
# print('Headers: ',r.headers['content-type'])
# print('Enconding: ',r.encoding)
# print('text: ',r.text)
# print('json: ',r.json())

#==========Exemplo - Requests DOC==========
print('General')
r = requests.get('https://api.github.com/events')
print(r)
print('Status Code: ',r.status_code)
print('Headers: ',r.headers['content-type'])
print('Enconding: ',r.encoding)
# print('text: ',r.text)
# print('json: ',r.json())

#HTTP request
print('HTTP request')

r = requests.get('https://httpbin.org/get') #https://httpbin.org/
print('get: ',r)

r = requests.post('https://httpbin.org/post') 
print('post: ',r)

r = requests.delete('https://httpbin.org/delete')
print('delete: ',r)

r = requests.patch('https://httpbin.org/patch')
print('patch: ',r)

r = requests.put('https://httpbin.org/put')
print('put: ',r)

