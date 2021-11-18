import re
import numpy as np
import random
from flask import Flask, render_template, request
app = Flask(__name__)   


@app.route("/eleccion")
def elige():
    return render_template("intento desesperado.html")

@app.route("/proyecto")
def muestra_proyecto():
    return render_template("nosotros.html")

@app.route('/')          
def hello_world():
    return render_template("nuestro_proyecto.html")

@app.route("/Menú" , methods=['POST'])          
def menu():
    proteina_list=request.form.getlist("proteina[]")
    vegetales_list=request.form.getlist("vegetales[]")
    fruta_list=request.form.getlist("fruta[]")
    legumbres_list=request.form.getlist("Legumbres[]")

    if "Carne_molida" in proteina_list or "Cordero" in proteina_list or "Pollo" in proteina_list:
     result="como vay a comer 3 carnes waton ql"
     
    
    
    
    lista=[]
    for i in range(len(proteina_list)):
        for j in range(len(legumbres_list)):
            for k in range(len(vegetales_list)):
                for f in range(len(fruta_list)):
                        lista.append(f"{proteina_list[i]} + {legumbres_list[j]} (plato de fondo), {vegetales_list[k]} (ensalada) y {fruta_list[f]} (postre)")
                        # for q in range(0,2):
                        #     nose=[]
                        #     variable1=random.randint(0,len(lista))
                        #     nose.append(variable1)
                        result=np.array(lista)
                        

    
    
#     if proteina=="vacio" and  fruta=="vacio" and vegetales=="vacio" and Legumbres=="vacio":
#         result = "No has seleccionado lo que tienes disponible."

#     elif proteina=="Cordero" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="Papas":
#          result = "Cordero con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Pollo" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="Papas":
#          result = "Pollo con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Atún" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="Papas":
#          result = "Cordero con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="vacio" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="Papas":
#          result = "Cordero con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Carne_molida" and  fruta=="Manzanas" and vegetales=="vacio" and Legumbres=="Papas":
#          result = "Carne_molida con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"  

#     elif proteina=="Carne_molida" and  fruta=="Plátanos" and vegetales=="Apio" and Legumbres=="Papas":  
#          result = "Carne_molida con papas (plato de fondo), apio (ensalada) y platano (postre)"
#     elif proteina=="Carne_molida" and  fruta=="Cerezas" and vegetales=="Apio" and Legumbres=="Papas":
#          result = "Carne_molida con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Carne_molida" and  fruta=="Duraznos" and vegetales=="Apio" and Legumbres=="Papas":
#          result = "Carne_molida con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Carne_molida" and  fruta=="Manzanas" and vegetales=="vacio" and Legumbres=="Papas":
#          result = "Carne_molida con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"  
#     elif proteina=="Carne_molida" and  fruta=="vacio" and vegetales=="Apio" and Legumbres=="Papas":
#          result = "Carne_molida con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"

#     elif proteina=="Carne_molida" and  fruta=="Manzanas" and vegetales=="Champiñones" and Legumbres=="Papas":
#          result = "Carne_molida con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Carne_molida" and  fruta=="Manzanas" and vegetales=="Tomate" and Legumbres=="Papas":
#          result = "Carne_molida con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Carne_molida" and  fruta=="Manzanas" and vegetales=="Lechuga" and Legumbres=="Papas":
#          result = "Carne_molida con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Carne_molida" and  fruta=="Manzanas" and vegetales=="vacio" and Legumbres=="Papas":
#          result = "Carne_molida con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"    
#     elif proteina=="Carne_molida" and  fruta=="Manzanas" and vegetales=="vacio" and Legumbres=="Papas":
#          result = "Carne_molida con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"  

#     elif proteina=="Carne_molida" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="Poroto_negro":
#          result = "Carne_molida con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Carne_molida" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="Habas":
#          result = "Carne_molida con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Carne_molida" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="frijol":
#          result = "Carne_molida con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Carne_molida" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="vacio":
#          result = "Carne_molida con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Carne_molida" and  fruta=="Manzanas" and vegetales=="vacio" and Legumbres=="Papas":
#          result = "Carne_molida con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"  


#     elif proteina=="Cordero" and  fruta=="Plátanos" and vegetales=="Apio" and Legumbres=="Papas":  
#          result = "Cordero con papas (plato de fondo), apio (ensalada) y platano (postre)"
#     elif proteina=="Cordero" and  fruta=="Cerezas" and vegetales=="Apio" and Legumbres=="Papas":
#          result = "Cordero con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Cordero" and  fruta=="Duraznos" and vegetales=="Apio" and Legumbres=="Papas":
#          result = "Cordero con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Cordero" and  fruta=="Manzanas" and vegetales=="vacio" and Legumbres=="Papas":
#          result = "Cordero con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"  
#     elif proteina=="Cordero" and  fruta=="vacio" and vegetales=="Apio" and Legumbres=="Papas":
#          result = "Cordero con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"

#     elif proteina=="Cordero" and  fruta=="Manzanas" and vegetales=="Champiñones" and Legumbres=="Papas":
#          result = "Cordero con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Cordero" and  fruta=="Manzanas" and vegetales=="Tomate" and Legumbres=="Papas":
#          result = "Cordero con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Cordero" and  fruta=="Manzanas" and vegetales=="Lechuga" and Legumbres=="Papas":
#          result = "Cordero con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Cordero" and  fruta=="Manzanas" and vegetales=="vacio" and Legumbres=="Papas":
#          result = "Cordero con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"    
#     elif proteina=="Cordero" and  fruta=="Manzanas" and vegetales=="vacio" and Legumbres=="Papas":
#          result = "Cordero con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"  

