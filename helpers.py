from mock_data import data, next_id



def _search_product_by_id(id):
    for product in data:
        if product['id'] == int(id):
           return product
    return None    



def _generate_new_id_product():
    global next_id
    cache = next_id
    next_id += 1
    return cache



def _model_product_swap(req):
     return  {
        "id":_generate_new_id_product(),
        "nombre": req['nombre'],
        "precio": req['precio'],
        "pantalla": req['pantalla'],
        "bateria": req['bateria'],
        "almacenamiento": req['almacenamiento']
    }
    

def _model_product_exchange_req_with_res(req,res):
    res['nombre'] = req['nombre']
    res['precio'] = req['precio']
    res['pantalla'] = req['pantalla']
    res['bateria'] = req['bateria']
    res['almacenamiento'] = req['almacenamiento']    
    return True