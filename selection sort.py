def selectSort(arr): 
    n = len(arr) 

    # Traverse through all array elements 
    for i in range(n): 
	
    	# Find the minimum element in remaining 
	# unsorted array
            min_idx = i 
            for j in range(i+1, n): 
                if arr[min_idx] > arr[j]: 
                    min_idx = j 
			
	# Swap the found minimum element with 
	# the first element		 
                arr[i], arr[min_idx] = arr[min_idx], arr[i] 
    print ("Sorted array is:") 
    for i in range(n):
        print ("[",i,"]",arr[i])
# Sorting arr array
items = [64, 34, 25, 12, 22, 11, 90,0] 
print ("List items are: " , items)
selectSort(items) 

input("Program has completed")

