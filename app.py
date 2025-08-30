from flask import Flask, request, jsonify
from flask_cors import CORS
from mock_data import data
from helpers import _search_product_by_id, _model_product_swap, _model_product_exchange_req_with_res


app = Flask(__name__)
CORS(app)



@app.route('/list', methods=['GET'])
def fn_product_list():
    return jsonify({
        "data":data
    })
    


@app.route('/search', methods=['GET'])
def fn_search_product_by_id():
    if request.method == 'GET':
        req_id = request.args.get('id', type=int)
    
        res = _search_product_by_id(req_id)
    
        return jsonify({
            "data":res
        })



@app.route('/add', methods=['POST'])
def fn_add_new_product():
    if request.method == 'POST':
        req = request.json

        new_product = _model_product_swap(req) 
  
        data.append(new_product)
    
        return jsonify({
            "data":new_product
        })   



@app.route('/del/<int:product_id>', methods=['DELETE'])
def fn_delete_product_by_id(product_id):
    if request.method == 'DELETE':
        res = _search_product_by_id(product_id)
    
        data.remove(res)
    
        return jsonify({
            "data":"delete success"
        })



@app.route('/modify', methods=['PUT'])
def fn_modify_all_by_id():
    req = request.json
    
    res = _search_product_by_id(req['id'])
    
    validate = _model_product_exchange_req_with_res(req, res)

    if validate:
        return jsonify({
            "data":res
        })
    
    return jsonify({
        "data":"modify not success"
    })
    
    


if __name__ == "__main__":
    app.run(debug=True)


