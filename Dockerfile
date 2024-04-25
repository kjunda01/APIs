FROM python:3.7.3-stretch

# Set unbuffered output for python
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Bundle app source
COPY . .

# Expose port
EXPOSE 8000

# Run migrations and start the server
CMD python3 manage.py makemigrations && \
    python3 manage.py migrate && \
    python3 manage.py runserver 0.0.0.0:8000
