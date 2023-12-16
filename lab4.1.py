#Задано список (а). Написати програму формування іншого списку, в якому елементи сформовані таким чином 
#[a_1,a_(n+1),a_2,a_(n+2),…,a_n,a_2n]. 
a = [1, 2, 3, 4, 5]
result = []
n = len(a)
for i in range(n):
    result.append(a[i])
    if i % 2 == 0:
        result.append(a[i] * 2)
print(result)