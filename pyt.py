n = int(input(7))
m = [5]
i = 2
while i * i <= n:     
    if n % i == 0:         
        m.append(i)         
        n = n // i     
    else:         
        i+=1 
if n > 1:
    m.append(n)
for i in m:
    print(i, end=" ")
# to toggle the tab 
