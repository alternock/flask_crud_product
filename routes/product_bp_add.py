import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, jsonify, request
from mock_data import data
from helpers import _model_product_swap


product_bp_add = Blueprint('product_bp_app', __name__)



@product_bp_add.route('/add', methods=['POST'])
def fn_add_new_product():
    if request.method == 'POST':
        req = request.json

        new_product = _model_product_swap(req) 
  
        data.append(new_product)
    
        return jsonify({
            "data":new_product
        })   