# docker_python_redis
Repositorio para codigo de uma aplicação python que roda dentro de um contanier python consultando um banco de dados redis
Objetivo do projeto: criar um código python que busca informações em um banco redis que estão dentro de um contaniner

1) Criação de uma rede no docker:
docker network create --driver  bridge minha-bridge

2) Baixar o container redis
docker pull redis

3) Subir o redis 
docker run -p 6379:6379 -v  /home/tiago/redis-dados  --network minha-bridge --name container-redis -d redis

4) Construir gerar o build do projeto
docker build -t hello_docker_python . --network minha-bridge

5) Subir aplicação para teste
docker run  --network minha-bridge hello_docker_python


-- Comandos mais utilizados
docker ps -- listar todos os container
docker images ls -- listar todas as images
docker network ls 

docker inspect id-container

-- limpar todos os contanier
docker rm $(docker ps -a -q)

-- limpar todas as imagens
docker rmi -f  $(docker images -aq)

