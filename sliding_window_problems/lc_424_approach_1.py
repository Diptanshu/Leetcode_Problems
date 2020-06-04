class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start_ptr = max_count = max_len = 0
        freq_map = collections.Counter()
        for end_ptr in range(0,len(s)):
        	# max_frequency_counter
            freq_map[s[end_ptr]] += 1
            max_count = max(max_count, freq_map[s[end_ptr]])
            if end_ptr -start_ptr+1 - max_count > k:
                print end_ptr
                freq_map[s[start_ptr]] -= 1
                start_ptr += 1
            max_len = max(max_len, (end_ptr-start_ptr+1))
        return max_len
                    
                
