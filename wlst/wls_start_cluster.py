if __name__ == '__main__': 
    from wlstModule import *#@UnusedWildImport
from common import *#@UnusedWildImport

connect(domain.username, domain.password, domain.url)

domainRuntime()

message_box('Starting Cluster %s' % cluster_name)

try:
    start(cluster_name, 'Cluster')
except:
    message_box('Unable to start Cluster!!!')
    dumpStack()

disconnect()


