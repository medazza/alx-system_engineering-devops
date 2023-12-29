# 0x08. Networking basics #1

## What is localhost/127.0.0.1

`localhost` or `127.0.0.1` is a loopback address that refers to your own computer. When you access `localhost`, you are connecting to your own machine, allowing you to test network-related services and applications locally.

## What is 0.0.0.0

`0.0.0.0` typically represents an invalid or unknown IP address. In networking, it can have different meanings depending on the context. For example, when used in the context of a server listening address, it usually means "listen on all available network interfaces" or "bind to all IP addresses."

## What is /etc/hosts

`/etc/hosts` is a system file on Unix-like operating systems that is used to map hostnames to IP addresses. It allows you to define custom hostnames and their corresponding IP addresses, effectively bypassing DNS resolution for those hostnames. This file is often used for local testing and configuration.

## How to display your machine’s active network interfaces

To display the active network interfaces on your machine, you can use various commands depending on your operating system:

### Linux and Unix-like Systems

You can use the `ifconfig` or `ip` command to display network interfaces. For example:

```bash
ifconfig
# or
ip addr
```

### Windows

You can use the `ipconfig` command in the Windows Command Prompt or PowerShell:

```cmd
ipconfig
```

These commands will provide information about your network interfaces, including their names, IP addresses, and other configuration details.