import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, jsonify
from mock_data import data


product_bp_list = Blueprint("procuct_bp_list", __name__)



@product_bp_list.route('/list', methods=['GET'])
def fn_product_list():
    return jsonify({
        "data":data
    })
    