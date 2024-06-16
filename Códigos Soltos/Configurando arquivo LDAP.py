from django.conf import settings
import ldap3
import logging
from ldap3 import Server, Connection, SUBTREE, ALL_ATTRIBUTES

# Configuração do logger
logger = logging.getLogger(__name__)

LDAP_IP_SERVER = 'COLOQUE O IP DO LDAP' #Este é o endereço IP do servidor LDAP.
LDAP_DOMAIN_NAME = 'COLOQUE O DOMINIO' #Este é o nome de domínio do servidor LDAP

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
