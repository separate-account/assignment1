import sys

def min_operations(n, a, k):
    # Base case for a single element array
    if n <= 1:
        return 0
        
    # Check if it's possible: all elements must have the same modulo K
    remainder = a[0] % k
    for x in a:
        if x % k != remainder:
            return -1
            
    # Sort the array to find the median
    a.sort()
    median_val = a[n / 2]
    
    # Calculate the total operations required to reach the median
    total_operations = 0
    for x in a:
        total_operations += abs(x - median_val) / k
        
    return total_operations

# Read standard input
if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    
    if input_data:
        n = int(input_data[0])
        a = [int(x) for x in input_data[1:n+1]]
        k = int(input_data[n+1])
        
        print min_operations(n, a, k)
