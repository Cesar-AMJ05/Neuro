
"""
Perceptron Reconocimiento de Vocales
"""
import tkinter as tk  #pip install tk

P_a= [
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 1]
]
P_e= [
    [0, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 0]
]
w= [
    [0, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

def toggle_button(row, col):
    if matrix[row][col] == 0:
        matrix[row][col] = 1
        buttons[row][col].config(bg='#000000')
    else:
        matrix[row][col] = 0
        buttons[row][col].config(bg='#E5E5E5')

def obtener_datos_matriz(x):
    for row in range(6):
        for col in range(6):
            color_fondo = buttons[row][col].cget("bg")
            if color_fondo == "#E5E5E5":
                x[row][col] = 0
            else:
                x[row][col] = 1
    print_v_rcg(w)
    for fila in x:     #Quitar
        print(fila)
    return x

def print_v_rcg(mtx):
    for fila in range(len(mtx)):
        for col in range(len(mtx[0])):
            if mtx[fila][col] == 1:
                boxes[fila][col].config(bg='#000000')
            else:
                boxes[fila][col].config(bg='#E5E5E5')
     

#Generacionde la interfaz#
# Crear la ventana principal
root = tk.Tk()
root.title("Matriz 6x6")    
root.config(bg='#14213D')

# Inicializar la matriz de valores y la matriz de botones y la matriz de muestreo
matrix = [[0] * 6 for _ in range(6)]
buttons = [[None] * 6 for _ in range(6)]
boxes = [[None] * 6 for _ in range(6)]

#Matriz de dibujo
draw_matrix = tk.Frame(root)
draw_matrix.grid(row=0, column=0,padx=10)   
for row in range(6):
    for col in range(6):
        button = tk.Button(draw_matrix, width=5, height=2, bg='#E5E5E5', command=lambda r=row, c=col: toggle_button(r, c))
        button.grid(row=row, column=col)
        buttons[row][col] = button

# Frame matriz de reconocimiento
comp_matrix = tk.Frame(root, borderwidth=2, relief="sunken")
comp_matrix.grid(row=0, column=1,padx=10)
for row in range(6):
    for col in range(6):
        box = tk.Button(comp_matrix, width=5, height=2, bg='#E5E5E5')
        box.config(state='disabled')
        box.grid(row=row, column=col)
        boxes[row][col] = box

#Frame de botones de operacion
tool_bar=tk.Frame(root,borderwidth=2,relief='sunken')
tool_bar.grid(row=1, column=0, pady=10, columnspan=6)
rcg_btt=tk.Button(tool_bar,width=15, height=2,bg='#FCA311',text="Reconocer",command=lambda:obtener_datos_matriz(matrix))
rcg_btt.grid(row=0, column=0)


# Iniciar la aplicación
root.mainloop()
