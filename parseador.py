import openpyxl
from openpyxl.utils import get_column_letter

class ExcelParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.workbook = openpyxl.load_workbook(file_path)
        self.sheet = self.workbook.active

    # Tus otros métodos aquí

    def print_values_from_range(self, start_row, end_row, codigo='B', descripcion='C', precio='D'):
        """
        Recorre las filas desde start_row hasta end_row e imprime los valores de las columnas especificadas
        por codigo, descripcion, y precio de cada fila, separados por un " - ".
        """
        print("Imprimiendo Rango")
        for row in range(start_row, end_row + 1):
        
        # Usa los nombres de las columnas parametrizadas
            codigo_value = self.sheet[f'{codigo}{row}'].value or ""
            descripcion_value = self.sheet[f'{descripcion}{row}'].value or ""
            precio_value = self.sheet[f'{precio}{row}'].value or 0
            if (codigo_value == "") & (descripcion_value == ""):
                pass
            else:
                print(f"{codigo_value} - {descripcion_value} - {precio_value}")

            #print(f"{type(b_value)} - {type(c_value)} - {type(d_value)}")

# Asegúrate de ejecutar esta celda o parte del script para definir correctamente la clase

# Luego, crea una nueva instancia de la clase y llama al método
parser = ExcelParser('lista22010422.xlsx')
#parser.print_values_from_range(15,56,'F','G','H')
parser.print_values_from_range(15,56)
