'''
Write a program to find the euclidean distance between two
coordinates.
'''

def euclidean_dist(p1,p2):
    diff = [p1[x] - p2[x] for x in range(len(p1))]
    diff_squared = [diffs**2 for diffs in diff]
    ss = sum(diff_squared)
    return ss**0.5

p1 = (1,2)
p2 = (4,7)
result = euclidean_dist(p1,p2)
print(f"The Euclidean Distance is approximately {result:.6f}")