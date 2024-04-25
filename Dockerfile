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

# Copy django.sh script into the container
COPY django.sh /django.sh

# Grant execute permissions to the django.sh script
RUN chmod +x /django.sh

# Set the entrypoint
ENTRYPOINT ["/django.sh"]
