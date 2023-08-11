from flask import Flask, request, Response, render_template
import random
import re
import os

app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/poem')
def getPoem():
    poem = request.args.get('baitho')
    taytien = './poems/taytien.txt'
    vietbac = './poems/vietbac.txt'
    datnuocnkd = './poems/datnuocnkd.txt'
    datnuocndt = './poems/datnuocndt.txt'
    danguitarcualorca = './poems/danguitarcualorca.txt'
    bacoi = './poems/bacoi.txt'
    song = './poems/song.txt'

    if (not poem or re.search(r'[^A-Za-z\.]', poem)):
        return 'Em hãy nhập đúng tên của bài thơ trong chương trình Ngữ văn lớp 12. Nếu em tiếp tục có những hành vi tấn công Website, cô sẽ ghi em vào sổ đầu bài!'

    with open(eval(poem), 'r', encoding='utf-8') as f:
        return render_template('index.html', poem=f.read())



@app.route("/")
def index():
    return render_template('index.html', poem='Em hãy chọn 1 bài thơ em thích.')


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=os.environ['PORT'])
