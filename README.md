# Deadlock-Detection-and-Resolution
 This project implements a deadlock detection and resolution system for a multi-resource environment. It reads allocation, request, and available resource data from input files, verifies consistency, detects deadlocks, and, if no deadlock is found, provides a safe execution sequence for processes.
Consider a system that has N processes, and M resources, and each resource has multiple instances.
You are provided with the following input files: [samples are attached]

Allocation.csv	Represents the NxM allocation matrix.
Request.csv	Represents the NxM request matrix.
Available.csv	Represents the M available vector.

Your task is to:
Read the input files, and verify that the dimensions are consistent.
Detect whether or not there is a deadlock condition.
If the system is deadlocked, list the processes that are deadlocked.
If not, show a series of process executions that are possible without deadlock.

