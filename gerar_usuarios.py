import requests
from faker import Faker
import random

fake = Faker('pt_BR')

def generate_fake_users(num_users):
    for _ in range(num_users):
        resolution = f'{random.randint(10, 250)}x{random.randint(10, 250)}'
        user_data = {
            'name': fake.name(),
            'email': fake.email(),
            'date_of_birth': fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat(),
            'cpf': fake.cpf(),
            'phone_number': fake.phone_number(),  # Gera número de telefone no formato brasileiro
            'profession': fake.job(),
            'profile_picture': f'https://dummyimage.com/{resolution}'
        }

        response = requests.post('http://127.0.0.1:8000/users/create', json=user_data)

        if response.status_code == 200:
            print('Usuário criado com sucesso!')
        else:
            print('Erro ao criar usuário:', response.status_code)

if __name__ == '__main__':
    num_users = int(input('Quantos usuários deseja criar? '))
    generate_fake_users(num_users)
