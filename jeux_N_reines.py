import random
import tkinter as tk


class Particule:
    def __init__(self, n):
        self.position = [random.randint(0, n - 1) for _ in range(n)]
        self.vitesse = [random.uniform(-1, 1) for _ in range(n)]
        self.pBest = self.position[:]
        self.score_pBest = self.fitness()

    def fitness(self):
        """Calcule le nombre de conflits."""
        return compter_conflits_total(self.position)


def compter_conflits_total(solution):
    """Compter les conflits dans une solution donnée."""
    conflits = 0
    n = len(solution)
    for i in range(n):
        for j in range(i + 1, n):
            if solution[i] == solution[j] or abs(solution[i] - solution[j]) == abs(i - j):
                conflits += 1
    return conflits


def mise_a_jour_vitesse_et_position(particule, gBest, w=0.5, c1=1.5, c2=1.5):
    """Mise à jour de la vitesse et de la position des particules."""
    n = len(particule.position)

    # Mise à jour des vitesses
    for i in range(n):
        r1, r2 = random.random(), random.random()
        inertie = w * particule.vitesse[i]
        attraction_pBest = c1 * r1 * (particule.pBest[i] - particule.position[i])
        attraction_gBest = c2 * r2 * (gBest[i] - particule.position[i])

        particule.vitesse[i] = inertie + attraction_pBest + attraction_gBest

    # Mise à jour des positions en les gardant valides
    positions_temp = particule.position[:]
    for i in range(n):
        nouvelle_position = int(positions_temp[i] + particule.vitesse[i]) % n
        positions_temp[i] = max(0, min(nouvelle_position, n - 1))

    # Corriger les doublons en assurant une permutation valide
    particule.position = corriger_positions(positions_temp)


def corriger_positions(position):
    """Corrige les doublons pour garantir une permutation valide."""
    n = len(position)
    vue = set(position)
    manquantes = [x for x in range(n) if x not in vue]

    for i in range(n):
        if position.count(position[i]) > 1:
            position[i] = manquantes.pop()

    return position


def pso_n_reines(n, nb_particules=30, max_iterations=1000):
    """Algorithme PSO pour résoudre le problème des n-reines."""
    # Initialisation
    essaim = [Particule(n) for _ in range(nb_particules)]
    gBest = min(essaim, key=lambda p: p.fitness()).position
    score_gBest = compter_conflits_total(gBest)

    for iteration in range(max_iterations):
        for particule in essaim:
            # Mise à jour des vitesses et positions
            mise_a_jour_vitesse_et_position(particule, gBest)

            # Mise à jour du pBest
            score_actuel = particule.fitness()
            if score_actuel < particule.score_pBest:
                particule.pBest = particule.position[:]
                particule.score_pBest = score_actuel

            # Mise à jour du gBest
            if score_actuel < score_gBest:
                gBest = particule.position[:]
                score_gBest = score_actuel

        print(f"Iteration {iteration + 1}: gBest = {gBest}, Conflits = {score_gBest}")

        # Critère d'arrêt
        if score_gBest == 0:
            print("Solution trouvée avec 0 conflits.")
            break
    else:
        print("Impossible de trouver une solution avec 0 conflits dans le nombre maximal d'itérations.")

    return gBest, score_gBest


def afficher_solution(solution, conflits):
    """Affiche la solution sur un échiquier avec les conflits en rouge."""
    n = len(solution)
    root = tk.Tk()
    root.title("Solution des N-Reines")

    canvas = tk.Canvas(root, width=n*50, height=n*50)
    canvas.pack()

    for i in range(n):
        for j in range(n):
            color = "white" if (i + j) % 2 == 0 else "gray"
            canvas.create_rectangle(j*50, i*50, (j+1)*50, (i+1)*50, fill=color)

    for i in range(n):
        x, y = i, solution[i]
        color = "red" if any(solution[i] == solution[j] or abs(solution[i] - solution[j]) == abs(i - j) for j in range(n) if i != j) else "black"
        canvas.create_text(y*50+25, x*50+25, text="Q", fill=color, font=("Arial", 24))

    label = tk.Label(root, text=f"Nombre de conflits : {conflits}")
    label.pack()

    root.mainloop()


solution_finale, conflits_finaux = pso_n_reines(10)
print("Solution finale :", solution_finale)
print("Conflits finaux :", conflits_finaux)
afficher_solution(solution_finale, conflits_finaux)