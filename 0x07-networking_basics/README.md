# 0x07. Networking Basics #0

## OSI Model

### What it is
The OSI (Open Systems Interconnection) Model is a conceptual framework used to understand how different networking protocols and technologies interact in a networked environment.

### How many layers it has
The OSI Model consists of seven layers, each with a specific function.

### How it is organized
The OSI Model is organized as follows:
1. Physical Layer
2. Data Link Layer
3. Network Layer
4. Transport Layer
5. Session Layer
6. Presentation Layer
7. Application Layer

## What is a LAN

### Typical usage
A LAN (Local Area Network) is a network of interconnected devices within a limited geographical area, such as a home, office, or campus. It is commonly used for local data sharing and resource sharing.

### Typical geographical size
LANs typically cover a small geographical area, such as a single building or a group of adjacent buildings.

## What is a WAN

### Typical usage
A WAN (Wide Area Network) is a network that spans a large geographical area, often connecting LANs or other networks over long distances. It is used for long-distance data communication and connectivity between geographically dispersed locations.

### Typical geographical size
WANs can cover vast geographical areas, ranging from a city to a global scale, connecting devices and networks across different regions or even continents.

## What is the Internet

### What is an IP address
An IP (Internet Protocol) address is a unique numerical label assigned to each device connected to a computer network. It is used for identifying and addressing devices on the Internet.

### What are the 2 types of IP address
There are two types of IP addresses: IPv4 (Internet Protocol version 4) and IPv6 (Internet Protocol version 6).

### What is localhost
"Localhost" refers to the loopback address 127.0.0.1, which points to the device itself. It is often used to test network applications on the local machine.

### What is a subnet
A subnet is a smaller network within a larger network. It allows for network segmentation and efficient management of IP addresses.

### Why IPv6 was created
IPv6 was created to address the exhaustion of available IPv4 addresses. IPv6 provides a larger address space and improved security features.

## TCP/UDP

### What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
The two main data transfer protocols for IP are TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).

### What is the main difference between TCP and UDP
The main difference between TCP and UDP is that TCP provides a reliable, connection-oriented communication with error checking and data retransmission, while UDP offers a connectionless, lightweight, and fast communication without error recovery.

### What is a port
A port is a logical endpoint for communication in a computer network. It allows multiple services or applications to run on the same device, each identified by a unique port number.

### Memorize SSH, HTTP, and HTTPS port numbers
- SSH (Secure Shell): Port 22
- HTTP (Hypertext Transfer Protocol): Port 80
- HTTPS (Hypertext Transfer Protocol Secure): Port 443

### What tool/protocol is often used to check if a device is connected to a network
The "Ping" tool and the ICMP (Internet Control Message Protocol) are often used to check if a device is connected to a network. Ping sends a network request to a target device and receives a response if the device is reachable.
