from flask import Flask,render_template
import os
app = Flask(__name__)

app.config['SECRET_KEY']='XXXXXX'

@app.route('/',methods=['GET','POST'])
def index():
    command_result=os.popen('ipconfig')
    filesystem=command_result.readlines()
    return render_template('index.html',filesystem=filesystem)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8880,threaded=True)
