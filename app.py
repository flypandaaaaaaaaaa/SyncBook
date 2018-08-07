from flask import Flask,render_template
import os
app = Flask(__name__)

app.config['SECRET_KEY']='XXXXXX'

@app.route('/',methods=['GET','POST'])
def index():
    # command_result=os.popen('ipconfig')
    # filesystem=command_result.readlines()
    filesystem=[]
    with open('D:\\filesystem.txt','r') as f:
        fstxt=f.readlines()
    for i in fstxt:
        single_fs=i.split()
        if len(i.split()[0].split('/'))==4 and 'mapper' in i.split()[0].split('/'):
            single_fs.append(i.split()[0].split('/')[3])
        else:
            single_fs.append('None')
        filesystem.append(single_fs)
        print(single_fs)
    filesystem.pop(0)
    return render_template('index.html',filesystem=filesystem)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8880,threaded=True)