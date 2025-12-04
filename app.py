from flask import Flask, render_template

# 明確指定模板與靜態檔案資料夾
app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    # 回傳 templates/index.html
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
