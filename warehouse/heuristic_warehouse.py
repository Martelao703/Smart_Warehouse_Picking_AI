import warehouse.warehouse_problemforSearch
from agentsearch.heuristic import Heuristic
from warehouse.warehouse_problemforSearch import WarehouseProblemSearch
from warehouse.warehouse_state import WarehouseState


class HeuristicWarehouse(Heuristic[WarehouseProblemSearch, WarehouseState]):

    def __init__(self):
        super().__init__()

    def compute(self, state: WarehouseState) -> float:
        return abs(self.problem.goal_position.line - state.line_forklift) \
                + abs(self.problem.goal_position.column - state.column_forklift)

    def __str__(self):
        return "# TODO"
