def get_angle(h,m):
    hour_angle = (h%12 + m/60)*30
    minute_angle = m*6
    angle=abs(hour_angle - minute_angle)
    return min(angle,360-angle)

h1,m1 = 9,0
print(get_angle(h1,m1))

h2,m2 = 3,30
print(get_angle(h2,m2))