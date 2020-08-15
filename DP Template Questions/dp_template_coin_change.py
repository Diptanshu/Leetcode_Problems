

import sys
def find_mimimum_number_of_coins(coin_change_list, target):
	if target == 0:
		return 0
	ncoins = sys.INT_MAX
	for coin_value in coin_change_list:
		tmp = find_mimimum_number_of_coins(coin_change_list, target-coin_value)
		if tmp == INT_MAX:
			continue
		nCoins = min(nCoins, 1 + tmp)
	return nCoins

def find_minimum_number_of_coins(coin_change_list, target):
	dp = [None] * (target+1)
	dp[0] = 0
	max_coin_val = INT_MAX
	for each_state in range(target):
		for coin_value in coin_change_list:
			 if coin_value <= each_state:
			 	curr_val = dp[each_state - coin_value]
			 	if curr_val = INT_MAX:
			 		continue
			 	nCoins = min(nCoins, tmp+1)
		dp[each_state] = nCoins		

def count_different_ways_to_make_denominations(amount, num_of_denoms, denom_list):
	dp_table = (amount+1)*[(num_of_denoms+1)*[0]]

	# Amount == 0 ; return 1 
	for index in range(num_of_denoms+1):
		dp_table[0][index] = 1

	# Amount < 0 ; return 0 
	for index in range(amount+1):
		dp_table[index][num_of_denoms] = 0

	# f(a,i) = f(a,i+1) + f(a-di,i)
	# f(a,i) -> Number of different ways to make change of amount a using denominations di, di+1 ... dk
	for amount in range(1, amount+1):
		for index in range(k-1,0):
			dp_table[amount][index] = dp_table[amount][index+1]
			if (amount -  denom_list[index] >= 0):
				dp_table[amount][index] += dp_table[amount - denom_list[index]][index]


	return dp_table[amount][0]






 










