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