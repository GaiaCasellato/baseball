import itertools

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._allTeams = []
    def buildGraph(self):
        self._grafo.clear()
        if len(self._allTeams) == 0:
            print("Lista squadre vuota.")
            return
        self._grafo.add_nodes_from(self._allTeams)
        #
        # for t1 in self._grafo.nodes:
        #     for t2 in self._grafo.nodes:
        #         if t1 != t2:
        #             self._grafo.add_edge(t1,t2)
        myedges = itertools.combinations(self._allTeams, 2)
        self._grafo.add_edges_from(myedges) # siccome è una lista di tuple posso usare questo metodo

    def getYears(self):
        return DAO.getAllYears()

    def getTeamsOfYear(self, year):
        self._allTeams = DAO.getTeamsOfYear(year)
        return self._allTeams

    def printGraphDetails(self):
        print(f"Grafo creato con {len(self._grafo.nodes)} nodi e {len(self._grafo.edges)} ")