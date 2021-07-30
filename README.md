# Report_Traker

Django app for support reports

## Deploy

### Compose apps
1. Django(+bot) + gunicorn (wsgi);
2. Celery;
3. Redis(as Celery message broker);
4. Postgres(as DB);
5. Nginx;
6. Flower;
