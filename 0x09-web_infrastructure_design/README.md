# 0x09. Web Infrastructure Design

This readme file provides an overview of various components related to web infrastructure design.

## DNS (Domain Name System)

The Domain Name System is a fundamental part of the internet that translates human-friendly domain names into IP addresses. DNS is essential for directing traffic to the correct web servers and ensuring the proper functioning of your web services.

## How DNS (Domain Name System) Works

DNS, which stands for Domain Name System, is a hierarchical and distributed system that translates human-friendly domain names (like www.example.com) into IP addresses (like 192.0.2.1) that computers and network devices use to locate each other on the internet. Understanding how DNS works involves breaking down the process into several key components and steps.

## DNS Hierarchy

The DNS system is organized hierarchically, with a global network of servers that collectively manage the domain name space. The top-level of this hierarchy includes the root DNS servers, which have information about the top-level domains (TLDs) like .com, .org, .net, and country-code TLDs like .uk, .ca, and .jp.

### DNS Records

DNS is essentially a distributed database, and the information it contains is stored in records. The most common DNS record types include:

- **A Record (Address Record):** Maps a domain name to an IPv4 address.
- **AAAA Record (IPv6 Address Record):** Maps a domain name to an IPv6 address.
- **CNAME (Canonical Name) Record:** Maps an alias or subdomain to another domain's canonical name.
- **MX (Mail Exchange) Record:** Specifies mail servers responsible for receiving email on behalf of a domain.
- **TXT (Text) Record:** Allows arbitrary text to be associated with a domain.

### Resolving DNS Queries

When you type a domain name into your web browser (e.g., www.example.com) and hit Enter, your computer needs to resolve that domain into an IP address. Here's how it works:

1. **Local DNS Cache:** Your computer checks its local DNS cache to see if it has a recent record of the domain and its corresponding IP address. If it finds a match, it can skip the rest of the resolution process.

2. **Local DNS Resolver:** If the cache doesn't have the needed information, your computer contacts a local DNS resolver, often provided by your Internet Service Provider (ISP) or configured manually. This resolver acts as an intermediary between your device and the DNS system.

3. **Root DNS Servers:** If the local DNS resolver doesn't have the requested information, it contacts one of the 13 root DNS servers distributed worldwide. These servers are responsible for knowing the IP addresses of the authoritative DNS servers for top-level domains (TLDs).

4. **TLD DNS Servers:** The root DNS server directs the resolver to the TLD DNS server associated with the TLD of the domain in question (e.g., .com, .org). The TLD server knows the authoritative name servers for that specific TLD.

5. **Authoritative Name Servers:** The TLD DNS server forwards the query to the authoritative name servers for the domain (e.g., example.com). These authoritative name servers contain the specific DNS records for that domain.

6. **Response:** The authoritative name servers provide the IP address of the requested domain back to the local DNS resolver.

7. **Caching and Response:** The local DNS resolver caches this information for a certain period (the Time to Live or TTL value) and sends the resolved IP address back to your computer. Your computer caches this information as well, so it doesn't have to repeat the process for subsequent requests to the same domain.

### Time to Live (TTL)

DNS records include a TTL value, which specifies how long the information should be considered valid. Once the TTL expires, the local DNS resolver will requery the authoritative name servers for the domain to get the most up-to-date information.

### Record Propagation

When DNS records change (e.g., when a website's hosting provider changes, resulting in a new IP address), the updated information is propagated through the DNS system. This propagation can take time due to the TTL values set for the records and the DNS resolver's caching.


## Monitoring

Monitoring is a critical aspect of web infrastructure design. It involves tracking the performance, availability, and security of your servers and services. Monitoring tools and practices help you detect and respond to issues proactively, ensuring the reliability of your web infrastructure.

## Web Server

Web servers are software or hardware components that receive and respond to client requests over the internet. They play a central role in serving web content, such as HTML pages, images, and other resources, to users' web browsers.

## Network Basics

Understanding network basics is crucial for web infrastructure design. This includes knowledge of TCP/IP, subnets, routers, firewalls, and network protocols. A strong grasp of networking concepts is essential for managing the flow of data in your infrastructure.

## Load Balancer

Load balancers distribute incoming web traffic across multiple servers to ensure optimal resource utilization and redundancy. They play a key role in improving performance and high availability of web services.

## Server

Servers are the backbone of web infrastructure, hosting applications, databases, and web content. Managing server hardware and software is essential for ensuring the reliability and performance of your web services.
