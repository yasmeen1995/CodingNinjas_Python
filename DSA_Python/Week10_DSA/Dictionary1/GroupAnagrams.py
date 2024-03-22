from typing import List

class GroupAnagram:
    def claculate_hash_str(self, freq: List[int]) -> str:
        str_freq = [str(num) for num in freq]
        return "$".join(str_freq)

    def calculate_freq_arr(self, word: str) -> List[int]:
        freq = [0 for _ in range(26)]
        for i in range(len(word)):
            # Ascii value of words
            freq[ord(word[i]) - ord('a')] += 1
        return freq

    def groupAnagarams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hashtable = {}

        for word in strs:
            freq_arr = self.calculate_freq_arr(word)
            hash_str = self.claculate_hash_str(freq_arr)

            if hashtable.get(hash_str, None):
                hashtable[hash_str].append(word)
            else:
                hashtable[hash_str] = [word]

        for value in hashtable.values():
            ans.append(value)

        return ans


if __name__ == "__main__":
    sol = GroupAnagram()
    print(sol.groupAnagarams(["eat", "tea", "tan", "ate", "bat", "nat"]))

