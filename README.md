# WeatherApp

	Application in Python and Django, allowing to get information about the weather conditions 
	in different cities around the world.

	1) API for weather: https://openweathermap.org/
	2) Django official site: https://www.djangoproject.com/
	3) Requests module: https://pypi.org/project/requests/
______________________________________________________________________

	# Environment deployment
	sudo apt-get update 
	sudo apt-get -y upgrade
	sudo apt-get install -y python3-pip
	sudo apt-get install build-essential libssl-dev libffi-dev python-dev

	git clone git@github.com:solomino09/WeatherApp.git
	cd WeatherApp/

		Virtual Environment
	python3 -m venv env_py36
	source env_py36/bin/activate

		Software installation
	pip3 install -r requirements.txt
		
		DataBase dump
	sqlite3 db.sqlite3 < dump-2020-07-31_11-58.sql

	./manage.py migrate

		Launch
	./manage.py runserver

		User - admin
		Password - admin
___________________________________________________________________
