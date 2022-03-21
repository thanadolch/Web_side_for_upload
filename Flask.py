from flask import Flask, render_template, request
import os
import pandas as pd
import zipfile as z
from werkzeug.utils import secure_filename
import subprocess

app = Flask(__name__)

def ex_file(name_file_zip):
    with z.ZipFile(name_file_zip,'r') as zf:
        zf.printdir()
        print("Extracting all the flies now...")
        zf.extractall()
        print("done!!")
        		
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    database = pd.read_csv('database.csv')
    if request.method == 'POST':
        brands = request.form.get('brand')
        serails = request.form.get('serail')
        colors = request.form.get('color')
        years = request.form.get('year')
        burns = request.form.get('burn')
        kears = request.form.get('kear')
        types = request.form.get('type')
        prices = request.form.get('price')
        database = database.append({'Brand':brands,'serail':serails,'color':colors,'year':years,'burn':burns,'kear':kears,'type':types,'price':prices}, ignore_index=True)
        database.to_csv('database.csv',index=False)
    if request.method == 'POST':
        for v in request.files.getlist('video'):
            f = request.files['file']
            f.save(os.path.join('picture',f.filename))
            #v = request.files['video']
            v.save(os.path.join('video',v.filename))
            print(f.filename)
            print(v.filename)
        return render_template('Tp.html',message='success')
    return render_template('Tp.html',message='Upload')

@app.route('/picture' ,methods = ['GET', 'POST'])
def page0():
    database = pd.read_csv('database.csv')
    if request.method == 'POST':
        folder = request.form.get('file_name')
        print(folder)
        folder_s = os.mkdir(str(folder))
        print(folder_s)
        brands = request.form.get('brand')
        serails = request.form.get('serail')
        colors = request.form.get('color')
        years = request.form.get('year')
        burns = request.form.get('burn')
        kears = request.form.get('kear')
        types = request.form.get('type')
        prices = request.form.get('price')
        database = database.append({'Brand':brands,'serail':serails,'color':colors,'year':years,'burn':burns,'kear':kears,'type':types,'price':prices}, ignore_index=True)
        database.to_csv('database.csv',index=False)
    if request.method == 'POST':
        print('hello')
        print(request.files)
        #folder = request.files
        #print(folder)
        #for i,j in folder.items():
           # print(i)
           # print(j)
        for v in request.files.getlist('video'):
            v.save(os.path.join(str(folder),v.filename))
        #v = request.files['video']
        #for v in request.folders('video'):
        #f = request.files['file']
        #print(f.filename)
        #print(v.filename)
        #f.save(os.path.join('picture',f.filename))
            #v = request.files['video']
            #v.save(os.path.join(str(folder)))
        call = f"\"C:\Program Files\Capturing Reality\RealityCapture\RealityCapture.exe\" -addFolder \"E:\Tan_Upload\{str(folder)}\" -setProjectCoordinateSystem Local:1 -detectMarkers \"E:\Tan_Upload\detectSettings.xml\" -importGroundControlPoints \"E:\Tan_Upload\markerPositions.csv\" \"E:\Tan_Upload\gcpSettings.xml\" -align -calculatePreviewModel -selectLargeTrianglesRel 30 -removeSelectedTriangles -setReconstructionRegion \"E:\Tan_Upload\object.rcbox\" -calculateNormalModel -selectLargestModelComponent -calculateTexture -simplify \"E:\Tan_Upload\simplifySettings.xml\" -save \"E:\Tan_Upload\Testa2.0.rcproj\" -exportSelectedModel \"E:\Tan_Upload\model\Testa2.01.obj\" \"E:\Tan_Upload\exportSettings.xml\"" 
        result = subprocess.run(call, capture_output=True, text=True, shell=True)
        return render_template('Tp.html',message='success')
    return render_template('Tp.html',message='Upload')


@app.route('/templates/recomment.html')		
def page():
    return render_template('recomment.html')


if __name__ == '__main__':
   app.run(port=5800)