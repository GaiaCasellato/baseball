from dataclasses import dataclass

@dataclass
class Team:
    year : int
    worldSeriesWinnner : str
    wins : int
    teamRank : int
    teamCode : str
    stolenBases : int
    runs : int
    park : str
    name : str
    losses : int
    leagueWinner : str
    ID : int
    homerunsAllowed : int
    homeruns : int
    hitsAllowed : int
    hits : int
    gamesHome : int
    games : int
    divisionWinnner : str
    divID : str
    div_ID : int

    def __hash__(self):
        return hash(self.ID)

    def __str__(self):
        return f"{self.name}"