#     elif proteina=="Cordero" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="Poroto_negro":
#          result = "Cordero con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Cordero" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="Habas":
#          result = "Cordero con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Cordero" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="frijol":
#          result = "Cordero con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Cordero" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="vacio":
#          result = "Cordero con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Cordero" and  fruta=="Manzanas" and vegetales=="vacio" and Legumbres=="Papas":
#          result = "Cordero con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"


#     elif proteina=="Pollo" and  fruta=="Plátanos" and vegetales=="Apio" and Legumbres=="Papas":  
#          result = "Pollo con papas (plato de fondo), apio (ensalada) y platano (postre)"
#     elif proteina=="Pollo" and  fruta=="Cerezas" and vegetales=="Apio" and Legumbres=="Papas":
#          result = "Pollo con papas (plato de fondo), apio (ensalada) y Cerezas (postre)"
#     elif proteina=="Pollo" and  fruta=="Duraznos" and vegetales=="Apio" and Legumbres=="Papas":
#          result = "Pollo con papas (plato de fondo), apio (ensalada) y Duraznos (postre)"
#     elif proteina=="Pollo" and  fruta=="Manzanas" and vegetales=="vacio" and Legumbres=="Papas":
#          result = "Pollo con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"  
#     elif proteina=="Pollo" and  fruta=="vacio" and vegetales=="Apio" and Legumbres=="Papas":
#          result = "Pollo con papas (plato de fondo) y apio (ensalada)"

#     elif proteina=="Pollo" and  fruta=="Manzanas" and vegetales=="Champiñones" and Legumbres=="Papas":
#          result = "Pollo con papas (plato de fondo), Champiñones (ensalada) y manzana picada (postre)"
#     elif proteina=="Pollo" and  fruta=="Manzanas" and vegetales=="Tomate" and Legumbres=="Papas":
#          result = "Pollo con papas (plato de fondo), Tomate (ensalada) y manzana picada (postre)"
#     elif proteina=="Pollo" and  fruta=="Manzanas" and vegetales=="Lechuga" and Legumbres=="Papas":
#          result = "Pollo con papas (plato de fondo), Lechuga (ensalada) y manzana picada (postre)"
#     elif proteina=="Pollo" and  fruta=="Manzanas" and vegetales=="apio" and Legumbres=="Papas":
#          result = "Pollo con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"    
#     elif proteina=="Pollo" and  fruta=="Manzanas" and vegetales=="vacio" and Legumbres=="Papas":
#          result = "Pollo con papas (plato de fondo) y manzana picada (postre)"  

#     elif proteina=="Pollo" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="Poroto_negro":
#          result = "Pollo con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Pollo" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="Habas":
#          result = "Pollo con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Pollo" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="frijol":
#          result = "Pollo con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Pollo" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="vacio":
#          result = "Pollo con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Pollo" and  fruta=="Manzanas" and vegetales=="vacio" and Legumbres=="Papas":
#          result = "Pollo con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"

    
#     elif proteina=="Atún" and  fruta=="Plátanos" and vegetales=="Apio" and Legumbres=="Papas":  
#          result = "Atún con papas (plato de fondo), apio (ensalada) y platano (postre)"
#     elif proteina=="Atún" and  fruta=="Cerezas" and vegetales=="Apio" and Legumbres=="Papas":
#          result = "Atún con papas (plato de fondo), apio (ensalada) y Cerezas (postre)"
#     elif proteina=="Atún" and  fruta=="Duraznos" and vegetales=="Apio" and Legumbres=="Papas":
#          result = "Atún con papas (plato de fondo), apio (ensalada) y Duraznos (postre)"
#     elif proteina=="Atún" and  fruta=="Manzanas" and vegetales=="vacio" and Legumbres=="Papas":
#          result = "Atún con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"  
#     elif proteina=="Atún" and  fruta=="vacio" and vegetales=="Apio" and Legumbres=="Papas":
#          result = "Atún con papas (plato de fondo) y apio (ensalada)"

#     elif proteina=="Atún" and  fruta=="Manzanas" and vegetales=="Champiñones" and Legumbres=="Papas":
#          result = "Atún con papas (plato de fondo), Champiñones (ensalada) y manzana picada (postre)"
#     elif proteina=="Atún" and  fruta=="Manzanas" and vegetales=="Tomate" and Legumbres=="Papas":
#          result = "Atún con papas (plato de fondo), Tomate (ensalada) y manzana picada (postre)"
#     elif proteina=="Atún" and  fruta=="Manzanas" and vegetales=="Lechuga" and Legumbres=="Papas":
#          result = "Atún con papas (plato de fondo), Lechuga (ensalada) y manzana picada (postre)"
#     elif proteina=="Atún" and  fruta=="Manzanas" and vegetales=="apio" and Legumbres=="Papas":
#          result = "Atún con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"    
#     elif proteina=="Atún" and  fruta=="Manzanas" and vegetales=="vacio" and Legumbres=="Papas":
#          result = "Atún con papas (plato de fondo) y manzana picada (postre)"  

#     elif proteina=="Atún" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="Poroto_negro":
#          result = "Atún con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Atún" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="Habas":
#          result = "Atún con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Atún" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="frijol":
#          result = "Atún con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Atún" and  fruta=="Manzanas" and vegetales=="Apio" and Legumbres=="vacio":
#          result = "Atún con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"
#     elif proteina=="Atún" and  fruta=="Manzanas" and vegetales=="vacio" and Legumbres=="Papas":
#          result = "Atún con papas (plato de fondo), apio (ensalada) y manzana picada (postre)"


    return render_template("result.html", 
    proteina=proteina_list,
    
    fruta=fruta_list,
    
    vegetales=vegetales_list,
    
    Legumbres=legumbres_list,
     
    result=result)
    





if __name__=="__main__":   
    app.run(debug=True)    
