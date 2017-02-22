if __name__ == '__main__': 
    from wlstModule import *#@UnusedWildImport
from common import *#@UnusedWildImport

connect(domain.username, domain.password, domain.url)

edit()
startEdit()

# create file stores
for name, path in file_stores.items():
    print 'creating file store ' + name
    cd('/')
    cmo.createFileStore(name)
    cd('/FileStores/' + name)
    cmo.setDirectory(path)
    set('Targets',jarray.array([ObjectName('com.bea:Name=' + cluster_name +',Type=Cluster')], ObjectName))

# create jms servers

for name, fs in jms_servers.items():
    print 'creating jms server ' + name
    cd('/')
    cmo.createJMSServer(name)
    cd('/JMSServers/' + name)
    cmo.setPersistentStore(getMBean('/FileStores/' + fs))
    set('Targets',jarray.array([ObjectName('com.bea:Name=' + cluster_name +',Type=Cluster')], ObjectName))

# create jms resource
cd('/')
cmo.createJMSSystemResource(jms_res['module_name'])
cd('/JMSSystemResources/' + jms_res['module_name'])
set('Targets',jarray.array([ObjectName('com.bea:Name=' + cluster_name +',Type=Cluster')], ObjectName))


# create cf
cd('/JMSSystemResources/' + jms_res['module_name'] + '/JMSResource/' + jms_res['module_name'])
cmo.createConnectionFactory(jms_res['cf_name'])

cd('/JMSSystemResources/' + jms_res['module_name'] + '/JMSResource/' + jms_res['module_name'] + '/ConnectionFactories/' + jms_res['cf_name'])
cmo.setJNDIName(jms_res['cf_jndi'])
cmo.setDefaultTargetingEnabled(true)

cd('/JMSSystemResources/' + jms_res['module_name'] + '/JMSResource/' + jms_res['module_name'] + '/ConnectionFactories/' + jms_res['cf_name'] + '/SecurityParams/' + jms_res['cf_name'])
cmo.setAttachJMSXUserId(false)

cd('/JMSSystemResources/' + jms_res['module_name'] + '/JMSResource/' + jms_res['module_name'] + '/ConnectionFactories/' + jms_res['cf_name'] + '/ClientParams/' + jms_res['cf_name'])
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)

cd('/JMSSystemResources/' + jms_res['module_name'] + '/JMSResource/' + jms_res['module_name'] + '/ConnectionFactories/' + jms_res['cf_name'] + '/TransactionParams/' + jms_res['cf_name'])
cmo.setXAConnectionFactoryEnabled(false)

# create dq

cd('/JMSSystemResources/' + jms_res['module_name'] + '/JMSResource/' + jms_res['module_name'])
cmo.createUniformDistributedQueue(jms_res['dqueue_name'])

cd('/JMSSystemResources/' + jms_res['module_name'] + '/JMSResource/' + jms_res['module_name'] + '/UniformDistributedQueues/' + jms_res['dqueue_name'])
cmo.setJNDIName(jms_res['dqueue_jndi'])
cmo.setDefaultTargetingEnabled(true)


try:
    save()
    activate(block="true")
    print "script returns SUCCESS"   
except Exception, e:
    print e 
    print "Error while trying to save and/or activate!!!"
    dumpStack()
    raise 
    
