# Temel imaj olarak Ubuntu kullan
FROM ubuntu:latest

# Çalışma dizinini ayarla
WORKDIR /app/src

# Gereken dosyaları çalışma dizinine kopyala
COPY src /app/src

# Python ve gerekli paketleri kur
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Uygulamayı çalıştır
CMD ["python3", "main.py"]
