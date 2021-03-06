from routes import app
from flask import send_file
from utils.wc import generate
import os
from pathlib import Path


@app.route("/wc/<stu_num>.png", methods=['GET'])
def wc(stu_num=None):
    file_path = os.getcwd() + "/utils/wc/tmp/{stu_num}.png".format(stu_num=stu_num)
    print(file_path)
    if not Path(file_path).is_file():
        generate.generate_place(stu_num)
    return send_file(file_path, as_attachment=False)
