with open('mnist_train.csv') as f: #abrimos el con with para que se cierre una vez hecho
    next(f)  # Saltar encabezado por que el primero solo tiene las identificaciones
    for i, linea in enumerate(f):
        datos = linea.strip().split(',')  #lo convierte a una lista 
        etiqueta = int(datos[0]) #Agarra el primer dato de la lista que es la etiqueta
        entrada = []
        for px in datos[1:]: #empezamos despues de la etiqueta
            entrada.append(int(px) / 255.0)     #Normalizamos los valores a un valor de 0 a 1 y append 
        ##print(f"Línea {i+1}: etiqueta={etiqueta}, primeros 5 pixeles normalizados={entrada[:5]}")
        ##if i == 2:  
        ##    break                           ESTO FUE PARA PROBAR SE SALTABA LA PRIMERA FILA 