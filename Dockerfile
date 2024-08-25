FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# pip ve setuptools'u güncelliyoruz
RUN pip install --no-cache-dir --upgrade pip setuptools

# Gereken paketleri yüklüyoruz
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

# Uygulamayı uvicorn ile çalıştırıyoruz
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "80"]
