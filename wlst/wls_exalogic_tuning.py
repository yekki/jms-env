if __name__ == '__main__': 
    from wlstModule import *#@UnusedWildImport
from common import *#@UnusedWildImport

connect(domain.username, domain.password, domain.url)

edit()
startEdit()

cd('/')
cmo.setExalogicOptimizationsEnabled(true)
cmo.setProductionModeEnabled(true)

try:
    save()
    activate(block="true")
    print "script returns SUCCESS"   
except Exception, e:
    print e 
    print "Error while trying to save and/or activate!!!"
    dumpStack()
    raise 
    
