## Projeto docker/ python /redis
Repositório para código de uma aplicação python que roda dentro de um contanier python consultando um banco de dados redis  
Objetivo do projeto: entender como uma aplicação roda dentro de um contaniner acessando um banco de dados. Essa versão utiliza um dockfile para o build
do projeto

1) Criação de uma rede no docker:  
docker network create --driver  bridge minha-bridge

2) Criação do volume 
docker volume create meu-volume 
Os arquivos ficam dentro de /var/lib/docker/volumes/meu-volume

3) Baixar o container redis  
docker pull redis

4) Subir o redis(mapear o volume para uma pasta)  
docker run -p 6379:6379 -v meu-volume:/app  --network minha-bridge --name container-redis -d redis

5) Inserir um registro no redis  
No DB0 inserir um registro do tipo string com  a chave valores e algum valor

6) Construir gerar o build do projeto  
docker build -t docker_python_redis . --network minha-bridge

7) Subir aplicação para teste  
docker run  --network minha-bridge docker_python_redis


### Comandos mais utilizados  
- docker --version  -- lstar a versão do docker
- docker ps -- listar todos os container
- docker images ls -- listar todas as images
- docker images  -- listar todas as imagens
- docker network ls 
- docker inspect id-container
- docker rm $(docker ps -a -q) -- limpar todos os contanier
- docker rmi -f  $(docker images -aq) -- limpar todas as imagens
- docker stop conntainer-id  -- stop no container
