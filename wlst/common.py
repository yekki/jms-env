class Machine(object):
    name = ''
    ip = ''
    servers = {}
    
    def __init__(self, name, ip, servers):
        self.name = name
        self.ip = ip
        self.servers = servers

class Domain(object):
    username='weblogic'
    password='welcome1'
    address = 'localhost'
    port = ''
    name = ''
    path = ''
    url = ''
    
    def __init__(self, root, name, port='7001'):
        self.port = port
        self.name = name
        self.path = '%s/%s' % (root, name)
        self.url = 't3://%s:%s' % (self.address, self.port)

# common settings
cluster_name = 'MyCluster'
jms_res={'module_name':'MyJMSResources', 'cf_name':'MyCF', 'dqueue_name':'MyDQ', 'cf_jndi':'mycf', 'dqueue_jndi':'mydq'}
jms_servers = {'JMSServer':'FileStore',}


# for testing start
file_stores = {'FileStore':'/Users/gniu/Temp.localized/store',}
domain = Domain('/Users/gniu/Oracle/mw12c/user_projects/domains', 'jms_domain')
machines = (Machine('node1', 'localhost', {'MS1_1':7101, 'MS1_2':7102}),)
# for testing end

'''
file_stores = {'FileStore':'/u01/oracle/temp/store',}
domain = Domain('/u01/oracle/mw12c/user_projects/domains', 'jms_domain')
machines = (Machine('node1', '192.168.10.101', {'MS1_1':7101, 'MS1_2':7102}), Machine('node3', '192.168.10.103', {'MS3_1':7301, 'MS3_2':7302}), Machine('node4', '192.168.10.104', {'MS4_1':7401, 'MS4_2':7402}), Machine('node5', '192.168.10.105', {'MS5_1':7501, 'MS5_2':7502}))
'''

def message_box(msg):
    print ''
    print '============================================='
    print msg
    print '============================================='
    print ''