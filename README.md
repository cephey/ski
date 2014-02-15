ski
===

1 pip install -r requirements.txt
2 ./manage.py collectstatic
3 python run.py
4 chmod +x gunicorn_start

5 cd /etc/supervisor/conf.d
6 sudo ln -s ~/works/ski/conf/ski.conf .
7 sudo supervisorctl reread
8 sudo supervisorctl update
9 sudo supervisorctl status ski - проверка статуса
  sudo supervisorctl stop/start/restart ski

10 cd /etc/nginx/sites-enabled
11 sudo ln -s ~/works/ski/conf/ski .
12 sudo /etc/init.d/nginx restart