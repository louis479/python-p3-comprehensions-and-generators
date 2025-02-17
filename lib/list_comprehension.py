def return_evens(num_list):
    return [n for n in num_list if n % 2 == 0]
    
print(return_evens([0,1,2,3,4,5,7,8,9,11,13,14,15,17,19,]))

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))