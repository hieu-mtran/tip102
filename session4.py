# Problem 1: Balanced Art Collection
# As the curator of an art gallery, you are organizing a new exhibition. 
# You must ensure the collection of art pieces are balanced to attract the right range of buyers. 
# A balanced collection is one where the difference between the maximum and minimum value of the art pieces is exactly 1. 
# Given an integer array art_pieces representing the value of each art piece, 
# write a function find_balanced_subsequence() that returns the length of the longest balanced subsequence.
# A subsequence is a sequence derived from the array by deleting some or no elements without changing the order of the remaining elements.

# def find_balanced_subsequence(art_pieces):
#     d = {}
    
#     for i in range(len(art_pieces)):
#         if art_pieces[i] not in d:
#             d[art_pieces[i]] = 1
#         else:
#             d[art_pieces[i]] = d[art_pieces[i]] + 1

#     result = 0
#     for key in d:
#         if key+1 in d:
#             result = max(result, d[key] + d[key+1])
    
#     return result


# art_pieces1 = [1,3,2,2,5,2,3,7]
# art_pieces2 = [1,2,3,4]
# art_pieces3 = [1,1,1,1]
# art_pieces4 = [1,5,5,5]

# print(find_balanced_subsequence(art_pieces1))
# print(find_balanced_subsequence(art_pieces2))
# print(find_balanced_subsequence(art_pieces4))


# Problem 2: Verifying Authenticity
# Your art gallery has just been shipped a new collection of numbered art pieces, 
# and you need to verify their authenticity. The collection is considered "authentic" if it is a permutation of an array base[n].
# The base[n] array is defined as [1, 2, ..., n - 1, n, n], 
# meaning it is an array of length n + 1 containing the integers from 1 to n - 1 exactly once, and the integer n twice. 
# For example, base[1] is [1, 1] and base[3] is [1, 2, 3, 3].
# Write a function is_authentic_collection that accepts an array of integers 
# art_pieces and returns True if the given array is an authentic array, and otherwise returns False.
# Note: A permutation of integers represents an arrangement of these numbers. 
# For example [3, 2, 1] and [2, 1, 3] are both permutations of the series of numbers 1, 2, and 3.


# Problem 3: Gallery Wall
# You are tasked with organizing a collection of art prints represented by a list
# of strings collection. You need to display these prints on a single wall in a 2D array format that meets the following criteria:
# The 2D array should contain only the elements of the array collection.
# Each row in the 2D array should contain distinct strings.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them. 
# Note that the 2D array can have a different number of elements on each row.

def organize_exhibition(collection):
    d = {}
    
    for i in range(len(collection)):
         if collection[i] not in d:
             d[collection[i]] = 1
         else:
             d[collection[i]] = d[collection[i]] + 1
    
    for key in d:

    


collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))