import numpy as np
import math

def lenghtOfPoints(x, y):
    return np.linalg.norm(x - y)
def lenghtOfAngle(x, y):
    return math.degrees(math.atan2(y, x))
points = np.array([
    [-7.3, -8.9],
    [2.7, -5.3],
    [-2.4, -4.8],
    [-6.0, -3.4],
    [-9.4,-6.4],
    [8.9, 0.1],
    [-9.2, 5.3],
    [3.4, 6.0]
])
lengths = [lenghtOfPoints(x, y) for x, y in points]
max_length = max(lengths)
max_length_indices = [i for i, length in enumerate(lengths) if length == max_length]

print("Точка(ки) які на максимальній відсатні від початку координат:")
for i in max_length_indices:
    print(f"Точка номер: {i + 1}: Координати:{points[i]}")
angles = [lenghtOfAngle(x, y) for x, y in points]
min_angle = min(angles)
min_angle_segment = angles.index(min_angle) + 1
print(f"Відрізок з мінімальним кутом до осі X: {min_angle_segment}")