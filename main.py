
import tkinter as tk
def calcular_sueldo():
    nombreTrabajador = nombreTrabajador_entry.get()
    sueldoBasico = int(sueldoBasico_entry.get())
    diasFalta = int(diasFalta_entry.get())
    minutosTardanza = int(minutosTardanza_entry.get())
    horasExtras = int(horasExtras_entry.get())



# Cálculo de bonificaciones
    pagoHorasExtras = 1.50 * horasExtras * sueldoBasico / 30 / 8
    movilidad = 1000
    bonificacionSuplementaria = 0.03 * sueldoBasico
    bonificaciones = movilidad + bonificacionSuplementaria + pagoHorasExtras
    remuneracionComputable = sueldoBasico + movilidad + bonificacionSuplementaria

# Cálculo de descuentos
    remuneracionMinima = sueldoBasico + bonificacionSuplementaria
    DescuentoFaltas = remuneracionComputable / 30 * diasFalta
    descuentoTardanzas = remuneracionComputable / 30 / 8 / 60 * minutosTardanza
    descuentos = round(DescuentoFaltas + descuentoTardanzas, 2)

    sueldoNeto = round(sueldoBasico + bonificaciones - descuentos, 2)

    nombreTrabajador_label.configure(text="{} Nombre del Trabajador:  {}".format(" ", nombreTrabajador))
    sueldoBasico_label.configure(text="{} Sueldo Basico:  {}".format(" ", sueldoBasico))
    bonificaciones_label.configure(text="{} Bonificaciones:  {}".format(" ", bonificaciones))
    descuentos_label.configure(text="{} Descuentos:  {}".format(" ", descuentos))
    sueldoNeto_label.configure(text="{} Sueldo Neto:  {}".format(" ", sueldoNeto))

ventana = tk.Tk()
ventana.title("Calculo de sueldo Horizonte")

#Ingreso de datos

nombreTrabajador_label = tk.Label(ventana, text="                               Ingrese nombre de Trabajador:                              ")
nombreTrabajador_label.pack()
nombreTrabajador_entry = tk.Entry(ventana)
nombreTrabajador_entry.pack()

sueldoBasico_label = tk.Label(ventana, text="Ingresar sueldo basico:")
sueldoBasico_label.pack()
sueldoBasico_entry = tk.Entry(ventana)
sueldoBasico_entry.pack()

diasFalta_label = tk.Label(ventana, text="Ingrese los dias de falta:")
diasFalta_label.pack()
diasFalta_entry = tk.Entry(ventana)
diasFalta_entry.pack()

minutosTardanza_label = tk.Label(ventana, text="Ingrese los minutos de tardanza:")
minutosTardanza_label.pack()
minutosTardanza_entry = tk.Entry(ventana)
minutosTardanza_entry.pack()

horasExtras_label = tk.Label(ventana, text="Ingrese las horas extras:")
horasExtras_label.pack()
horasExtras_entry = tk.Entry(ventana)
horasExtras_entry.pack()

#Insertando botones

calcular_button = tk.Button(ventana, text="Calcular sueldo", command=calcular_sueldo)
calcular_button.pack()

nombreTrabajador_label = tk.Label(ventana, text="")
nombreTrabajador_label.pack()
sueldoBasico_label = tk.Label(ventana, text="")
sueldoBasico_label.pack()
bonificaciones_label = tk.Label(ventana, text="")
bonificaciones_label.pack()
descuentos_label = tk.Label(ventana, text="")
descuentos_label.pack()
sueldoNeto_label = tk.Label(ventana, text="")
sueldoNeto_label.pack()

imprimir_button = tk.Button(ventana, text="imprimir")
imprimir_button.pack()

ventana.mainloop()

