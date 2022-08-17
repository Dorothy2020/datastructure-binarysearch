# import math


# print(math.sqrt(49))
# Arranging the numbers in an array fromdecreasing order



# list_num=[10,9,8,7,6,5,4,3,2,1]
# # Accessing the number by use of indexing
# x=list_num[3]
# print(x)


# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1


# def binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = 0
 
#     while low <= high:
 
#         mid = (high + low) // 2
 
#         # If x is greater, ignore left half
#         if arr[mid] < x:
#             low = mid + 1
 
#         # If x is smaller, ignore right half
#         elif arr[mid] > x:
#             high = mid - 1
 
#         # means x is present at mid
#         else:
#             return mid
 
#     # If we reach here, then the element was not present
#     return -1
 
 
# # Test array
# arr = [ 2, 3, 4, 10, 40 ]
# x = 10
 
# # Function call
# result = binary_search(arr, x)
 
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")
# Create a python list of size MAX_HASH_TABLE_SIZE
# HASH TABLE
data_list=[None]*4096
print(data_list)

# iterating over a string character by character
String_name="Dorothy"
for i in String_name:
    print(i)

#  coverting a character into a number
char_num="r"
print(ord(char_num))

# Graphs
num_nodes=5
edges=[(0,1),(1,2),(1,4),(3,4),(2,3),(0,4),(3,1)]
print(num_nodes)
print(len(edges))

class Graph:
    def __init__(self,num_nodes,edges):
        self.num_nodes=num_nodes
        self.data=[[] for _ in range(num_nodes)]
        for n1,n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
graph1=Graph(num_nodes,edges) 
print(graph1.data)        



