# OgameBot
An ogamebot written in python. Just for fun!

[![Build Status](https://drone.quving.com/api/badges/Quving/ogamebot/status.svg)](https://drone.quving.com/Quving/ogamebot)



## Features
- Stack resources every 3 hours
- Update state every 15 minutes.

## Requirements
- Redis 4
- MySQL 5.7.8
- Chrome
- Python3.6
- All dependencies above can be handled by Docker.

## Installation
1. ``` git clone https://github.com/Quving/ogamebot.git ```
2. ``` cd ogamebot ```
3. ``` docker-compose build ```
4. ``` docker-compose up -d ```


### Further Steps
1. ``` docker exec -it ogamebot_bot_1 bash ```
2. ``` python manage.py makemigrations && python manage.py migrate ```
3. After these steps are done. Create an admin-user with the folling command: ``` python mange.py createsuperuser ```
3. Visit http://localhost:5000/admin



## Docker Setup
See example [docker-compose.yml]( https://github.com/Quving/ogamebot/blob/master/README.md) in this repository.


## Bot-Usage
Still in progress :-) 
