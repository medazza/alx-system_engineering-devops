# 0x0C. Web Server

## Main Role of a Web Server

A web server plays a crucial role in serving and managing resources on the internet. Its primary functions include:

- **Handling HTTP Requests:** Web servers respond to client requests, typically in the form of HTTP (Hypertext Transfer Protocol) requests, by providing the requested resources, such as web pages, images, or files.

- **Processing Dynamic Content:** Web servers can handle dynamic content generation by interfacing with application servers (e.g., using CGI scripts, server-side scripting languages like PHP, or application server connectors).

- **Ensuring Security:** Web servers implement security measures to protect against common web-based attacks, such as DDoS attacks, SQL injection, and cross-site scripting (XSS).

## Child Process

A child process is a spawned instance of a program that is created by another process, known as the parent process. In the context of web servers:

- **Child Processes in Web Servers:** Web servers often use child processes to handle incoming requests. Each child process operates independently, managing a subset of client connections.

## Parent and Child Processes in Web Servers

Web servers typically adopt a parent-child process model for several reasons:

- **Concurrency:** Using multiple child processes allows a web server to handle multiple requests simultaneously, improving concurrency and responsiveness.

- **Fault Isolation:** Isolating client requests in separate child processes enhances fault tolerance. If one process fails, it doesn't affect others.

- **Resource Utilization:** Distributing incoming requests among multiple processes optimizes resource utilization and enhances overall server performance.

## Main HTTP Requests

The main HTTP (Hypertext Transfer Protocol) requests include:

- **GET:** Requests data from a specified resource.
- **POST:** Submits data to be processed to a specified resource.
- **PUT:** Updates a specified resource.
- **DELETE:** Deletes a specified resource.

# DNS (Domain Name System)

## What DNS Stands For

DNS stands for Domain Name System.

## DNS Main Role

The primary role of DNS is to translate human-readable domain names into IP addresses that computers use to identify each other on a network. It acts as a distributed database, mapping domain names to corresponding IP addresses.

# DNS Record Types

## A Record

- **Purpose:** Associates a domain name with an IPv4 address.

## CNAME Record

- **Purpose:** Specifies that a domain name is an alias for another domain, the "canonical" domain.

## TXT Record

- **Purpose:** Holds text information, often used for additional details like SPF records for email authentication.

## MX Record

- **Purpose:** Specifies mail servers responsible for receiving emails on behalf of the domain.

## Author
* **AZZA MOHAMED** [AZZA](https://github.com/medazza)- ALX-Africa SE Student cohort 17