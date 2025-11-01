from flask import Flask, request, jsonify
import ddddocr
import requests

app = Flask(__name__)
ocr = ddddocr.DdddOcr()

@app.route("/ocr", methods=["POST"])
def ocr_api():
    data = request.get_json()
    image_url = data.get("image_url")

    if not image_url:
        return jsonify({"error": "missing image_url"}), 400

    try:
        # 直接下載圖片到記憶體
        resp = requests.get(image_url, timeout=5)
        resp.raise_for_status()
        img_bytes = resp.content

        # OCR 辨識（全在記憶體進行）
        result = ocr.classification(img_bytes)
        return jsonify({"result": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
