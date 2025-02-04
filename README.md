# test_task

Необходимо склонировать проект
```
git clone https://github.com/Kaver160/test_task_bet_maker.git
```
Перейти в папку с проектом
```
cd test_task_bet_maker
```

Запустить docker-compose:
```
docker-compose up --build
```
Проект представлен 2 сервисами bet_maker и line_provider
bet_maker использует pgsql и alembic для миграций, также читает очереь, куда прислывает сообщения line_provider настроена очередь через RabbitMQ
Написаны тесты на pytest. 
