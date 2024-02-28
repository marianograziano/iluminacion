import re
from datetime import datetime

def extraer_fecha(texto):
    try:
        # Definimos el patrón de búsqueda con expresiones regulares para encontrar la fecha
        # Usamos (SEPTIEMBRE|SETIEMBRE) para aceptar ambas ortografías
        patron = r'(\d{1,2}) DE (\w+) DE (\d{4})'
        # Buscamos en el texto el patrón definido, considerando mayúsculas y minúsculas
        match = re.search(patron, texto, re.IGNORECASE)
        if match:
            # Extraemos los componentes de la fecha
            dia, mes, ano = match.groups()
            # Convertimos el mes de texto a número
            meses = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO',
                     'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
            # Manejo especial para SEPTIEMBRE/SETIEMBRE
            mes = mes.upper()
            if mes == "SETIEMBRE":
                mes = "SEPTIEMBRE"
            mes_numero = meses.index(mes) + 1
            # Creamos un objeto datetime con la fecha extraída
            fecha = datetime(int(ano), mes_numero, int(dia))
            return fecha
        else:
            # Si no hay coincidencia, indicamos que no se puede extraer la fecha
            return "No se puede extraer la fecha."
    except ValueError:
        # Manejo de la excepción si ocurre un error en la conversión de datos
        return "No se puede extraer la fecha debido a un error en el formato."
    

def imprimir_tipo(cadena):
    # Patrón para verificar si comienza con 'U' seguido de un número
    patron_unipolar = re.compile(r'^U\d')
    # Patrón para verificar si comienza con 'UB' seguido de un número
    patron_unipolar_bobina = re.compile(r'^UB\d')
    patron_paralelo = re.compile(r'^P\d')
    patron_bipolar_rojo_negro= re.compile(r'^B\d')
    patron_tipo_taller = re.compile(r'^T\d')
    patron_tipo_taller_bobina = re.compile(r'^TB\d')
    patron_tipo_subterraneo = re.compile(r'^S\d')

    if patron_unipolar_bobina.match(cadena):
        return ("Unipolar bobina")
    elif patron_unipolar.match(cadena):
        return ("Unipolar")
    elif patron_paralelo.match(cadena):  # Added missing reference to "patron_paralelo"
        return ("Paralelo")  # Fixed return value
    elif patron_bipolar_rojo_negro.match(cadena):  # Added missing reference to "patron_bipolar_rojo_negro"
        return ("Bipolar rojo negro")  # Fixed return value
    elif patron_tipo_taller.match(cadena):
        return ("Tipo Taller Envainado")
    elif patron_tipo_taller_bobina.match(cadena):
        return ("Tipo taller Envainado Bobina")
    elif patron_tipo_subterraneo.match(cadena):
        return ("Subterraneo Flexible")
    else:
        return("No coincide")
