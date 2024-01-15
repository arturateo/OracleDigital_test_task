## Локальный запуск проекта

После клонирования проекта выполните команды:

### Изменить .env

Требуется переименовать .env_example в .env и поменять переменную API_KEY на действительную.

API_KEY можно получить по адресу после регистрации https://home.openweathermap.org/api_keys

### Создайте docker-container 

Данная команда соберет и установит все необходимое

```bash
docker-compose up -d --build
```

После выполнения команды выше можете обратиться по адресу http://127.0.0.1:8000/api/weather/?city=Bishkek.

Или попробовать указать свой город.