# API CRUD Django + PostgreSQL

Este projeto consiste em uma API CRUD desenvolvida em Django com banco de dados PostgreSQL.

## Comandos para iniciar

1. Construa os contêineres Docker:
   
`docker compose build`


3. Inicie os contêineres Docker:
   
`docker compose up -d`


5. Execute o os comandos para construir as tabelas no django:
   
`python3 manage.py makemigrations && python3 manage.py migrate`


7. Execute o servidor Django manualmente:
   
`python3 manage.py runserver`

Se estiver rodando em uma máquina virtual, rode com o ip da máquina, exemplo:
`python3 manage.py runserver 192.168.1.100:8000`


9. Para gerar usuários de teste, execute o script `gerar_usuarios.py` em um novo terminal:
    
`python3 gerar_usuarios.py`



11. Se preferir, rode tudo em apenas 1 comando:
`docker compose build && docker compose up -d && python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver`

## Endpoints da API

- **Visualizar todos os usuários na web:**
- URL: http://127.0.0.1:8000/users/

---

- **Métodos da API:**

- **GET para listar todos os usuários:**
 - URL: http://127.0.0.1:8000/users/

- **GET para visualizar dados de um usuário específico:**
 - URL: http://127.0.0.1:8000/users/read/ID

- **POST para criar um novo usuário:**
 - URL: http://127.0.0.1:8000/users/create
 - Parâmetros: dados do usuário em formato raw no corpo da requisição

- **PUT para atualizar os dados de um usuário:**
 - URL: http://127.0.0.1:8000/users/update/ID
 - Parâmetros: dados atualizados do usuário em formato raw no corpo da requisição

- **DELETE para excluir um usuário:**
 - URL: http://127.0.0.1:8000/users/delete/ID

