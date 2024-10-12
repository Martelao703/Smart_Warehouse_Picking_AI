import random
from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual
from ga.genetic_algorithm import GeneticAlgorithm


class RecombinationSpx(Recombination):
    # Single-Point CrossOver - SPX
    # Seleciona um cut aleatorio e preenche o genoma de um filho com os genes de um dos pais ate ao cut, e preenche
    # o resto do genoma com os genes do outro pai, garantido que nao existem genes repetidos
    # Preserva a ordem relativa dos genes entre os pais


    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        num_genes = ind1.num_genes
        child1 = [-1] * len(ind1.genome)
        child2 = [-1] * len(ind2.genome)
        cut = random.randint(1, num_genes - 1)
        child1[:cut] = ind1.genome[:cut]
        child2[:cut] = ind2.genome[:cut]

        j = cut
        for i in range(num_genes):
            if ind2.genome[i] not in child1:
                child1[j] = ind2.genome[i]
                j += 1

        j = cut
        for i in range(num_genes):
            if ind1.genome[i] not in child2:
                child2[j] = ind1.genome[i]
                j += 1

        ind1.genome = child1
        ind2.genome = child2

    def __str__(self):
        return "OX recombination (" + f'{self.probability}' + ")"
