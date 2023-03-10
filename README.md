![](https://github.com/freudentraenen/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# Групповой проект YaMDb.

### Описание
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «изобразительное искусство» или «Ювелирка»). 

Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).

Добавлять произведения, категории и жанры может только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

### Стек технологий использованный в проекте:
* Python 3.7
* Django 2.2.28
* Django REST framework 3.12.4
* Simple JWT 5.2.2
* django-filter 21.1
 

### Запуск проекта в dev-режиме:
1. Клонировать репозиторий и перейти в него в командной строке.
2. Установите и активируйте виртуальное окружение c учетом версии Python 3.7:

    ```
    python3 -m venv venv
    source venv/bin/activate
    python -m pip install --upgrade pip
    ```

3. Затем нужно установить все зависимости из файла requirements.txt:

    ```
    pip install -r requirements.txt
    ```

4. Выполняем миграции:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. (опционально) импортируйте подготовленные csv файлы в базу данных:

    ```
    python manage.py import_csv
    ```
    (!) Важно: импортировать файлы необходимо строго до создания суперпользователя
6. Создаем суперпользователя:

    ```
    python manage.py createsuperuser
    ```

7. Запускаем проект:

    ```
    python manage.py runserver
    ```

### Примеры работы с API для всех пользователей
Подробная документация доступна по эндпоинту /redoc/

Для неавторизованных пользователей работа с API доступна в режиме чтения, что-либо изменить или создать не получится.

```
Права доступа: Доступно без токена.
GET /api/v1/categories/ - Получение списка всех категорий
GET /api/v1/genres/ - Получение списка всех жанров
GET /api/v1/titles/ - Получение списка всех произведений
GET /api/v1/titles/{title_id}/reviews/ - Получение списка всех отзывов
GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/ - Получение списка всех комментариев к отзыву
Права доступа: Администратор
GET /api/v1/users/ - Получение списка всех пользователей
```

### Пользовательские роли

* Аноним — может просматривать описания произведений, читать отзывы и комментарии.
* Аутентифицированный пользователь (user) — может, как и Аноним, читать всё, дополнительно он может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять свои отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.
* Модератор (moderator) — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.
* Администратор (admin) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
* Суперюзер Django — обладает правами администратора (admin)

### Регистрация нового пользователя
Получить код подтверждения на переданный email. Права доступа: Доступно без токена. использовать имя 'me' в качестве username запрещено. Поля email и username должны быть уникальными.

Регистрация нового пользователя:
```
POST /api/v1/auth/signup/
```
```
{
  "email": "string",
  "username": "string"
}
```

Получение JWT-токена:
```
POST /api/v1/auth/token/
```
```
{
  "username": "string",
  "confirmation_code": "string"
}
```

### Примеры работы с API для авторизованных пользователей
Добавление категории:
```
Права доступа: Администратор.
POST /api/v1/categories/
```
```
{
  "name": "string",
  "slug": "string"
}
```

Удаление категории:
```
Права доступа: Администратор.
DELETE /api/v1/categories/{slug}/
```

Добавление жанра:
```
Права доступа: Администратор.
POST /api/v1/genres/
```
```
{
  "name": "string",
  "slug": "string"
}
```

Удаление жанра:
```
Права доступа: Администратор.
DELETE /api/v1/genres/{slug}/
```

Обновление публикации:
```
PUT /api/v1/posts/{id}/
```
```
{
"text": "string",
"image": "string",
"group": 0
}
```

Добавление произведения:
```
Права доступа: Администратор. 
POST /api/v1/titles/
```
```
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```

Добавление произведения:
```
Права доступа: Доступно без токена
GET /api/v1/titles/{titles_id}/
```
```
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```

Частичное обновление информации о произведении:
```
Права доступа: Администратор
PATCH /api/v1/titles/{titles_id}/
```
```
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```

Страница с документацией: http://yatbepraktikum.hopto.org/redoc/
