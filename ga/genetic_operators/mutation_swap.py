import random
from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation


class MutationSwap(Mutation):
    # Troca as posicoes de 2 produtos aleatorios

    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        num_genes = len(ind.genome)
        prods = []  # index dos produtos

        for i in range(1, num_genes):
            if ind.genome[i] < num_genes:  # product
                prods.append(i)

        prod1 = random.choice(prods)
        prod2 = random.choice(prods)

        while prod1 == prod2:
            prod2 = random.choice(prods)

        ind.genome[prod1], ind.genome[prod2] = ind.genome[prod2], ind.genome[prod1]

    def __str__(self):
        return "Mutation Shifting (" + f'{self.probability}' + ")"
