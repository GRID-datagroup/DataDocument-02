#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :   pic_server.py
@Author :   liuyihui
@Email  :   liuyihui02@gmail.com
'''

# here put the import lib
import os
from flask import Flask, request, render_template

# config
app = Flask(__name__, static_folder='./build/html/_static/', template_folder='./build/html/')
app.config['ROOT_FOLDER'] = os.path.abspath('./build/html/')

@app.route('/')
@app.route('/index.html')
def root() :
    return render_template('index.html')

@app.route('/genindex.html')
def genindex() :
    return render_template('genindex.html')

@app.route('/search.html')
def search() :
    return render_template('search.html')

@app.route('/searchindex.js')
def searchjs() :
    return render_template('searchindex.js')

@app.route('/brief.html')
def brief() :
    return render_template('brief.html')

@app.route('/norm.html')
def norm() :
    return render_template('norm.html')

@app.route('/detail/<src>')
def detail(src) :
    return render_template('./detail/'+src)

@app.route('/_sources/<src>')
@app.route('/_sources/detail/<src>')
def _sources() :
    return render_template(request.path)

@app.route('/favicon.ico')
def favicon() :
    return app.send_static_file('favicon.ico')

if __name__ == '__main__' :
    app.run(debug=True, host='0.0.0.0', port=9191)