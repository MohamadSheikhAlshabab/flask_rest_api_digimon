import requests
from flask import Flask,request,render_template

app = Flask(__name__)

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


# GET ALL DIGIMONs
@app.route('/')
@app.route('/digimon',methods =['GET'])
def get_digimon():
    return render_template('index.html',data=data,levels=levels)
# <------GET ALL DIGIMONs----->

# GET ALL DIGIMONs by level
@app.route('/digimon/level/<level>',methods =['GET'])
def get_digimon_by_level(level):
    digimons_by_level = get_detail_by_level(level)
    return render_template('index.html',data=digimons_by_level,levels=levels)

# function to filter by level
def get_detail_by_level(level):
    api = f'{url}/level/{level}'
    response_api = requests.get(api)
    data_api = response_api.json()
    return data_api
# <------GET ALL DIGIMONs by level----->

# function to filter by name
@app.route('/digimon/name', methods=['GET'])
def get_digimon_by_name():
    search_name = request.args.get('name').lower()
    if search_name:
        filtered_data = [item for item in data if search_name in item['name'].lower()]
    else:
        filtered_data = data
    return render_template('index.html',data=filtered_data,levels=levels)
# <------GET ALL DIGIMONs by name----->

# @app.route('/digimon/<name>', methods=['POST'])
# def update_digimon_by_id(id):
#     return "pass"

# @app.route('/digimon/<name>', methods=['PUT'])
# def update_digimon_by_id(id):
#     return "pass"

# @app.route('/digimon/<name>', methods=['DELETE'])
# def delete_digimon_by_id(id):
#     return "pass"

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)