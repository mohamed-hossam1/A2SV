# Problem: Decode XORed Permutation - https://leetcode.com/problems/decode-xored-permutation/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        total_xor = 0
        for i in range(1, n + 1):
            total_xor ^= i
        except_first = 0
        for i in range(1, len(encoded), 2):
            except_first ^= encoded[i]
        first = total_xor ^ except_first
        perm = [first]
        for i in range(len(encoded)):
            next_val = perm[-1] ^ encoded[i]
            perm.append(next_val)
        return perm