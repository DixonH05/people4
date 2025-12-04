# 大學生作業 Deadline 管理系統 - Render 版

這個 zip 解壓縮後的結構已經可以直接部署到 Render。

## 在 Render 部署步驟（Web Service）

1. 登入 Render，點 **New → Web Service**。
2. 如果你用 GitHub，就選這個 repo；如果你只想上傳 zip，可以選 **Add files via upload**，把這個 zip 上傳。
3. 在設定畫面中確認：
   - Runtime：Python
   - Build Command：`pip install -r requirements.txt`
   - Start Command：`gunicorn app:app`
4. 建立服務並等待部署完成，Render 會給你一個網址，例如：
   `https://xxxx.onrender.com`，就是作業要填的「程式部署網址」。

## 檔案說明

- app.py：Flask 主程式，回傳 templates/index.html
- requirements.txt：Render 會依照這個裝 Flask 與 gunicorn
- templates/index.html：前端頁面（使用 localStorage 記錄作業）
- static/style.css：版面樣式
- static/app.js：主要功能（新增 / 編輯 / 刪除 / 排序 / 篩選 / 顏色提醒）
