import requests
from faker import Faker
import random
import socket

fake = Faker('pt_BR')

# Obter o endereço IP da máquina
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  # Conecta a um servidor DNS público
    local_ip = s.getsockname()[0]
    s.close()
    return local_ip

# URL da API
API_URL = f'http://{get_local_ip()}/api/users/create'

def generate_phone_number():
    phone_number = f'({random.randint(10, 99)}) {random.randint(10000, 99999)}-{random.randint(1000, 9999)}'
    return phone_number

def generate_fake_users(num_users):
    for _ in range(num_users):
        resolution = f'{random.randint(10, 250)}x{random.randint(10, 250)}'
        user_data = {
            'name': fake.name(),
            'email': fake.email(),
            'date_of_birth': fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat(),
            'cpf': fake.cpf(),
            'phone_number': generate_phone_number(),
            'profession': fake.job(),
            'profile_picture': f'https://dummyimage.com/{resolution}'
        }

        response = requests.post(API_URL, json=user_data)

        if response.status_code == 200:
            print('Usuário criado com sucesso!')
        else:
            print('Erro ao criar usuário:', response.status_code)

if __name__ == '__main__':
    num_users = int(input('Quantos usuários deseja criar? '))
    generate_fake_users(num_users)
    