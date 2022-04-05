def posicion_signos(texto, signos_puntuacion):
    lista_signos = []
    for num_letras in range(len(texto)):
        for num_signos in range(len(signos_puntuacion)):
            if texto[num_letras] == signos_puntuacion[num_signos] and signos_puntuacion[num_signos] not in lista_signos:
                lista_signos.append(signos_puntuacion[num_signos])
    lista_lugar = [[] * 1 for i in range(len(lista_signos))]
    contador = 0
    for num_lista_signos in range(len(lista_signos)):
        for num_letras in range(len(texto)):
            if texto[num_letras] == lista_signos[num_lista_signos]:
                lista_lugar[contador].append(num_letras)
            if num_letras == len(texto) - 1:
                contador += 1
    return lista_signos, lista_lugar

