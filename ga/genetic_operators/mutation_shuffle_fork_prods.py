import random
from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation


class MutationShuffleForkProds(Mutation):
    # Seleciona um forklifts (com produtos) aleatorio e dá shuffle aos seus produtos

    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        num_genes = len(ind.genome)
        forklifts = []
        prods = []  # produtos do forklift selecionado

        for i in range(num_genes):
            if ind.genome[i] >= num_genes:
                if i == num_genes - 1:
                    break
                elif ind.genome[i + 1] < num_genes:  # só apanha forklifts com produtos
                    forklifts.append(ind.genome[i])
        forklift = random.choice(forklifts)

        flag = False
        start = -1
        end = -1
        for i in range(1, num_genes):
            if flag:
                if ind.genome[i] >= num_genes:
                    end = i
                    break
                else:
                    prods.append(ind.genome[i])
                    if i == num_genes - 1:
                        end = num_genes
                        break
            elif ind.genome[i] == forklift:
                start = i
                flag = True

        random.shuffle(prods)

        j = 0
        for i in range(start + 1, end):
            ind.genome[i] = prods[j]
            j += 1

    def __str__(self):
        return "Mutation Inversion (" + f'{self.probability}' + ")"
