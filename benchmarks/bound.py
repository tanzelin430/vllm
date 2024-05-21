
m = 300
n = 20

T = 16
G = 3441

upper_bound = 2*(m+n-1)*(T*G-m-1)/(2*m+2 + (2*m+n+1)*(n-1))
lower_bound = m+n-1

print(upper_bound, lower_bound)