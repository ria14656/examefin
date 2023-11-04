
# Crear un nuevo libro de Excel
libro_de_trabajo = openpyxl.Workbook()

# Seleccionar la hoja activa
hoja=libro_de_trabajo.active
hoja.title = "Lista_de_supermercado"
                                    
# Agregar encabezados 
  
hoja['A1'] = "Supermercado"
hoja['B1'] = "Producto"
hoja['C1'] = "Precio"

# Lista de supermercados con nombre de producto y precio
supermercados = [
    ("Supermercado A", "Manzanas", 2.99),
    ("Supermercado A", "Peras", 3.49),
    ("Supermercado B", "Naranjas", 2.79),
    ("Supermercado B", "Kiwi", 3.29),
    # Agrega mas productos y precios aqui
]

# Agregar datos a la hoja
for fila, datos in enumerate(supermercados, start=2):
    hoja.cell(row=fila, column=1, value=datos[0])
    hoja.cell(row=fila, column=2, value=datos[1])
    hoja.cell(row=fila, column=3, value=datos[2])

# Guardar el archivo Excel
libro_de_trabajo.save("lista_supermercados.xlsx")

# Cerrar el archivo Excel
libro_de_trabajo.close()
