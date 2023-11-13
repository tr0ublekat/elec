Руководство по установке проекта.

Пакеты, исользуемые в проекте:
1) Python 3.12.0;
2) pip 23.3.1;
3) Django 4.2.7;

Установка:
1) Создаём папку для хранения проекта (любое название), далее пишем в командной строке этой папки эту команду 'git clone https://github.com/tr0ublekat/elec.git'
2) Далее заходим в нашу папку, где лежит наш проект (одиночная папка elec) и устанавливаем виртуальную среду (venv) командой 'python -m venv venv'
3) Активируем вирт. среду командой 'venv\scripts\activate'. И если все получилось, то перед путем к папке в командной строке появится "(venv) C:\..."
4) Далее выполняем все команды под виртуальной средой
5) Устанавливаем django 'pip install django'
6) Устанавливаем scrispy forms 'pip install crispy-bootstrap5'
7) Устанавливаем Postgresql 16.1 'https://www.enterprisedb.com/downloads/postgres-postgresql-downloads'
8) Пишем в консоли под вирт средой 'pip install psycopg2'
9) Переходим по ссылке 'https://proghunter.ru/articles/django-base-2023-installing-postgresql-in-django#%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-postgresql-%D0%BD%D0%B0-%D0%BF%D0%BA' и следуем инструкциям пункта 'Запускаем pgAdmin'
10) На этом установка завершена.

Запуск локального сервера:
1) Переходим в папку elec (туда, где лежит manage.py) 'cd elec'
2) Запускаем сервер командой 'python manage.py runserver'

На этом всё, сайт запущен, переходим по ссылке http://127.0.0.1:8000/ и радуемся :)




  
  
  

