# Web_side_for_upload
เว็บสำหรับการอัปโหลดรูปภาพเพื่อสร้าง 3D โมเดล
## สเปกของอุปกรณ์ที่ใช้
- Note book ASUZ TUF Gaming FX505DT
- Invidia GTX 1650
- Ram 16 GB
- Rom 1 TB
- AMD Ryzen 5 3550H with Radeon Vega Mobile Gfx 2.10 GHz
## โปรแกรมที่ใช้
- visual studio code
### 1. ติดตั้ง packet Flask python 
#### ติดตั้ง Env และ install
    py -3 -m venv venv
    pip install Flask
#### packet ที่ใช้งาน
    from flask import Flask, render_template, request
    import os
    import pandas as pd
    import subprocess
### 2. เขียนโค้ดคำสั่งในการรับ input จากผู้ใช้ 
    if request.method == 'POST':
#### สร้างคำสั่งในการสร้างโฟล์เดอร์อัตโนมัติ       
        folder = request.form.get('serail')
        print(folder)
        folder_s = os.mkdir(str(folder))
        print(folder_s)
#### คำสั่งในการรับ input ในลักษณะของ text        
        brands = request.form.get('brand')
        serails = request.form.get('serail')
        colors = request.form.get('color')
        years = request.form.get('year')
        burns = request.form.get('burn')
        kears = request.form.get('kear')
        types = request.form.get('type')
        prices = request.form.get('price')
#### คำสั่งในการรับ input ในลักษณะของไฟล์ภาพ(หลายๆภาพต้อง วนลูปรับ)
        if request.method == 'POST':
            for v in request.files.getlist('video'):
            v.save(os.path.join(str(folder),v.filename)) ###(เก็บไฟล์รูปภาพไว้ในโฟล์เดอร์ที่สร้างขึ้นใหม่)
### 3. Subprocess เพื่อเรียกใช้โปรแกรม reality capture
#### setting ค่าไฟล์ที่ใช้ใน reality capture
โดยมีไฟล์การตั้งค่าทั้งหมด 6 ไฟล์ ดังนี้
-	detectSettings เป็นการตั้งค่าเพื่อในโปรแกรมค้นหาจุด Markers ที่มีอยู่ในภาพ หากไม่มี Markers ในภาพก็จะไม่สามารถสร้าง Model 3D แบบ Automatic ได้
-	exportSettings เป็นไฟล์การตั้งค่าเพื่อให้โปรแกรม Export ตามการตั้งค่าที่กำหนดไว้ในไฟล์ exportSettings.xml เพื่อให้โปรแกรม Export ไฟล์นามสกุล .obj, .MTL และไฟล์ Texture หรือไฟล์สี
-	gcpSettings เป็นไฟล์การตั้งค่าสำหรับให้โปรแกรมใช้การตั้งค่าพื้นดินเป็น location-1
-	markerPositions markerPositions.csv คือไฟล์ที่ใช้กำหนดจุดของ markers ในโปรแกรม RealityCapture โดยเราจะกำหนดจุดให้ แบบจำลอง 3 มิติอยู่ตรงกลางแกนพอดีหรือจุด (0,0) เพื่อให้ง่ายต่อการหมุนตรวจสอบ 
-	object.rcbox เป็นไฟล์ตั้งค่าสำหรับตัดสิ่งแวดล้อมตามที่เหมาะสมสำหรับการสร้าง แบบจำลองนั้นๆ 
-	simplifySettings ไฟล์การตั้งค่าสำหรับลดขนาดไฟล์ Model ที่จะทำการ Export ออกมา โดยได้ทดลองหลายๆแบบ เพื่อให้เหมาะสมกับการอัปโหลดและการแสดงผลในเว็ปแอบพลิเคชัน จากการทดลอง ขนาดของ Model ที่ควรจะ Export ออกมาคือ 30 MB

#### โค้ดในการ Subprocess
        call = f"\"C:\Program Files\Capturing Reality\RealityCapture\RealityCapture.exe\" -addFolder \"E:\Tan_Upload\             {str(folder)}\" -setProjectCoordinateSystem Local:1 -detectMarkers \"E:\Tan_Upload\detectSettings.xml\" -                 importGroundControlPoints \"E:\Tan_Upload\markerPositions.csv\" \"E:\Tan_Upload\gcpSettings.xml\" -align -                  calculatePreviewModel -selectLargeTrianglesRel 30 -removeSelectedTriangles -setReconstructionRegion                         \"E:\Tan_Upload\object17.rcbox\" -calculateNormalModel -selectLargestModelComponent -calculateTexture -simplify         \"E:\Tan_Upload\simplifySettings.xml\" -save \"E:\Tan_Upload\Testa2.0.rcproj\" -exportSelectedModel                         \"E:\Tan_Upload\{str(folder)}\{str(folder)}.obj\" \"E:\Tan_Upload\exportSettings.xml\"" 
        
            result = subprocess.run(call, capture_output=True, text=True, shell=True)
            return render_template('Tp.html',message='success')
        return render_template('Tp.html',message='Upload')

    
    
