def finn_forbrente_kalorier(minutter):
    for i in range(minutter+1):
        forbrente_kalorier = i*4.2
        if i % 5 == 0 and i != 5 and i != 0:
            print("Etter {} minutter har du forbrent {} kalorier".format(i, forbrente_kalorier))

finn_forbrente_kalorier(30)