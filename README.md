# testAPI
Скрипт для примера работы Spotify API. Выводит список всех альбомов и песен выбранного музыканта.
## Перед запуском:
1. Создать аккаунт на сайте developer.spotify.com.
2. Создать приложение developer.spotify.com/dashboard/applications.
3. Создать файл secret_info.py и записать в него две переменные из выше созданного приложения.
* CLIENT_ID = ""
* CLIENT_SECRET = ""
4. Импортировать библиотеки из файла requirements.txt.
5. По желанию изменить id музыканта в файле artist.py.

## Ответы: 
### Каким сервисом воспользовались?
Spotify.
### Количество запросов?
Два get запроса для получения данных о музыканте и его альбомах. Также get запрос в цикле, который возвращает информацию о песнях исполнителя.
### Используется ли база данных?
Нет.
### Сделано, как веб-сервер, или как скрипт?
Как скрипт.
### Прочее
Нет.
### Сколько времени затрачено?
Примерно 2 часа. На изучение api Spotify и создания скрипта.
