from flask import Flask, request, jsonify
from flask import render_template, redirect, url_for
import cv2
import zxingcpp
import csv
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)


""" def process_image(imginput):
    # img = cv2.imread('myimage.png')
    img = cv2.imread(imginput)
    results = zxingcpp.read_barcodes(img)
    for result in results:
        print("Found barcode:\n Text:    '{}'\n Format:   {}\n Position: {}"
              .format(result.text, result.format, result.position))
    if len(results) == 0:
        print("Could not find any barcode.")
    return results[0].text


def search_str(file_path, word):
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if word in content:
            print('string exist in a file')
            return True
        else:
            print('string does not exist in a file')
            return False """


@app.route("/")
def homepage():
    var = "poos"
    message = request.args.get('message')
    return render_template('index.html', var=var, message=message)

@app.route('/upload', methods=['POST'])
def upload():
    print("POST request at /upload, received = > ", request.files)
    if 'csvFile' not in request.files:
        return 'No file part'
    
    file = request.files['csvFile']

    if file.filename == '':
        return 'No selected file'

    # Process the uploaded file as needed
    # For example, you can save it to a specific directory
    file.save('uploads/' + file.filename)

    return redirect(url_for('homepage',message='File uploaded successfully'))


""" @app.route('/upload', methods=['POST'])
def upload():
    print("POST request at /upload, received = > ", request.files)
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    print("Extracted file: ", file)
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        # decoded = reader.decode(file)
        file_path = "image.png"
        file.save(file_path)
        result = process_image(file_path)

        # Finding the legi in csv
        inCSV = search_str('students.csv', result)

        return jsonify({'result': result, 'inCSV': inCSV})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/camera', methods=['POST'])
def camera():
    print("POST request at /camera, received => ", request.files)
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['image']
    print("Extracted file: ", file)
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        # decoded = reader.decode(file)
        file_path = "screenshot.png"
        file.save(file_path)
        result = process_image(file_path)

        # Finding the legi in csv
        inCSV = search_str('students.csv', result)

        return jsonify({'result': result, 'inCSV': inCSV})
    except Exception as e:
        return jsonify({'error': str(e)})
 """

""" @app.route('/leginr', methods=['POST'])
def leginr():
    print("POST request received")
    # try:
    # Decode JSON data from the request body
    data = request.json

    # Assuming data contains a key named 'decodedBarcode'
    decoded_barcode = data.get('legi_nr')

    decoded_barcode = decoded_barcode[1:]

    print('decoded_barcode = ', decoded_barcode)

    found = False
    # Read the CSV file and find the corresponding names
    with open('upload/students.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['student_id'] == decoded_barcode:
                first_name = row['first_name']
                last_name = row['last_name']
                print(f"First Name: {first_name}, Last Name: {last_name}")
                found = True
                break
        else:
            print(f"Student ID {decoded_barcode} not found.")

    # Response
    if found:
        response_data = {
            'result': 'found',
            'first_name': first_name,
            'last_name': last_name
        }
    else:
        response_data = {
            'result': 'not_found',
            'first_name': 'null',
            'last_name': 'null'
        }

    print(response_data)

    return jsonify(response_data) """


@app.route('/leginr', methods=['POST'])
def leginr():
    print("POST request received")
    # try:
    # Decode JSON data from the request body
    data = request.json

    # Assuming data contains a key named 'decodedBarcode'
    decoded_barcode = data.get('legi_nr')

    decoded_barcode = decoded_barcode[1:]

    print('decoded_barcode = ', decoded_barcode)

    found = False
    # Read the CSV file and find the corresponding names
    with open('uploads/students.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['student_id'] == decoded_barcode:
                first_name = row['first_name']
                last_name = row['last_name']
                print(f"First Name: {first_name}, Last Name: {last_name}")
                found = True
                break
        else:
            print(f"Student ID {decoded_barcode} not found.")

    # Response
    if found:
        response_data = {
            'result': 'found',
            'first_name': first_name,
            'last_name': last_name
        }
    else:
        response_data = {
            'result': 'not_found',
            'first_name': 'null',
            'last_name': 'null'
        }

    print(response_data)

    return jsonify(response_data)

if __name__ == "__main__":
    # app.run(debug=True, ssl_context=('cert.pem', 'priv_key.pem'))
    # app.run(debug=True)
    #app.run(debug=True, host='0.0.0.0', port=5000)
    """ app.run(debug=True, host='0.0.0.0', port=5000,
            ssl_context=('server.crt', 'server.key')) """
    app.run(debug=True, host='0.0.0.0', port=8080,
            ssl_context=('server.crt', 'server.key'))
