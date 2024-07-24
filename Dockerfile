# Use the official Python base image with version tag
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy all codes to the container
COPY . .

# Uygulamayı çalıştır
CMD ["python3", "src/main.py"]
