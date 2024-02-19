# CRM Web App with Django

Create CRM App using python django with CRUD functionality.

- [X] Sign in & Sign up
- [X] CRUD Functions
- [X] SuperUser & Users

## Demo
CRM Web App - [LINK](https://crm-web-app-hi7g.onrender.com)

### Normal User
- USERNAME: banana
- PASSWORD: Hw9Ra8}CcA

### SuperUser
- USERNAME: demoadmin
- PASSWORD: demoadmin123

if you are requesting this app for first time then it will take 50s or more time to awake the instance. I'm using free hosting service so they spin down with inactive. that's why it will delay for first time.

# Database

I used **mysql** DB for development and for production I used **postgreSQL** DB.
This is dipending on **DEBUG ENV** true or false.
- True = MySQL
- False = postgreSQL

# render.yaml

This file contain all the configuration for deploy the web app in render.com. you only need to login to your render.com and use bluprint method and give git repo link. and this fill take care of all the config that you need to run the website.

You don't have to worry about DB this file will create DB for you and web app will migrate automatically.

# build.sh

This file contain all the commands that need to be run before run the server.
- it will install all the dependencies that needed.
- it will migrate if needed.
- it will create SuperUser if SuperUser didn't exist.

```bash
./bash.sh
```

# Server

I used gunicorn as a process manager, listening on a port an IP. and I used uvicorn as a workers handle the actual application communication, converting data to the ASGI standard for frameworks like FastAPI to use.

```bash
python -m gunicorn dcrm.asgi:application -k uvicorn.workers.UvicornWorkers
```