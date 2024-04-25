# API CRUD Django + PostgreSQL

Este projeto consiste em uma API CRUD desenvolvida em Django com banco de dados PostgreSQL.


## Comandos para iniciar

1. Inicie os contêineres Docker:
   
`docker compose up -d`

2. Para gerar usuários de teste, execute o script `gerar_usuarios.py` em um novo terminal:

`sudo apt install python3-pip`

`sudo apt install faker`

`python3 gerar_usuarios.py`



## Endpoints da API

- **Visualizar todos os usuários na web:**
- URL: http://127.0.0.1/api/users/

---

- **Métodos da API:**

- **GET para listar todos os usuários:**
 - URL: [http://127.0.0.1/api/users/]

- **GET para visualizar dados de um usuário específico:**
 - URL: [http://127.0.0.1:8000/users/read/ID]
   
- **POST para criar um novo usuário:**
 - URL: [http://127.0.0.1:8000/users/create]
 - Parâmetros: dados do usuário em formato raw no corpo da requisição

- **PUT para atualizar os dados de um usuário:**
 - URL: [http://127.0.0.1/users/update/ID]
 - Parâmetros: dados atualizados do usuário em formato raw no corpo da requisição

- **DELETE para excluir um usuário:**
 - URL: [http://127.0.0.1/users/delete/ID]

