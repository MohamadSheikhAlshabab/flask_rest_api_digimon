import requests
from flask import Flask,request,render_template

server = Flask(__name__)

url = 'https://digimon-api.vercel.app/api/digimon'
response = requests.get(url)
data = response.json()
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


@server.route('/')
@server.route('/digimon',methods =['GET'])
def get_digimon():
    try:
        return render_template('index.html',data=data,levels=levels)
    except Exception as err:
        print(err)

@server.route('/digimon/level/<level>',methods =['GET'])
def get_digimon_by_level(level):
    try:
        digimons_by_level = get_detail_by_level(level)
        return render_template('index.html',data=digimons_by_level,levels=levels)
    except Exception as err:
        print(err)

def get_detail_by_level(level):
    try:
        api = f'{url}/level/{level}'
        response_api = requests.get(api)
        data_api = response_api.json()
        return data_api
    except Exception as err:
        print(err)

@server.route('/digimon/name', methods=['GET'])
def get_digimon_by_name():
    try:
        search_name = request.args.get('name').lower()
        if search_name:
            filtered_data = [item for item in data if search_name in item['name'].lower()]
        else:
            filtered_data = data
        return render_template('index.html',data=filtered_data,levels=levels)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    server.run()