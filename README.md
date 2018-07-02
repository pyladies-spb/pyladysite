# Сайт PyLadies Spb
Сделан на статическом генераторе Mynt.

Сервится через Flask.

Для редактирования содержимого: 

Главная страница ```generated\_posts\2018\2018-07-1-About```

Code of Conduct ```generated\_posts\2018\2018-07-1-Code-of-Conduct```

FAQ ```generated\_posts\2018\2018-07-1-FAQ.md```

Что бы добавить партнера, нужно обновить partners в ```generated\config.yml```

Генерация страниц: 

	  создать virtualenv с python 2.7
	  
	```pip install generated/requirements.txt
	
	  cd generated
	  
	  mynt gen -f _site && mynt serve _site```

После изменения шаблонов в ```generated\_templates``` или параметров в ```generated\config.yml``` страницы обязательно перегенерить перед коммитом. 

После перегенерации и коммита изменения автоматом поднянуться на Heroku. 

Для того, что бы проверить, корректно ли flask сервит страницы: 
	создать virtualenv с python 3.6
	```pip install requirements.txt
	
	  FLASK_APP=app.py
	  
	  flask run```
	
