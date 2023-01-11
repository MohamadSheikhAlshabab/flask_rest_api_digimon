from logging import FileHandler,WARNING
from flask import Flask,request,render_template,send_from_directory
import requests,os

TEMPLATE_DIR = os.path.abspath('../templates')
STATIC_DIR = os.path.abspath('../static')

app = Flask(__name__)

file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

url = 'https://digimon-api.vercel.app/api/digimon'
response = requests.get(url)
response.raise_for_status()
data = response.json()
if response.status_code != 204:
    data
if response.status_code != 404:
    print(response)
levels = [
    'In Training',
    'Training',
    'Fresh',
    'Rookie',
    'Champion',
    'Ultimate',
    'Mega',
    'Armor'
    ]

@app.route('/')
@app.route('/digimon',methods =['GET'])
def get_digimon():
    return render_template('index.html',data=data,levels=levels)

@app.route('/digimon/level/<string:level>',methods =['GET'])
def get_digimon_by_level(level):
    try:
        digimons_by_level = get_detail_by_level(level)
        return render_template('index.html',data=digimons_by_level,levels=levels)
    except Exception as err:
        return print(err)

def get_detail_by_level(level):
    try:
        api = f'{url}/level/{level}'
        response_api = requests.get(api)
        data_api = response_api.json()
        return data_api
    except Exception as err:
        return print(err)

@app.route('/digimon/name', methods=['GET'])
def get_digimon_by_name():
    try:
        search_name = request.args.get('name').lower()
        if search_name:
            filtered_data = [item for item in data if search_name in item['name'].lower()]
        else:
            filtered_data = data
        return render_template('index.html',data=filtered_data,levels=levels)
    except Exception as err:
        return print(err)


@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=int(os.environ.get('PORT', 3000)))