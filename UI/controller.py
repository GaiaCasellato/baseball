import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def readDDTeams(self,e):
        if e.control.data is None:
            self._selectedTeam = None
        else:
            self._selectedTeam = e.control.data
        print(f"readDDTeams called -- {self._selectedTeam}")

    def handleCreaGrafo(self, e):
        pass

    def handleDettagli(self, e):
        pass

    def handlePercorso(self, e):
        pass

    def handleDDYearSelection(self,e):
        teams = self._model.getTeamsOfYear(self._view._ddAnno.value)
        self._view._txtOutSquadre.controls.clear()
        self._view._txtOutSquadre.controls.append(ft.Text(f"Ho trovato {len(teams)}"
                                                          f"squadre che hanno giocato nel {self._view._ddAnno.value}"))
        for t in teams:
            self._view._txtOutSquadre.controls.append(ft.Text(f"{t.teamCode}"))
            self._view._ddSquadra.options.append(
                ft.dropdown.Option(data= t, text= t.teamCode, on_click= self.readDDTeams)
            )

    def fillDDYears(self):
        years = self._model.getYears()
        for year in years:
            self._view._ddAnno.options.append(ft.dropdown.Option(year))

            # yearsDD = map(lambda x: ft.dropdown.Option(x), years) è la stessa cosa