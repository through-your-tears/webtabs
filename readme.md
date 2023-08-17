# Тестовое задание Fruktorum
### https://drive.google.com/file/d/1v_98Qr_WzD-5xROA9NbhbJV2JzDdyNXA/edit

## Для запуска в docker(используя docker-compose) последовательно ввести
```docker
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```
После перейти на http://localhost/swagger/
