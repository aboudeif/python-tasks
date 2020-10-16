
# Returns index of ele in arr if present, else -1 
def binary_search(arr, low, high, ele): 

	# Check base case 
	if high >= low: 

		mid = (high + low) // 2

		# If element is present at the middle itself 
		if arr[mid] == ele: 
			return mid 

		# If element is smaller than mid, then it can only 
		# be present in left subarray 
		elif arr[mid] > ele: 
			return binary_search(arr, low, mid - 1, ele) 

		# Else the element can only be present in right subarray 
		else: 
			return binary_search(arr, mid + 1, high, ele) 

	else: 
		# Element is not present in the array 
		return -1

# Input searchkey
arr = [ 2, 3, 4, 6, 7,12,25,28,29,33,34,38,41,54,57 ]
print ("List items are: " , arr)
ele=int(input("please type the iteam you want to search for: "))

# Function call 
result = binary_search(arr, 0, len(arr)-1, ele) 

if result != -1: 
	print(ele,"is found in location [", str(result),"]") 
else: 
	print("Sorry,",ele,"is not found!")
input("Program has completed")
