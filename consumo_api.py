import requests

print('***** Usuários do GitHub *****')

username = input('Qual é o nome do usuário? ')
print(username)
url = f'https://api.github.com/users/{username}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f'Nome completo: {data["name"]}')
    print(f'Localização: {data["location"]}')
    print(f'Seguidores: {data["followers"]}')
    print(f'Seguindo: {data["following"]}')
    print(f'Biografia   : {data["bio"]}')
elif response.status_code == 404:
    print('Usuário não encontrado')
else:
    print('Não é possével encontrar o usuário') 
    
status = response.status_code

print(f'\nStatus da execução:{status}')