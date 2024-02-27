from helper import extraer_fecha
from datetime import datetime
# Test case 10: Valid date format with leading zeros
texto = "03 DE MARZO DE 2022"
expected_output = datetime(2022, 3, 3)
assert extraer_fecha(texto) == expected_output

# Test case  D: Valid date format with single-digit day and month
texto = "1 DE ENERO DE 2023"
expected_output = datetime(2023, 1, 1)
assert extraer_fecha(texto) == expected_output

# Test case O Valid 5ate format with all lowercase month
texto = "15 de diciembre de 2024"
expected_output = datetime(2024, 12, 15)
assert extraer_fecha(texto) == expected_output

# Test case 13: Invalid date format with non-numeric day
texto = "AB DE JUNI ABCDO DE 2025"
expected_output = None
assert extraer_fecha(texto) == expected_output

# Test case 14: Invalid date format with non-existent month
texto = "20 DE XYZ DE 2026"
expected_output = None
assert extraer_fecha(texto) == expected_output

# Test case 15: Invalid date format with non-numeric year
texto = "10 DE OCTUBRE DE ABCD"
expected_output = None
assert extraer_fecha(texto) == expected_output

print("All test cases passed!")