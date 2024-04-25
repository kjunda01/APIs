FROM python:3.7.3-stretch

# Set unbuffered output for python
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Bundle app source
COPY . .

# Expose port
EXPOSE 8000

# Run migrations
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

# Set a default environment variable for Django to use
ENV DJANGO_HOST=0.0.0.0

# Command to run Django with dynamic IP
CMD ["python3", "manage.py", "runserver", "$DJANGO_HOST:8000"]
