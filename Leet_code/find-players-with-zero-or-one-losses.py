class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        n = len(matches)
        winners = {}
        losers = {}

        for match in matches:
            winners[match[0]] = winners.get(match[0], 0)+1
            losers[match[1]] = losers.get(match[1], 0)+1

        no_loss = []
        one_loss = []

        for winner in winners.keys():
            if winner not in losers.keys():
                no_loss.append(winner)

        for loser in losers.keys():
            if losers[loser] == 1:
                one_loss.append(loser)
                
        no_loss.sort()
        one_loss.sort()
            
        answer = [no_loss, one_loss] 
        return answer
