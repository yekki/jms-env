## Environment
- WebLogic Server: 12.2.1.2.0
- Hardware: Exalogic x5-2
- JDK: 1.8.0_121

## IP Addresses

### My Laptop

- IP: 10.153.236.48
- Mask: 255.255.255.128
- Gateway: 10.153.236.1

### Node 8

- Bridge IP: 152.55.228.247
- Host IP: 172.32.226.168


### Node 3

- Host IP: 172.32.226.163

### Node 4

- Host IP: 172.32.226.164


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
	