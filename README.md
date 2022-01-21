# api_final

### _Описание проекта_

> ***Марк Туллий Цицерон***
>>Ничто так не сближает, как сходство характеров.
>>
Проект API для небольшой социальной сети. 
Позволяет публиковать собственные заметки и размещать к ним фото или любую другую картинку (желательно приличного содержания). Данный проект позволяет найти друзей, узнать что-нибудь новое и сделать это мир немного лучше.

### _Технологии_
 - _[Python 3.9.7](https://docs.python.org/3/)_
 - _[Django 2.2.16](https://docs.djangoproject.com/en/2.2/)_
 - _[Pillow 8.3.1](https://pillow.readthedocs.io/en/stable/)_
 - _[Django REST framework 3.12.4](https://www.django-rest-framework.org/)_
 - _[Simple JWT 4.7.2](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)_
 - _[Djoser 2.1.0](https://djoser.readthedocs.io/en/latest/)_


### _Как запустить проект_:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/kapkaevandrey/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
python3 pip install -r requirments.txt
```



### _Что могут делать пользователи_:

**Зарегистрированные :innocent:** пользователи могут:
1. Просматривать, публиковать, удалять и редактировать свои публикации;
2. Просматривать, информацию о сообществах;
3. Просматривать, публиковать комментарии от своего имени к публикациям других пользователей *(включая самого себя)*, удалять и редактировать **свои** комментарии;
4. Подписываться на других пользователей и просматривать **свои** подписки.
***Примечание***: Доступ ко всем операциям записи, обновления и удаления доступны только после аутентификации и получения токена.

**Анонимные :alien:** пользователи могут:
1. Просматривать, публикации;
2. Просматривать, информацию о сообществах;
3. Просматривать, комментарии;

### _Набор доступных эндпоинтов :point_down:_:
* ```redoc/``` - Подробная документация по работе API.
* ```api/v1/posts/``` - Получение постов и публикация новых (_GET, POST_).
* ```api/v1/posts/{id}``` - Получение, изменение, удаление поста с соответствующим **id** (_GET, PUT, PATCH, DELETE_).
* ```api/v1/posts/{post_id}/comments/``` - Получение комментариев к посту с соответствующим **post_id** и публикация новых комментариев(_GET, POST_).
* ```api/v1/posts/{post_id}/comments/{id}``` - Получение, изменение, удаление комментария с соответствующим **id** к посту с соответствующим **post_id** (_GET, PUT, PATCH, DELETE_).
* ```api/v1/posts/groups/``` - Получение описания зарегестрированных сообществ (_GET_).
* ```api/v1/posts/groups/{id}/``` - Получение описания сообщества с соответствующим **id** (_GET_).
* ```api/v1/posts/follow/``` - Получение информации о подписках текущего пользователя, создание новой подписки на пользователя (_GET, POST_).

* #### _Аутентификация :point_down:_:
  * ```api/v1/jwt/create/``` - Получение JWT-токена (_POST_). 
  * ```api/v1/jwt/refresh/``` - Обновление JWT-токена (_POST_). 
  * ```api/v1/jwt/verify/``` - Проверка JWT-токена (_POST_). 



### _Примеры выполнения запросов_:
##### Получаем JWT-токена 
>```api/v1/jwt/create/```
>
>Payload
>```json
>{
>"username": "string",
>"password": "string"
>}
>```
>Response sample (status code = 200)
>```json
>{
>"refresh": "string",
>"access": "string"
>}
>```


##### Опубликовать новый пост. 
(*требуется Аутентификация*)
>```api/v1/posts/```
>
>Payload
>```json
>{
>"text": "string",
>"image": "string",
>"group": 0
>}
>```
>Response sample (status code = 201)
>```json
>{
>"id": 0,
>"author": "string",
>"text": "string",
>"pub_date": "2019-08-24T14:15:22Z",
>"image": "string",
>"group": 0
>}
>```

##### Изменить свой комментарий к посту.
(*требуется Аутентификация*)
>```api/v1/posts/{post_id}/comments/{id}```
>
>Payload
>```json
>{
>"text": "string"
>}
>```
>Response sample (status code = 200)
>```json
>{
>"id": 0,
>"author": "string",
>"text": "string",
>"created": "2019-08-24T14:15:22Z",
>"post": 0
>}
>```

##### Подписаться на автора.
(*требуется Аутентификация*)
>```api/v1/posts/follow/```
>
>Payload
>```json
>{
>"following": "string"
>}
>```
>Response sample (status code = 201)
>```json
>{
>"user": "string",
>"following": "string"
>}
>```






#### Автор
Капкаев Андрей
>*Улыбайтесь - это всех раздражает :relaxed:.*
