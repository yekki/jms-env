if __name__ == '__main__': 
    from wlstModule import *#@UnusedWildImport
from common import *#@UnusedWildImport

connect(domain.username, domain.password, domain.url)

domainRuntime()

def deleteMessageFromDestination(server, module, jmsserver, destination):
    try:
        cd('ServerRuntimes/' + server + '/JMSRuntime/' + server + '.jms/JMSServers/' + jmsserver + '@' + server +'/Destinations/'+ module + '!' + jmsserver + '@' + server + '@' + destination)
    except:
        return 0
    amountOfDeletedMessages = cmo.deleteMessages('')
    return amountOfDeletedMessages

count = 0

for jserver in jms_servers.keys():
    for machine in machines:
        for wserver in machine.servers.keys():
            count += deleteMessageFromDestination(wserver, 'MyJMSResources', jserver, 'MyDQ')

message_box('deleted %d messages' % count)
    
disconnect()
