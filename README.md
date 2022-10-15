![yamdb_workflow](https://github.com/xHYSTERIAx/foodgram-project-react/workflows/foodgram_workflow/badge.svg)


## FOODGRAM 
Foodgram - приложение для публикации рецептов. В нём можно публиковать рецепты, добавлять чужие рецепты в избранное, подписываться на других авторов. Так же в нём можно создавать список покупок, в котором создается список необходимых продуктов для приготовления выбранного рецепта.

### Стек
- Python
- Django
- Django Rest Framework
- Postgres
- Docker
- Yandex cloud

## Адрес приложения:
http://51.250.20.230/

### Запуск проекта:
- Склонируйте репозитрий на свой компьютер
- Из папки "infra/" соберите образ при помощи docker-compose
    "$ docker-compose up -d --build"
- Примените миграции
    "$ docker-compose exec web python manage.py migrate"
- Соберите статику
    "$ docker-compose exec web python manage.py collectstatic --no-input"
- Для доступа к админке не забудьте создать суперюзера
    "$ docker-compose exec web python manage.py createsuperuser"
- Проверьте работоспособность приложения, для этого перейдите на страницу:
    "http://localhost/admin/"
 


 ## Авторы
   - Анастасия Жалненкова