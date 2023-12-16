def calculate_y(arr):
    n = len(arr)
    m = n - 1  
    y = 0
    product = 1  
    for i in range(n):
        if arr[i] < 0:
            m = i  
            break
        product *= arr[i]
        y += product
    return y, m


arr = [3, 2, 1, 4, -1, 5, 4]
result, m = calculate_y(arr)
print(f"Значення y: {result}")
print(f"Значення m: {m}")