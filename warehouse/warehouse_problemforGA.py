from ga.problem import Problem
from warehouse.warehouse_agent_search import WarehouseAgentSearch
from warehouse.warehouse_individual import WarehouseIndividual


class WarehouseProblemGA(Problem):
    def __init__(self, agent_search: WarehouseAgentSearch):
        # TODO
        self.initial_state = agent_search.initial_environment
        self.forklifts = agent_search.forklifts
        self.products = agent_search.products
        self.agent_search = agent_search
        self.exit = agent_search.exit

    def generate_individual(self) -> "WarehouseIndividual":
        new_individual = WarehouseIndividual(self, len(self.forklifts) + len(self.products))
        new_individual.initialize(len(self.products), len(self.forklifts))
        return new_individual

    def __str__(self):
        string = "# of forklifts: "
        string += f'{len(self.forklifts)}'
        string = "# of products: "
        string += f'{len(self.products)}'
        return string
