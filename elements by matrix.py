##program to display the elements as matrix
n=[[1,2,3],[4,5,6],[7,8,9]]
print(n)
for r in n:
    print(r)
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j])
