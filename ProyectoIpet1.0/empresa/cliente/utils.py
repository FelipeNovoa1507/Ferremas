# utils.py

def validar_rut(rut):
    rut = rut.replace("-", "")
    cuerpo, dv = rut[:-1], rut[-1].upper()

    reversa = map(int, reversed(cuerpo))
    factor = 2
    suma = 0
    for d in reversa:
        suma += d * factor
        factor = 2 if factor == 7 else factor + 1 
    
    resto = suma % 11
    dv_calculado = '0' if resto == 0 else 'K' if resto == 1 else str(11 - resto)
    
    return dv == dv_calculado