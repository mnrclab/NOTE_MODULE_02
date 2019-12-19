from flask import request, redirect, jsonify, Flask, render_template
app = Flask(__name__)

x = [
    {'no':1, 'nama':'Andi'},
    {'no':2, 'nama':'Budi'},
    {'no':3, 'nama':'Caca'},
]

@app.route('/')
def beranda():
    return render_template('home.html')

@app.route('/home')
def home():
    return redirect('/')

@app.route('/data')
def data():
    return jsonify(x)
    
@app.route('/data/<int:no>')
def datano(no):
    return jsonify(x[no-1])

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return 'Anda nge-GET'
    # elif request.method == 'POST':
    #     return 'Anda nge-POST'
    elif request.method == 'POST':
        body = request.json
        print(body)
        return jsonify({
            'status' : 'Data sukses terkirim',
            'nama': body['name'],
            'usia': body['age']
        })
    else:
        return 'Anda request selain GET dan POST'

if __name__ == '__main__':
    app.run(debug = True, port=1992)