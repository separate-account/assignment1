import sys

def max_cyclic_substring_sum(s):
    n = len(s)
    # Concatenate string to itself to handle cyclic wraps
    s2 = s + s 
    
    left = 0
    current_sum = 0
    max_sum = 0
    seen = set()
    
    # Use xrange() in Python 2 for $O(1)$ memory usage during iteration
    for right in xrange(2 * n - 1):
        char = s2[right]
        val = ord(char) - ord('a') + 1
        
        # If character is already in the window, shrink from the left
        while char in seen:
            left_char = s2[left]
            seen.remove(left_char)
            current_sum -= (ord(left_char) - ord('a') + 1)
            left += 1
            
        # Add the current character to the window
        seen.add(char)
        current_sum += val
        
        # Update the maximum sum found so far
        if current_sum > max_sum:
            max_sum = current_sum
            
    return max_sum

# Read input and print output using Python 2 syntax
if __name__ == "__main__":
    input_str = sys.stdin.read().strip()
    if input_str:
        print max_cyclic_substring_sum(input_str)
