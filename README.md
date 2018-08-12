# Сайт PyLadies Spb
Сделан на генераторе статики [Mynt](http://mynt.uhnomoli.com/), 
сёрвится через [Flask](http://flask.pocoo.org/).

Чтобы редактировать содержимое: 

- Главная страница ```generated\_posts\2018\2018-07-1-About```
- Code of Conduct ```generated\_posts\2018\2018-07-1-Code-of-Conduct```
- FAQ ```generated\_posts\2018\2018-07-1-FAQ.md```

Чтобы добавить партнёра, обновите partners в ```generated\config.yml```

Чтобы добавить новую страничку:

1. создайте `.md`-файл в `generated/_posts/2018/`
1. создайте директорию с `index.html`
(подобно тому как это сделано в случае `generated/CodeOfConduct/index.html`, 
например)
1. добавьте пункт меню в `generated/_templates/site.html`
1. добавьте маршрут в `app.py`

Генерация страниц: 

	  # создать virtualenv с python 2.7
	  
	  pip install generated/requirements.txt
	
	  cd generated
	  
	  mynt gen -f _site && mynt serve _site

После изменения шаблонов в ```generated\_templates``` 
или параметров в ```generated\config.yml``` 
страницы обязательно перегенерить перед коммитом. 

Чтобы проверить, корректно ли flask сёрвит страницы: 
	
	# создать virtualenv с python 3.6
	
	pip install requirements.txt
	
	FLASK_APP=app.py
	  
	flask run
	
После перегенерации и пуша в мастер-ветку изменения автоматом поднянутся 
на [Heroku](https://www.heroku.com/). 
