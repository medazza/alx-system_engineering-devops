# 0x05. Processes and Signals

## What is a PID?

A PID, or Process ID, is a unique numerical identifier assigned to each running process in a Unix-based operating system. PIDs are used to manage and control processes.

## What is a Process?

A process is a program in execution. It is an independent unit of work that can perform various tasks on a computer. Processes have their own memory space and system resources, allowing them to run concurrently.

## How to Find a Process' PID

To find a process's PID, you can use various command-line tools such as `ps` or `pgrep`. For example:

```shell
ps aux | grep process_name
```

Replace `process_name` with the name of the process you want to find. The PID will be listed in the output.

## How to Kill a Process

To terminate a process, you can use the `kill` command followed by the process's PID. For example:

```shell
kill PID
```

Replace `PID` with the actual Process ID of the process you want to terminate. You can also use the `-9` option to forcefully kill a process:

```shell
kill -9 PID
```

## What is a Signal?

A signal is a software interrupt delivered to a process. It can be used to notify a process to perform a specific action or to terminate gracefully.

## What are the 2 Signals that Cannot be Ignored?

There are two signals that cannot be ignored by a process:

1. **SIGKILL (9)**: This signal forces the immediate termination of a process. It cannot be caught or ignored, making it a powerful way to stop a misbehaving or unresponsive process.

2. **SIGSTOP (19 or 20)**: This signal suspends a process's execution temporarily. Like SIGKILL, it cannot be caught or ignored. You can resume a stopped process using the `fg` (foreground) or `bg` (background) commands.

These signals are typically used for critical actions when dealing with processes. It's important to use them judiciously, especially SIGKILL, as it can lead to data loss or corruption if used indiscriminately.

--DoHardThings