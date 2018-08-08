from flask import Flask,render_template,request,redirect,url_for
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

@app.route('/extend/<lvname>',methods=['GET','POST'])
def extend(lvname):
    if request.method=='POST':
        tosize=request.form.get('tosize')
        os.system("ansible 192.168.29.201 -m shell -a '/root/extend_lv.sh'")
    with open('D:\\filesystem.txt','r') as f:
        fstxt=f.readlines()
    for i in fstxt:
        if lvname in i:
            extend_lvname=lvname
            size=i.split()[1]
            used=i.split()[2]
            break
    return render_template('extend.html',extend_lvname=extend_lvname,size=size,used=used)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8880,threaded=True)