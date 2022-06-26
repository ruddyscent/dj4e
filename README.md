# dj4e

```shell
cd dj4e
docker build -t django .
cd mysite
docker run -it -p 8000:8000 -v $PWD:/usr/src/app django python manage.py runserver 0:8000
```
