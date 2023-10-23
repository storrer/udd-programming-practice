"""
Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
"""

from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Create count dictionary empty
        #word_dict = {}
        # Count occurrences in word list
        #dictionary = {"the": 1}
        
        word_dict = Counter(words)
        # Sort k frequent words
        #for word in words:
        #    if word in word_dict:
        #        word_dict[word] += 1
        #    else:
        #        word_dict[word] = 1 
        
        print(word_dict.items())

        # Cast to list
        freq_list = word_dict.most_common()
        print("Frequency list", freq_list)
        word_dict

        # Sort lexicographically
        freq_list.sort(key=lambda x: x[0])

        # Sort by count
        freq_list.sort(key=lambda x: x[1], reverse=True)
        print("Sorted frequencies", freq_list)

        result = []

        for element in freq_list[:k]:
            result.append(element[0])
        
        return result




words = ["i","love","leetcode","i","love","coding"]
k = 1
counts = {
    "i": 2,
    "love": 2,
    "leetcode": 1,
    "coding": 1
}
# If there is no tie, output is max(values) -> key
counts_list = [("key",1), ("key2",2)]
counts_list.sort(key=lambda x: x[1])
#print(counts_list)


sol = Solution()
print(sol.topKFrequent(words, 2))
