from flask import Flask,Blueprint
from flask import request



bp = Blueprint('test', __name__, url_prefix='/bp')

@bp.route('/test', methods=['POST'])
def test1():
    return {'result': '这是一个POST'}



@bp.route('/test/<apiname>', methods=['POST'])
def test2(apiname):
    """
    /test/<apiname>：后面的apiname表示任意名字
    """

    args = request.get_json()
    
   
    return {'result': f'这是一个GET，您请求的是：{apiname}，您的参数是：{args}'}



app = Flask(__name__)
app.register_blueprint(bp)



if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = 5678)