def validar_id_usuario(id_usuario:str):
    """
    Valida que id_usuarios sea convertible a int
    Retorna True:False
    """
    # Completar
    return True

def validar_nombre(nombre:str):

    #saca los espacios vacios al principio y final
    nombre_limpio = nombre.strip()

    #valida que no este vacio y que solo tenga letras
    if nombre_limpio != "" and nombre_limpio.isalpha():
        return True
    else:
        return False
    
    return True

def validar_email(email:str):
    """
    Valida que email sea un correo válido"""
    # Completar
    return True