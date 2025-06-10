from typing import List

def sliding_window(arr:List[int], k:int) -> List[int]:
    if not arr or k <= 0 or k > len(arr):
        return []
        
    result = []
    # Calculate first window
    window_sum = sum(arr[:k])
    result.append(window_sum)
    
    # Slide the window
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        result.append(window_sum)
        
    return result

print(sliding_window([1,2,3,4,5], 3))

