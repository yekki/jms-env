## Environment
- WebLogic Server: 12.2.1.2.0
- Hardware: Exalogic x5-2
- JDK: 1.8.0_121

## IP Addresses

### My Laptop

- IP: 10.153.236.48
- Mask: 255.255.255.128
- Gateway: 10.153.236.1

### Node 1

- 172.32.226.161
- 192.168.10.101

### Node 2

- 172.32.226.164
- 192.168.10.104

### Node 3

- 172.32.226.163
- 192.168.10.103

### Node 4

- 172.32.226.164
- 192.168.10.104

### Node 5

- 172.32.226.165
- 192.168.10.105

### Node 6

- 172.32.226.166
- 192.168.10.106

### Node 7

- 172.32.226.167
- 192.168.10.107

### Node 8

- 152.55.228.247
- 172.32.226.168
- 192.168.10.108

### Provider URL
- 4-Nodes

```
t3://192.168.10.101:7101,192.168.10.101:7102,192.168.10.103:7301,192.168.10.103:7302,192.168.10.104:7401,192.168.10.104:7402,192.168.10.107:7701,192.168.10.107:7702
```

- 2-Nodes

```
t3://192.168.10.103:7301,192.168.10.103:7302,192.168.10.104:7401,192.168.10.104:7402
```

## IP Forward

### 1. Modify .ssh/config add following content:
	
```
Host wls
    User root
    HostName    152.55.228.247
    IdentityFile ~/.ssh/id_rsa
```

### 2. Startup forward
	
	ssh -CfNg -L 7001:172.32.226.163:7001 wls
	ssh -CfNg -L 2222:172.32.226.163:22 wls
	ssh -CfNg -L 5556:172.32.226.163:5556 wls
## Paths

- /u01/oracle/mw12c/user_projects/domains/jms_domain/bin
- /home/oracle/emagent/agent_inst/bin
- /u01/oracle/scripts/samples/
- /u01/oracle/temp/store

	

