import redis
print("Ola eu sou Docker pytohn ")
r = redis.Redis(host='container-redis', port=6379, db=0)
print ((r.get('valores').decode('utf-8')))