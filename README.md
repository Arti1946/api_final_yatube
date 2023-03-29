### API Yatube Final:

Описание:

```
Проект API сервиса для работы с социальной сетью "Yatube".
Помогает использовать все возможности социальной сети через API.
```

### Установка:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Arti1946/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Примеры запросов к сервису:

Получение всех постов от любого пользователя методом GET:

```
http://127.0.0.1:8000/api/v1/posts/
```

Регистрация пользователя методом Post:

```
http://127.0.0.1:8000/auth/users
```

```
В теле запроса "Body" установить тип "raw" и выбрать формат "JSON".
передать значения полей "username", "password" в виде словаря.
{
    "username": "your_username",
    "password": "your_password"
}
```