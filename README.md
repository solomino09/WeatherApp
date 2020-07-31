# WeatherApp

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
