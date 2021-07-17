from flask import Flask, render_template, request, redirect, url_for, send_file, abort
import os, json, pyqrcode, png

app = Flask(__name__)
app.secret_key = 'xder56yhnko987654esxsw3456yujo9'


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/yrqr', methods=['GET','POST'])
def qr():
    if request.method == 'POST':
        links = {}
        if 'url' in request.form.keys():
            links=request.form['url']
            with open('log.json','w') as f:
                json.dump(links, f)
            #change the link to qr code and return 
            pyqrcode.create(links).png('/Users/mishals/Documents/Projects/qr-flask/static/qrcode.png', scale=6)
            return render_template('yrqr.html', link=request.form['url'])
            #redirect(url_for('static', filename='qrcode.png'))
       
    else:
        return redirect(url_for('home'))

@app.route('/download')
def download():
    return send_file('/Users/mishals/Documents/Projects/qr-flask/static/qrcode.png', as_attachment=True)

@app.route('/<string:text>')
def redirect_to_qr(text):
    return abort(404)

@app.errorhandler(404)
def pnf(error):
        return render_template('pagenotfound.html'), 404

