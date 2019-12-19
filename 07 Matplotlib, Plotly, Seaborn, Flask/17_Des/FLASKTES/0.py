# BAHAN BELAJAR: http://flask.palletsprojects.com/en/1.1.x/

from flask import Flask, send_from_directory, abort, jsonify, render_template
server = Flask(__name__)

employees = [
    {"id":1, "nama":"Andi", "usia":20, "kota":"Jakarta"},
    {"id":2, "nama":"Budi", "usia":20, "kota":"Jakarta"},
    {"id":3, "nama":"Caca", "usia":20, "kota":"Jakarta"},
    {"id":4, "nama":"Dedi", "usia":20, "kota":"Jakarta"},
    {"id":5, "nama":"Eius", "usia":20, "kota":"Jakarta"}
]

#home route
@server.route('/')
def home():
    return render_template('html.html')

# render html
@server.route('/html')
def html():
    return render_template('html.html')

# render data from flask, render html
@server.route('/data')
def data():
    nama = "Andi"
    kota = "Jakarta"
    return render_template(
        'data.html',
        data = {'name': nama, 'city': kota}
    )

#route response json
@server.route('/karyawan')
def karyawan():
    return jsonify(employees)

#render static file: storage
@server.route('/file/<path:namaFile>')
def myFile(namaFile):
    return send_from_directory('storage', namaFile)

# route untuk error 404
@server.errorhandler(404)
def notFound(error):
    return render_template('error.html')

#dynamic route: karyawan/1
@server.route('/karyawan/<int:id>')
def Employees(id):
    if id > len(employees) or id < 1:
        abort(404)
    else:
        return jsonify(employees[id-1])


if __name__ == "__main__":
    server.run(debug = True,
    host = 'localhost',
    port = 1234
)