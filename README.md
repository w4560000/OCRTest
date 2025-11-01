
- 安裝套件 (Python 3.11.0 版本)
pip install Flask
pip install request
pip install jsonify
pip install ddddocr

pip install pyinstaller


- 打包 (連同套件 ddddocr)

pyinstaller --onefile --add-data "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\ddddocr;ddddocr" test_ocr.py

- 安裝服務
nssm.exe install TestOCR_Service D:\Stock\OCRTest\dist\test_ocr.exe
sc config TestOCR_Service start= auto


- 刪除服務
nssm.exe remove TestOCR_Service




