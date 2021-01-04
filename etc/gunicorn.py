
bind = "0.0.0.0:8000"

daemon = False

chdir = "/opt/jarvis/"

workers = 4
worker_class = "gevent"
worker_connections = 1000
timeout = 30
keepalive = 30

pidfile = "./logs/gunicorn.pid"
accesslog = "./logs/access.log"
errorlog = "./logs/error.log"
loglevel = "info"