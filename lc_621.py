import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        frequency_map = dict()
       	n_max_freq = []
        heapq.heapify(n_max_freq)
 

        for process in tasks:
        	if process not in frequency_map:
        		frequency_map[process] = 0
        	frequency_map[process] += 1


       	for process, freq in frequency_map.items():
       		heapq.heappush(n_max_freq, (-freq,process))

       	final_process_list = []
        while(n_max_freq):
            temp_list = []
            for i in range(n+1):
                if n_max_freq:
                    freq, process_name = heapq.heappop(n_max_freq)
                    frequency_map[process_name] -= 1
                    temp_list.append(process_name)
                else:
                    break
            if temp_list:
                for process in temp_list:
                    freq = frequency_map[process]
                    if freq > 0:
                        heapq.heappush(n_max_freq, (-freq, process))
            
            final_process_list += temp_list
            if n_max_freq:
                final_process_list += ['idle'] * (n+1 - len(temp_list))

       	return len(final_process_list)
        


if __name__ == '__main__':
		final_soln = Solution()
		final_soln.leastInterval(["A","A","A","B","B","B"],2)


