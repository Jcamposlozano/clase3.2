from Empleado import *
import pandas as pd

import plotly.graph_objects as go


empleados = []


e1 = Empleado()
e1.setNombre('Jonathan')
#e1.nombre = 'Jonathan' #### ESTO ESTA MAL
e1.setApellido('Campos Lozano')
e1.setSueldo(1000000)
e1.setDiasLiquidados(20)
empleados.append(e1) #Ingreso informacion en el arreglo


e2 = Empleado()
e2.setNombre('Angelica')
e2.setApellido('Franco R')
e2.setSueldo(2500000)
e2.setDiasLiquidados(25)
empleados.append(e2) #Ingreso informacion en el arreglo


e3 = Empleado()
e3.setNombre('Fernando')
e3.setApellido('Castro')
e3.setSueldo(4000000)
e3.setDiasLiquidados(28)
empleados.append(e3) #Ingreso informacion en el arreglo

#for i in empleados:
#    print('********************')
#    print(i)


row = []
for i in empleados:
    column = []
    column.append(i.getNombre())
    column.append(i.getApellidos())
    column.append(i.getSueldo())
    column.append(i.getDiasLiquidados())
    column.append(i.SalarioDevengado())
    row.append(column)

column_name = ["nombres", "apellidos"
                , "sueldo", "diasliquidados"
                ,"salariodevengado"]
df = pd.DataFrame(row, columns= column_name)


#**********************************************
# Histogram
'''
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="sum", y=df["sueldo"] 
                            ,x=df["nombres"]))
fig.add_trace(go.Histogram(histfunc="sum", y=df["salariodevengado"] 
                            ,x=df["nombres"]))
fig.show()
'''
#**********************************************
# PieCharm

label = df["nombres"]
value = df["sueldo"]

print(label)
print(value)

fig = go.Figure(data=[go.Pie(labels = label, values = value)])
fig.show()





'''
f = open('empleados.txt', 'w')
for i in empleados:
    f.write('\n******************\n')
    f.write(str(i))
f.close()
'''




