'''
- if my index == number the take that as a single chunk.


- assuming - numbers are not repeating

- calculate the end index of the chunk 

- initally assume start_chunk_size = end_chunk_size = 1

- index i -  j
  - all numbers should be present in that index i ..j
  - start range - end range - some chunk
    - if curr_idx == end_idx and number expected at this pos:
    	chunks += 1
    	start_idx = end_idx = idx+1
    else:
    	- if my number is present within the end range of this chunk

    	- if my number is not present within the range then increase the range of the chunk



- my assumption is that previous chunks have the required numbers.
'''

class Solution(object):
    def get_index(self, permute_arr, inverted_index_doc):
        for idx, num in enumerate(permute_arr):
            inverted_index_doc[num] = idx
    
    def maxChunksToSorted(self, arr):
        index_map = {}
        self.get_index(arr, index_map)
        def greedy_chunks(end_idx = 0):
            chunks = 0
            for curr_idx, num in enumerate(arr):
                to_be_num = curr_idx
                if curr_idx == end_idx and (num == to_be_num or index_map[to_be_num] < end_idx):
                    chunks += 1
                    end_idx = curr_idx+1
                else:
                    to_be_num_idx = index_map[to_be_num]
                    if to_be_num_idx <= end_idx:
                        continue
                    else:
                        end_idx = to_be_num_idx
            return chunks
        return greedy_chunks()


if __name__ == '__main__':
    num_chunks= Solution()
    print (num_chunks.maxChunksToSorted([4,3,2,1,0]))


