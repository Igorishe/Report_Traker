# RTraker

RTraker is a support reports tracker. It is Django driven app that helps to customer service manager to track all long lasting cases. 

Support specialists send daily reports to special telegram-chat. Tracker bot parse it and save in database (Postgres) with appropriate status and tag.

Reports table keep data about: report creator(tg id, tg username), creation and edition datetime, status, tag and text with case description.

All reports can be edited in django admin. Admin panel includes default and few custom actions and filters. 

Bot and django app interact via API (running on DRF).

Celery tasks update statuses every day and send special notifications to admin and moderator. Redis works as Celery message broker.

Project also includes nginx configuration, docker & docker-compose files.

Also you can use ready CI-CD flow (auto tests, deploy and success notification) with Github Actions (main.yml file).

## Deploy RTra~~C~~ker to Debian-server

**Important!** Don't forget to create .env file in your project directory. 

Env file includes:

* SECRET_TOKEN - django app secret key;
* api_token - DRF OAuth token created for admin user;
* api_host=web - django app container name;
* bot_token - telegram-bot token from BotFather;
* bot_chat - daily reports chat id (must be negative);
* second_bot_chat - same for the second project report;
* admin_telegram - developer's telegram id;
* moderator_telegram - manager's telegram id;
* allowed_users=123456,123457,123458... - telegram id whitelist for bot;
* DB_ENGINE=django.db.backends.postgresql - database engine;
* DB_NAME - database name;
* POSTGRES_USER - username for database;
* POSTGRES_PASSWORD - password for database;
* DB_HOST=db - database container name;
* DB_PORT - database port;

In order to start you need to install docker and docker-compose on your server.

Then clone project from Git-repository and build&run docker-compose:

`cd Report_Traker`

`git pull https://github.com/Igorishe/Report_Traker.git`

`docker-compose up -d --build`

Following three commands will upload staticfiles and perform db migrations:

`docker-compose exec web python manage.py collectstatic --no-input`

`docker-compose exec web python manage.py makemigrations`

`docker-compose exec web python manage.py migrate --noinput`


#### Docker-compose starts seven containers
1. Postgres database (container name: db);
2. Redis as Celery message broker (container name: redis);
3. Django app + gunicorn as wsgi (container name: web);
4. TelegramBot (container name: bot);
5. Nginx http server (container name: nginx);
6. Celery worker (container name: celery);
7. Celery beat (container name: celery-beat);


