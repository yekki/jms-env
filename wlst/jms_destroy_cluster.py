if __name__ == '__main__': 
    from wlstModule import *#@UnusedWildImport
from common import *#@UnusedWildImport

connect(domain.username, domain.password, domain.url)

edit()
startEdit()

for server in jms_servers:
    cmo.destroyJMSServer(getMBean('/JMSServers/%s' % server))

cmo.destroyJMSSystemResource(getMBean('/JMSSystemResources/MyJMSResources'))

for store in file_stores.keys():
    cmo.destroyFileStore(getMBean('/FileStores/%s' % store))

try:
    save()
    activate(block="true")
    print "script returns SUCCESS"   
except Exception, e:
    print e 
    print "Error while trying to save and/or activate!!!"
    dumpStack()
    raise 
    
