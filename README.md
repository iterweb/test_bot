# Тестовое задание BotValley
Разработать бота с 3 нижними кнопками (ReplyKeyboardMarkup): BTC, ETH, DOGE (криптовалюты). При нажатии на кнопку, выводится курс (к USD) соответствующей криптовалюты. Для получения курса можно использовать любое API / парсить любой подходящий сайт/сайты. Если пользователь ввел что-то не то, нужно вывести соответствующее сообщение ошибки.

В админке на Django должен выводиться список юзеров бота в виде таблички: время первого запуска, ID, @username, имя, фамилия. Кроме этого, должна быть возможность редактирования текстов и кнопок бота (можно использовать django-preferences или любой другой удобный инструмент). По возможности, админку нужно сделать максимально красивой, убрать лишние ссылки, кнопки, разделы и т.д.

## Скриншоты
![alt tag](https://github.com/iterweb/test_bot/blob/master/screenshots/coin_bot.png)

![alt tag](https://github.com/iterweb/test_bot/blob/master/screenshots/profiles.png)

![alt tag](https://github.com/iterweb/test_bot/blob/master/screenshots/bot_settings.png)

![alt tag](https://github.com/iterweb/test_bot/blob/master/screenshots/bot_settings_1.png)

## Требования
* [python 3.7+](https://www.python.org/)
* ```pip install -r requirements.txt```
## Как пользоваться
* Создать Телеграм бота и записать его токен в файле ```settings.py``` на 139 строке
* Зарегистрироваться на сайте `https://coinmarketcap.com/api/v1/` для получения API KEY, полученый API KEY записать в файл ```settings.py``` на 138 строке
* Выполнить миграции ```python manage.py migrate```
* Создать супер пользователя (для админки) ```python manage.py createsuperuser```
* Запуск сервера ```python manage.py runserver```
* Запуск бота ```python manage.py tg_bot```
