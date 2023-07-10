def zoo(n, m, k):
    animales = [str(i) for i in range(1, n + 1)]  # creamos la lista de animales, el animal se llama igual que su tamaño
    escenas = []

    # First Part: (m - 1) * k scenes
    for i in range((m - 1) * k):
        escena = []
        for j in range(3):
            animal = animales.pop(0)  # Take an animal from the list
            escena.append(animal)
        escenas.append(escena)

    # Remaining m - 1 parts: k scenes each
    for i in range(m - 1):
        for j in range(k):
            escena = escenas[j].copy()  # Use scenes from the first part
            escenas.append(escena)

    return escenas
