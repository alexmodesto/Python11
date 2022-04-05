"""def reverse(phrase):
    return ' '.join(list(map(lambda x: x[::-1], phrase.split())))

print(reverse("Mi perro Renzo"))
"""



patata = ' '.join([x[::-1] for x in ("Mi perro Renzo").split(' ')])
print(patata)
