### purpose

[spb.pyladies.com](http://spb.pyladies.com) website code.

### stack

Python 3.5, [pelican](http://docs.getpelican.com/en/stable/index.html)

### how to get the site running locally

Create virtualenv with Python3.

Install Python requirements:

```bash
pip install -r requirements.txt
```

Run pelican builder (with autoreload):
```bash
pelican -r
```

In a different terminal run server:

```bash
cd output
python -m http.server
```

Edit `content/` directory in order to make changes.

### how to deploy

Our hosting is the Heroku provided by [pyladies.com](http://pyladies.com).

So deploy is basically the usual:  
download Heroku toolbelt, set it up, then

```bash
git push heroku master
```
