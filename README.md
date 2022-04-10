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
    
    
    
    
