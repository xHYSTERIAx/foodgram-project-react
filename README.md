![Foodgram_workflow](https://github.com/xHYSTERIAx/foodgram-project-react/workflows/main.yml/badge.svg)



## FOODGRAM 
Foodgram - приложение для публикации рецептов. В нём можно публиковать рецепты, добавлять чужие рецепты в избранное, подписываться на других авторов. Так же в нём можно создавать список покупок, в котором создается список необходимых продуктов для приготовления выбранного рецепта.

### Стек
- Python
- Django
- Django Rest Framework
- Postgres
- Docker
- Yandex cloud
- CI/CD


## Адрес приложения:
http://51.250.20.230/

### Запуск проекта на сервере:
- Склонируйте репозитрий на свой компьютер

- Установите на сервер Docker, Docker Compose

- Скопируйте на сервер файлы docker-compose.yml, nginx.conf из папки infra

- Cоберите образ при помощи docker-compose
    "$ sudo docker compose up -d "

- Примените миграции
    "$ sudo docker compose exec backend python manage.py makemigrations"
    "$ sudo docker compose exec backend python manage.py migrate"

- Соберите статику
    "$ sudo docker compose exec backend python manage.py collectstatic --no-input"

- Cоздайте суперюзера
    "$ sudo docker compose exec backend python manage.py createsuperuser"

- Заполните базу данных содержимым из файла ingredients.json
    "$ sudo docker compose exec backend python manage.py loaddata ingredients.json"
- Проверьте работоспособность приложения, для этого перейдите на страницу:

    "http://localhost/admin/"
 


 ## Авторы
   - Анастасия Жалненкова