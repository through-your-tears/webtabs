# Тестовое задание Fruktorum
### https://drive.google.com/file/d/1v_98Qr_WzD-5xROA9NbhbJV2JzDdyNXA/edit

## Для запуска в docker(используя docker-compose) последовательно ввести
```docker
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```
После перейти на http://localhost/swagger/

В swagger authorization необходимо вставить в поле Token(apiKey) по приципу - Token {access token}, example "Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZXhwIjoxNjkyMjUxMjkxfQ.aJhEZBktpWQCFs5RK0MREgc6--U8ogqRz6UgFD9RHu8"