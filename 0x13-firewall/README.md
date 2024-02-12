# 0x13. Firewall

## Introduction

A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. It acts as a barrier between a trusted internal network and untrusted external networks, managing and filtering traffic based on a defined set of rules.

## Types of Firewalls

### 1. Packet Filtering Firewalls

Packet filtering firewalls examine packets of data and make decisions to allow or block them based on predefined rules. These rules are typically based on source and destination IP addresses, ports, and protocols.

### 2. Stateful Inspection Firewalls

Stateful inspection firewalls not only examine individual packets but also keep track of the state of active connections. They make decisions based on the context of the traffic, helping prevent certain types of attacks.

### 3. Proxy Firewalls

Proxy firewalls act as intermediaries between internal and external networks. They forward requests and responses between clients and servers, allowing for additional security measures and hiding internal network details.

### 4. Application Layer Firewalls

Application layer firewalls operate at the application layer of the OSI model, inspecting and controlling traffic based on specific applications or services. They provide granular control and are effective in protecting against application-level attacks.

## Types of Firewalls Based on Deployment

### 1. Network-based Firewall

Operates at the network layer and is typically deployed at the perimeter of a network to monitor and control incoming and outgoing traffic.

### 2. Host-based Firewall

Operates at the individual device level (host) and is installed on each computer or server. It monitors and controls traffic on a per-device basis, providing an additional layer of defense beyond the network-based firewall.

## Main Function of a Firewall

The main function of a firewall is:

- **To filter incoming and outgoing network traffic**

A firewall's primary role is to monitor and control network traffic based on specific security rules. It acts as a barrier to unauthorized access and cyber threats, ensuring the security of a network environment.

## Using Firewalls with ufw

The Uncomplicated Firewall (ufw) is a user-friendly interface for managing iptables, the default firewall management tool on many Linux distributions.

### Installing ufw

To install ufw on a Debian-based system, use the following commands:

```bash
sudo apt-get update
sudo apt-get install ufw
```

### Verifying ufw Status

To verify the status and rules of ufw, use:

```bash
sudo ufw status
```
## Conclusion

Firewalls are essential components of network security, providing a first line of defense against unauthorized access and cyber threats. Understanding the different types of firewalls and how to configure them contributes to creating a more secure network environment.

## Author
* **AZZA MOHAMED** [AZZA](https://github.com/medazza)- ALX-Africa SE Student cohort 17
