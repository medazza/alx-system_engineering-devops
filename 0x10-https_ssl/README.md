# 0x10. HTTPS SSL

## Overview

This README provides an in-depth explanation of HTTPS and SSL, focusing on the two main roles of SSL, the purpose of encrypting traffic, and the concept of SSL termination. Additionally, it includes guidance on using the `dig` command to check SSL-related information for a domain.

## HTTPS and SSL

### What is HTTPS?

HTTPS (Hypertext Transfer Protocol Secure) is a secure version of HTTP, the protocol used for transmitting data between a user's web browser and a website. It ensures that the data exchanged between the user and the website is encrypted and secure.

### SSL - Secure Sockets Layer

SSL (Secure Sockets Layer) is a protocol designed to secure communication over a computer network. It provides a secure connection between a client and a server, typically a web browser and a web server. SSL ensures that data transmitted between the two parties remains confidential and integral.

## Two Main Roles of SSL

1. **Authentication:**
   - SSL provides a mechanism for authenticating the identity of the server to the client and, optionally, the client to the server. This authentication helps establish trust between the parties involved in the communication.

2. **Encryption:**
   - SSL encrypts the data exchanged between the client and the server. This encryption prevents unauthorized parties from intercepting and understanding the transmitted information. It ensures the confidentiality and privacy of sensitive data.

## Purpose of Encrypting Traffic

The primary purpose of encrypting traffic using SSL is to enhance the security of data transmission over the internet. By encrypting data, SSL protects sensitive information such as login credentials, personal details, and financial transactions from being intercepted or tampered with by malicious actors.

Encrypting traffic with SSL provides the following benefits:

- **Confidentiality:** Ensures that only the intended recipient can decrypt and understand the transmitted data.
  
- **Integrity:** Guarantees that the data has not been altered or tampered with during transit.

## SSL Termination

SSL termination refers to the process of decrypting SSL-encrypted traffic at a particular point in the network. In the context of web servers, SSL termination often occurs at a load balancer or a reverse proxy before the traffic reaches the web servers. Once decrypted, the traffic continues its journey in an unencrypted form.

## Using `dig` Command for SSL Information

To check SSL-related information for a domain, you can use the `dig` command. For example:

```bash
dig +short TXT _acme-challenge.example.com
```

This command can provide information related to SSL certificate issuance and renewal, particularly when dealing with services like Let's Encrypt.

## Author
* **AZZA MOHAMED** [AZZA](https://github.com/medazza)- ALX-Africa SE Student cohort 17
