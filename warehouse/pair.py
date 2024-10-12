from agentsearch.agent import Agent

import copy


class Pair:
    def __init__(self, cell1, cell2):
        self.cell1 = cell1
        self.cell2 = cell2
        self.value = 0
        self.path = []
        self.fork_init_pos = cell1
        # TODO?

    def store_path(self, solution):
        cell_atual = copy.deepcopy(self.fork_init_pos)  # permite mudar a posicao inicial do forklift no gui sem alterar a cell1

        if solution:
            self.path.append(self.fork_init_pos)
            for i in solution.actions:
                if str(i) == "UP":
                    cell_atual.line -= 1
                elif str(i) == "RIGHT":
                    cell_atual.column += 1
                elif str(i) == "DOWN":
                    cell_atual.line += 1
                elif str(i) == "LEFT":
                    cell_atual.column -= 1

                self.path.append(copy.deepcopy(cell_atual))

    def getPath(self, cell1, cell2):
        if cell1 == self.cell1 and cell2 == self.cell2:
            return self.path
        elif cell1 == self.cell2 and cell2 == self.cell1:
            return self.path[::-1]  # reverse the path
        return None

    def getPathaux(self, cell1, cell2):  # debug
        if cell1 == self.cell1 and cell2 == self.cell2:
            return [[cell.line, cell.column] for cell in self.path]
        elif cell1 == self.cell2 and cell2 == self.cell1:
            return [[cell.line, cell.column] for cell in self.path[::-1]]  # reverse the aux path

    def isPair(self, cell1, cell2):
        return (cell1 == self.cell1 and cell2 == self.cell2) or (cell1 == self.cell2 and cell2 == self.cell1)

    def hash(self):
        return str(self.cell1.line) + "_" + str(self.cell1.column) + "_" + str(
            self.cell2.line) + "_" + str(self.cell2.column)

    def __str__(self):
        return str(self.cell1.line) + "-" + str(self.cell1.column) + " / " + str(self.cell2.line) + "-" + str(
            self.cell2.column) + ": " + str(self.value) + "\n"
