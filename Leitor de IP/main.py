import fun
arq = open('rede.txt', 'r')

registros = arq.read().splitlines()

arq.close()

print()
fun.qtd_adptdrs(registros)
print()
fun.ipv4(registros)
print()
fun.ipv6(registros)
print()
fun.mask(registros)
print()