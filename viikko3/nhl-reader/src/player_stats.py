
class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
    def top_scorers_by_nationality(self, nationality):
        unsorted = []
        players = self.reader.get_players()
        for player in players:
            if player.nationality == nationality:
                unsorted.append(player)
        
        sorted_players = sorted(unsorted, key= lambda x: x.goals + x.assists, reverse=True)
        
        return sorted_players

