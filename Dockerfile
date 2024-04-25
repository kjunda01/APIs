# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9.7-alpine

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

COPY entrypoint.sh /app/entrypoint.sh

# Change permissions of the working directory to 777
RUN chmod -R 777 /app

# Define o script de entrada como o ponto de entrada do contêiner
ENTRYPOINT ["/app/entrypoint.sh"]