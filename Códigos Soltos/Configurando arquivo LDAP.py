from django.conf import settings
import ldap3
import logging
from ldap3 import Server, Connection, SUBTREE, ALL_ATTRIBUTES

# Configuração do logger
logger = logging.getLogger(__name__)

LDAP_IP_SERVER = 'COLOQUE O IP DO LDAP' #Este é o endereço IP do servidor LDAP.
LDAP_DOMAIN_NAME = 'COLOQUE O DOMINIO' #Este é o nome de domínio do servidor LDAP

# Script para procurar em uma coluna e subtituir na coluna do lado

# Carregar a planilha de consulta
consulta_df = pd.read_excel('Resultado.xlsx', sheet_name='Planilha1')

# Carregar a planilha de resultado (vazia inicialmente)
resultado_df = pd.read_excel('dados filtrados.xlsx', sheet_name='42365')
N = 0

# Verificar o cadastro do usuário na planilha de consulta
for index, row in consulta_df.iterrows():
    usuario = row.iloc[0]  # Primeira coluna da planilha de consulta (usuário)
    dado = row.iloc[7]     # Oitava coluna da planilha de consulta (dado a ser copiado)
    
    # Verifica se o usuário está na planilha de resultado
    if usuario in resultado_df.iloc[:, 0].values:
        # Encontra o índice onde o usuário está na planilha de resultado
        idx = resultado_df.index[resultado_df.iloc[:, 0] == usuario][0]
        
        # Copia o dado da 5ª coluna da planilha de consulta para a 5ª coluna da planilha de resultado
        resultado_df.iloc[idx, 7] = dado
        print(f"Encontrei e alterei {N}")
        N += 1

# Salvar a planilha de resultado atualizada
resultado_df.to_excel('dados filtrados.xlsx', index=False)




def autenticar(username, password):
    ldap_server = 'COLOQUE O IP DO LDAP'                         #settings.LDAP_IP_SERVER
    ldap_domain = 'COLOQUE O DOMINIO'                              #settings.LDAP_DOMAIN_NAME
    
    ldap_base_dn = "OU=Usuarios,DC={},DC=local".format(ldap_domain)

    logger.warning("Tentativa de autenticação para o usuário: {}".format(username))

    try:
        # Conecta-se ao servidor LDAP
        server = ldap3.Server('ldap://' + ldap_server)
        conn = ldap3.Connection(server, user='{}\\{}'.format(ldap_domain, username), password=password, authentication=ldap3.SIMPLE)

        # Tenta conectar
        if conn.bind():
            # Realiza uma pesquisa LDAP para obter os atributos do usuário
            conn.search(search_base=ldap_base_dn, search_filter='(sAMAccountName={})'.format(username), search_scope=SUBTREE, attributes=['displayName', 'physicalDeliveryOfficeName'])

            
            if len(conn.entries) == 1:
                # Recupera o nome completo do usuário da entrada LDAP
                full_name = conn.entries[0]['displayName'].value
                cpf = conn.entries[0]['physicalDeliveryOfficeName'].value
    

                logger.warning("Autenticação bem-sucedida para o usuário: {}".format(username))
                return full_name, cpf
            else:
                logger.warning("Usuário não encontrado ou múltiplos usuários correspondentes.")
                return False
        else:
            logger.warning("Falha na conexão com o servidor LDAP.")
            return False

    except ldap3.core.exceptions.LDAPInvalidCredentialsResult as e:
        # Credenciais inválidas
        logger.warning("Credenciais inválidas para o usuário {}: {}".format(username, e))
        return False
    except Exception as ex:
        # Outras exceções
        logger.warning("Erro durante a autenticação para o usuário {}: {}".format(username, ex))
        return False
    finally:
        conn.unbind()
