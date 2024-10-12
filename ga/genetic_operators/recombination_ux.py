import random
from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual


class RecombinationUx(Recombination):
    # Uniform crossover - UX
    # Seleciona um numero aleatorio de cuts, e preenche o genoma de um filho com os genes de um dos pais nos cuts, e
    # preenche o resto do genoma com os genes do outro pai, garantido que nao existem genes repetidos

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        num_genes = ind1.num_genes
        child1 = [-1] * len(ind1.genome)
        child2 = [-1] * len(ind2.genome)
        child1[0] = ind1.genome[0]
        child2[0] = ind2.genome[0]

        num_cuts = random.randint(1, num_genes - 1)
        cuts = sorted(random.sample(range(1, num_genes), num_cuts))

        for i in range(1, num_genes):
            if i in cuts:
                child1[i] = ind2.genome[i]
                child2[i] = ind1.genome[i]

        unused_genes1 = [gene for gene in ind1.genome if gene not in child1]
        unused_genes2 = [gene for gene in ind2.genome if gene not in child2]

        for i in range(1, num_genes):
            if child1[i] == -1:
                child1[i] = unused_genes1.pop(0)
            if child2[i] == -1:
                child2[i] = unused_genes2.pop(0)

        ind1.genome = child1
        ind2.genome = child2

    def __str__(self):
        return "UX recombination (" + f'{self.probability}' + ")"
