if __name__ == '__main__': 
    from wlstModule import *#@UnusedWildImport
from common import *#@UnusedWildImport


def startAdminServer():
    try:
        nmStart('AdminServer')
    except:
        message_box('Unable to start AdminServer!!!')
        dumpStack()

message_box('Connecting to Node Manager...')

nmConnect(domain.username, domain.password, domain.address, 5556, domain.name, domain.path, 'Plain')

message_box('Connected to NODE MANAGER Successfully')
        
try:
    print 'Attempting to connect to AdminServer at URL %s' % domain.url
    connect(domain.username, domain.password, domain.url)
except:
    print 'Unable to connect to AdminServer, attempting to start'
    startAdminServer()
    connect(domain.username, domain.password, domain.url)


