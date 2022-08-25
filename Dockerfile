FROM registry.tools.havan.com.br/hvn-devops/python:3.6.10
ENV SERVER_HOST='0.0.0.0'
ENV SERVER_PORT='5000'
ENV TZ=America/Sao_Paulo
EXPOSE 5000
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
