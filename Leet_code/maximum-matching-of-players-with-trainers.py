class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)

        counter = 0
        p1 = 0
        p2 = 0

        while p1 < len(players) and p2 < len(trainers):
            if players[p1] <= trainers[p2]:
                counter+=1
                p1+=1
                p2+=1
            else:
                p1+=1
        
        return counter
        