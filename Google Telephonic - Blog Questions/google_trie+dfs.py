#Example Input: String: "can s r n " Dictionary: ["can", "canes", "serene", "rene", "sam"]
#Expected Output: ["can serene", "canes rene"]




'''
def find_words(i, str, word, word_list):
	if i == len(str):
		print (word)
		if word in set(word_list):
			output.append(word)
		return


	if str[i] == ' ':
		find_words(i+1, str, word + " ", word_list)
		find_words(i+1, str, word + "e", word_list)
	else:
		word += str[i]
		find_words(i+1, str, word, word_list)

	return


output = []
'''
#word_list = ["can", "canes", "serene", "rene", "sam"]

#find_words(0, "can s r n ","",word_list)
#print (output)


#["ne", "n"]

#[" ne", "ene", " n", "en"]



word_list = ["can", "canes", "serene", "rene", "sam"]



def build_trie(word_list):
	root = {}
	for word in word_list:
		curr_root = root
		for char in word:
			curr = {}
			if char in curr_root:
				curr_root = curr_root[char] 
			else:
				curr_root[char] = curr
				curr_root = curr
		curr['-'] = word

	return root



def buildTrie(words):
	root = {}
	for word in words:
	    curr = root
	    for letter in word:
	        if letter not in curr:
	            curr[letter] = {}
	        curr = curr[letter]
	    curr['-'] = word 
	return root

print(build_trie(word_list))
print(buildTrie(word_list))	

# 
# {'c':{'a':{'n':{'can':"#", 'e': {'s': {'canes':"#"}}}}}}



#n = 8 k = 4

#Answer: 5

#Explanation: [1,1,1,5], [1,1,2,4], [1,1,3,3], [1,2,2,3], [2,2,2,2]

