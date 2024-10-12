import copy

from ga.individual_int_vector import IntVectorIndividual
import random


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        self.genome = []
        self.max_steps = 0
        self.collisions = 0
        self.fitness = 0
        # TODO

    def initialize(self, products: int, forklifts: int):
        product_list = list(range(products))
        forklift_list = list(range(forklifts))

        for i in range(forklifts):
            forklift_list[i] = self.num_genes + i

        self.genome.append(forklift_list[0])
        forklift_list.remove(forklift_list[0])
        aux_list = product_list + forklift_list
        random.shuffle(aux_list)
        self.genome = self.genome + aux_list

    def compute_fitness(self) -> float:
        fitness = 0
        self.obtain_all_path()
        self.fitness = self.max_steps + self.collisions
        # return fitness

    def obtain_all_path(self):
        forklift_path = [[]]
        forklift_path_aux = [[]]  # debug
        j = 0  # index of forklift_path
        cur_steps = 0
        max_steps = 0

        for i in range(len(self.genome)):
            if self.genome[i] < self.num_genes:  # gene é product

                cell2 = self.problem.products[self.genome[i]]
                if self.genome[i-1] >= self.num_genes:  # anterior é forklift
                    cell1 = self.problem.forklifts[self.genome[i-1]-self.num_genes]
                else:  # anterior é product
                    cell1 = self.problem.products[self.genome[i-1]]
                pair = self.getPair(cell1, cell2)
                pair_path = pair.getPath(cell1, cell2)
                pair_path_aux = pair.getPathaux(cell1, cell2)  # debug
                cur_steps += pair.value  # adiciona steps deste par aos steps do forklift atual

                if len(forklift_path[j]) > 0 and forklift_path[j][-1] == pair_path[0]:  # evita cells repetidas em forklift_path[j]
                    forklift_path[j].pop()
                    forklift_path_aux[j].pop()  # debug
                forklift_path[j].extend(pair_path)
                forklift_path_aux[j].extend(pair_path_aux)  # debug

            if i + 1 == self.num_genes or self.genome[i + 1] >= self.num_genes:  # ultimo gene ou proximo é forklift

                cell2 = self.problem.exit
                if self.genome[i] < self.num_genes:  # gene é product
                    cell1 = self.problem.products[self.genome[i]]
                else:  # gene é forklift
                    cell1 = self.problem.forklifts[self.genome[i] - self.num_genes]
                pair = self.getPair(cell1, cell2)
                pair_path = pair.getPath(cell1, cell2)
                pair_path_aux = pair.getPathaux(cell1, cell2)  # debug
                cur_steps += pair.value

                if len(forklift_path[j]) > 0 and forklift_path[j][-1] == pair_path[0]:
                    forklift_path[j].pop()
                    forklift_path_aux[j].pop()  # debug
                forklift_path[j].extend(pair_path)
                forklift_path_aux[j].extend(pair_path_aux)  # debug
                j += 1  # prepare for next forklift

                if i + 1 != self.num_genes:
                    forklift_path.append([])  # prepare for next forklift
                    forklift_path_aux.append([])  # debug

                if cur_steps > max_steps:
                    max_steps = cur_steps
                cur_steps = 0  # prepare for next forklift

        # COLLISIONS
        # verifica se uma cell é igual em dois forklift_paths diferentes no mesmo step

        sorted_forklift_paths = sorted(forklift_path, key=len)
        collision_count = 0
        for i in range(len(sorted_forklift_paths)):
            for j in range(i + 1, len(sorted_forklift_paths)):
                for step in range(min(len(sorted_forklift_paths[i]), len(sorted_forklift_paths[j]))):
                    cell_i = sorted_forklift_paths[i][step]
                    cell_j = sorted_forklift_paths[j][step]
                    if cell_i == cell_j:
                        collision_count += 1
                        break

        self.max_steps = max_steps
        self.collisions = collision_count
        return forklift_path, max_steps


    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += str (self.genome) + "\n\n"
        string += 'Max steps: ' + str(self.max_steps) + '\n'
        string += 'Collisions: ' + str(self.collisions) + '\n'
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        new_instance.max_steps = self.max_steps
        new_instance.collisions = self.collisions
        # TODO
        return new_instance

    def getPair(self, cell1, cell2):
        pairs = self.problem.agent_search.pairs
        for pair in pairs:
            if pair.isPair(cell1, cell2):
                return pair
        return None

    def get_sorted_prods(self):  # return de uma lista de listas, lista interna = produtos ordenados para um forklift
        sorted_prods = [[]]
        for i in range(self.num_genes):
            if self.genome[i] < self.num_genes:  # product
                sorted_prods[-1].append(self.problem.products[self.genome[i]])
            else:  # forklift
                if i == 0:  # first gene is forklift, no need to append empty list
                    continue
                sorted_prods.append([])
        return sorted_prods
