from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        frequency_map = Counter()
        for char in t:
            frequency_map[char] += 1 
        start_pointer = end_pointer = 0
        target_len= len(t)
        result = ""
        min_window_size = float("inf")
        for end_pointer in range(len(s)):
            if frequency_map[s[end_pointer]] > 0:
                target_len -= 1
            frequency_map[s[end_pointer]] -= 1
            while target_len == 0:
                window_size = end_pointer-start_pointer+1
                if window_size < min_window_size:
                    min_window_size = end_pointer-start_pointer+1
                    result = s[start_pointer:end_pointer+1]
                frequency_map[s[start_pointer]] += 1
                if frequency_map[s[start_pointer]] > 0:
                    target_len += 1
                start_pointer += 1
                print target_len
        return result
                    
                    