dev: check migrate
	python manage.py runserver

check:
	python manage.py check

migrate: 
	python manage.py makemigrations
	python manage.py migrate

dump:
	python manage.py dumpdata user > .fixtures/user.json

load:
	python manage.py loaddata  .fixtures/data.json

generate-keys:
	openssl genrsa -out private_key.pem 2048
	openssl rsa -in private_key.pem -pubout -out public_key.pem
