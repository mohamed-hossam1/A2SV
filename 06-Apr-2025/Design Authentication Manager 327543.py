# Problem: Design Authentication Manager - https://leetcode.com/problems/design-authentication-manager/

from collections import OrderedDict

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.orderedTokens = OrderedDict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.orderedTokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if (
            tokenId in self.orderedTokens
            and currentTime < self.orderedTokens[tokenId]
        ):
            self.orderedTokens[tokenId] = currentTime + self.timeToLive
            self.orderedTokens.move_to_end(tokenId, last=True)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        while self.orderedTokens:
            delete_me = False
            for tokenId in self.orderedTokens.keys():
                if self.orderedTokens[tokenId] <= currentTime:
                    delete_me = True
                break
            if delete_me:
                del self.orderedTokens[tokenId]
            else:
                break

        return len(self.orderedTokens)