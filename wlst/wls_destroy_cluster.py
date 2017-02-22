if __name__ == '__main__': 
    from wlstModule import *#@UnusedWildImport

from common import *#@UnusedWildImport

def removeServer(name):
    sbean = getMBean('/Servers/%s' % name)
    cd('/Servers/%s' % name)
    cmo.setCluster(None)
    cmo.setMachine(None)
    editService.getConfigurationManager().removeReferencesToBean(sbean)
    cd('/')
    cmo.destroyServer(sbean)

def removeMachine(name):
    mbean = getMBean('/Machines/%s' % name)
    editService.getConfigurationManager().removeReferencesToBean(mbean)
    cmo.destroyMachine(mbean)
    

def removeCluster(name):
    cbean = getMBean('/Clusters/%s' % name)
    editService.getConfigurationManager().removeReferencesToBean(cbean)
    cmo.destroyCluster(cbean)

connect(domain.username, domain.password, domain.url)

edit()
startEdit()

for machine in machines:
    for server in machine.servers.keys():
        removeServer(server)

for m in machines:
    removeMachine(m.name)
    
removeCluster(cluster_name)

try:
    save()
    activate(block="true")
    print "script returns SUCCESS"   
except Exception, e:
    print e 
    print "Error while trying to save and/or activate!!!"
    dumpStack()
    raise 
    
