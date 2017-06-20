pi=2
for i in range(1000000):
    pi=pi*((4*(i+1)**2)/(4*(i+1)**2-1))

print(pi)
