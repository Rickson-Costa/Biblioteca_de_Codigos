def ipv4 (arquivo):
    ips = []
    for i in range(len(arquivo)):
        if "IPv4" in arquivo[i]:
            dados = arquivo[i].split(': ')
            ips.append(dados[1])

    print(f'Os IPv4 encontrados foram: {ips}')

def qtd_adptdrs (arquivo):
    soma = 0
    nome = []
    for i in range(len(arquivo)):
        if "Adaptador" in arquivo[i]:
            soma += 1
            dados = arquivo[i].split("Adaptador ")
            nome.append(dados[1][:-1])


    print(f"Existem {soma} adaptadores de rede.", "\n")
    print(f'E os adaptadores encontrados foram: [{nome}]')

def ipv6 (arquivo):
    ips = []
    for i in range(len(arquivo)):
        if "IPv6" in arquivo[i]:
            dados = arquivo[i].split(': ')
            ips.append(dados[1])

    print(f'Os IPv6 encontrados foram: {ips}')


def mask (arquivo):
    mask = []
    for i in range(len(arquivo)):
        if "Sub-rede" in arquivo[i]:
            dados = arquivo[i].split(': ')
            mask.append(dados[1])

    print(f'As máscaras de sub-rede encontradas foram: {mask}')