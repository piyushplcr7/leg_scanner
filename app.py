from flask import Flask, request, jsonify
from flask import render_template
import cv2
import zxingcpp
import csv
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

def process_image(imginput):
    #img = cv2.imread('myimage.png')
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
            return False

@app.route("/")
def homepage():
    var = "poos"
    return render_template('index.html',var=var)

@app.route('/upload', methods=['POST'])
def upload():
    print("POST request at /upload, received = > ",request.files)
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    print("Extracted file: ",file)
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        #decoded = reader.decode(file)
        file_path = "image.png"
        file.save(file_path)
        result = process_image(file_path)

        # Finding the legi in csv
        inCSV = search_str('students.csv',result)

        return jsonify({'result': result,'inCSV': inCSV})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/camera', methods=['POST'])
def camera():
    print("POST request at /camera, received => ",request.files)
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['image']
    print("Extracted file: ",file)
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        #decoded = reader.decode(file)
        file_path = "screenshot.png"
        file.save(file_path)
        result = process_image(file_path)

        # Finding the legi in csv
        inCSV = search_str('students.csv',result)

        return jsonify({'result': result,'inCSV': inCSV})
    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == "__main__":
    #app.run(debug=True, ssl_context=('cert.pem', 'priv_key.pem'))
    app.run(debug=True)