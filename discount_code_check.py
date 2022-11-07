_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1", "heladoFrozen"]

def validate_discount_code(discount_code):
    """
    Ejemplo:
    "primavera2021" deberia devolver True, ya que al compararlo:
    vs "Primavera2021" = 2 caracteres de diferencia ("p" y "P")
    vs "Verano2021" = 7 caracteres de diferencia ('i', 'n', 'o', 'm', 'V',
    'p', 'v')
    vs "Navidad2x1" = 8 caracteres de diferencia ('N', 'm', '0', 'x', 'e',
    'd', 'p', 'r')
    vs "heladoFrozen" = 14 caracteres de diferencia ('z', 'i', 'v', 'n',
    'o', 'm', '2', '0', 'd', 'p', '1', 'F', 'h', 'l')
    """
    for available_discount_code in _AVAILABLE_DISCOUNT_CODES:
        if compare_codes(available_discount_code, discount_code):
            return True
        return False

def compare_codes(available_discount_code, discount_code):
    if len(set(available_discount_code) ^ set(discount_code)) < 3:
        return True
    else:
        return False