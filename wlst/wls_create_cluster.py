if __name__ == '__main__': 
    from wlstModule import *#@UnusedWildImport

from common import *#@UnusedWildImport

def createManagedServers(machine, machine_bean):
    for m, lp in machine.servers.items():
        cd('/')
        print 'creating managed server %s' % m
        managedServer = create(m,'Server')
        managedServer.setListenAddress(machine.ip)
        managedServer.setListenPort(lp)
        managedServer.setCluster(cluster)
        managedServer.setMachine(machine_bean)

def createNodeMachine(machine):
    cd('/')
    print 'creating machine %s' % machine.name
    machine_bean = cmo.createMachine(machine.name)
    cd('/Machines/' + machine.name + '/NodeManager/' + machine.name)
    cmo.setNMType('Plain')
    cmo.setListenAddress(machine.ip)
    cmo.setListenPort(5556)
    cmo.setDebugEnabled(false)
    return machine_bean

connect(domain.username, domain.password, domain.url)

edit()
startEdit()

print 'creating cluster %s' % cluster_name
cluster = create(cluster_name,'Cluster')

for machine in machines:
    machine_bean = createNodeMachine(machine)
    createManagedServers(machine, machine_bean)

try:
    save()
    activate(block="true")
    print "script returns SUCCESS"   
except Exception, e:
    print e 
    print "Error while trying to save and/or activate!!!"
    dumpStack()
    raise 
    
