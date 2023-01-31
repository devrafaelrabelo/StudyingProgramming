# ADD (adicional), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas nao em ambos)

s1 = {1, 2, 3, 4, 5}
print(s1, type(s1))

for v in s1:
    print(v, type(v))

s2 = set()

print('')

s2.add(1)
s2.add((1, 2, 3))
s2.add(2)
s2.add(2)
s2.discard(2)
s2.update('Python')

print('\n', s2)

for s in s2:
    print(s, type(s))

print("S1")
s1 = {1, 2, 3, 4, 5, 6}
print(s1, type(s1))

print("S2")
s2 = {4, 5, 6, 7, 8}
print(s2, type(s2))

print("S3 - Une todos os elementos ")
s3 = s1 | s2
print(s3, type(s3))

print("S3 - apenas os elementos presentes nos dois  ")
s3 = s1 & s2
print(s3, type(s3))

print("S3 - Elementos que estão apenas no set da esquerda")
s3 = s1 - s2
print(s3, type(s3))

print("S3 - Elementos que estão nos dois mas nao em ambos ")
s3 = s1 ^ s2
print(s3, type(s3))
