# Define a imagem base usando a versão oficial do Python
FROM python:3.11

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório atual dentro do container
COPY ./requirements.txt /app/requirements.txt

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do seu código da aplicação para o diretório de trabalho
COPY . /app

# Comando para executar sua aplicação, ajuste conforme necessário
CMD ["python", "app.py"]
