from flask import Flask, request, send_from_directory
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='/generated')

generated_site = 'generated/_site'

@app.route('/')
def root():
    return send_from_directory(generated_site,'index.html')

@app.route('/faq/')
def faq():
    return send_from_directory(generated_site,'faq/index.html')

@app.route('/partners/')
def partners():
    return send_from_directory(generated_site,'partners/index.html')

@app.route('/resources/')
def resources():
    return send_from_directory(generated_site,'resources/index.html')

@app.route('/CodeOfConduct/')
def coc():
    return send_from_directory(generated_site,'CodeOfConduct/index.html')


@app.route('/assets/<path:path>')
def assets(path):
    return send_from_directory(generated_site+'/assets',path)