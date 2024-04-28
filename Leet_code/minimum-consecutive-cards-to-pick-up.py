from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        num_to_idx = defaultdict()
        min_cards = float("inf")

        for end in range(len(cards)):
            if cards[end] in num_to_idx:
                min_cards = min(min_cards, end-num_to_idx[cards[end]]+1)
                
            num_to_idx[cards[end]] = end
            
        if min_cards == float("inf"):
            return -1

        return min_cards 
        