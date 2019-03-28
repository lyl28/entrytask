
# coding:utf-8
#!/usr/bin/env python
#!/usr/bin/python
from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

@app.errorhandler(404)
def handle_404_error(err_msg):
    return jsonify(
        error_code=11,
        errmsg='system error',
        reference='sorry to see this!'
    )


@app.route('/shopee/test')
def hello():
    a = request.args.get('a',  type = int),
    b = request.args.get('b',  type= str)
    if a is not None  and  a[0] is not None and b is not None and b[0]=='"' and b[-1]=='"' and len(b)>2:
         return jsonify(
        error_code=0,
        errmsg='success',
        reference='you are great!'
    )

    else:
        return jsonify(
        error_code=21,
        errmsg='empry or wrong params',
        reference='please check params again'
    )

if __name__ == '__main__':
    app.run()