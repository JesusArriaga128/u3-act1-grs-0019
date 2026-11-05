import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#crearemos nuestra tabla y la guardaremos con pandas 
# tenemos 5 listas  de redes sociales con 4 elementos por lista
fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkdin', 7277, False, 2012]
# creamos una lista de listas (conformando tabla)
lista_redes_sociales=[fb,twt,ig,wsp,tel,lkn]
# print(lista_redes_sociales)
# utilizar panda para organizar la tabla (dataframe o marco de datos)
# a cada columna le ponemos nombre
df_redes_sociales=pd.DataFrame(lista_redes_sociales,columns=["Nombre","Cantidad","Es_FB","Año"])
print(df_redes_sociales)
# creamos el archivo CSV  y lo guardamos en CSV 
#df_redes_sociales.to_csv("redessociales.csv", index=False)
plt.plot(df_redes_sociales['Nombre'],df_redes_sociales['Cantidad'])
plt.title('grafica de redes sociales 0019')
plt.xlabel('Aplicaciones')
plt.ylabel('Cantidades de usuarios')
plt.show()
# creamos grafica de puntos 
plt.scatter(df_redes_sociales['Nombre'],df_redes_sociales['Cantidad'])
plt.show()
# grafica de barras 
barras = plt.bar(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.title("Redes sociales")
plt.xlabel("Las redes sociales")
plt.ylabel("Cantidad de usuarios")
plt.show()
#Ordenar la grafica de tablas de manera descendente 
df_rs_ordenar=df_redes_sociales.sort_values('Cantidad',ascending=False)
plt.bar(df_rs_ordenar['Nombre'],df_rs_ordenar['Cantidad'])
plt.show()
# coloriando la grafica 
df_rs_ordenar=df_redes_sociales.sort_values('Cantidad',ascending=False)
plt.bar(df_rs_ordenar['Nombre'],df_rs_ordenar['Cantidad'],
     color=['b','g','c','m','y','r'])
plt.show()
# grafica de pastel 
plt.plot(df_redes_sociales['Nombre'],df_redes_sociales['Cantidad'])
plt.pie(df_redes_sociales['Cantidad'],labels=df_redes_sociales['Nombre'])
plt.show()