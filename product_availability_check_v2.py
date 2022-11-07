import pandas as pd

_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado",
"Limon", "Dulce de Leche"], "quantity": [3,10,0,5]})
_MAX_ATTEPMTS = 3

def is_product_available(product_name, quantity, attempt_N):
    if attempt_N < _MAX_ATTEPMTS:
        try:
            stock = _PRODUCT_DF["quantity"].loc[_PRODUCT_DF["product_name"] == product_name].values[0]
            if stock >= quantity:
                return True
            else:
                return False
        except:
            return False
    else:
        raise(Exception)