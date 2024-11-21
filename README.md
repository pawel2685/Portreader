# Port Reader Project

A Python project to simulate and test serial port communication using Virtual Serial Port Emulator (VSPE) and Hercules. This project allows you to read data sent to a serial port (e.g., COM3) using a Python script.

---

## Table of Contents
- [Requirements](#requirements)
- [Setup](#setup)
  - [Configuring VSPE](#configuring-vspe)
  - [Setting up Hercules](#setting-up-hercules)
- [Running the Python Script](#running-the-python-script)
- [Testing Communication](#testing-communication)
- [References](#references)

---
## Setup
---
## Configuring VSPE
To create a virtual serial port (e.g., COM3):

#configuring-vspe
Install VSPE: Download and install VSPE. Run it as an administrator.
Create a Virtual Connector:
In VSPE, go to Device -> Create.
Select Device type: Virtual Connector and click Next.
Set the Port name to COM3 and click OK.
Verify:
In the main VSPE window, ensure that COM3 is listed and marked as Ready.

## Setting up Hercules
Setting up Hercules
Install Hercules: Download and install Hercules.
Configure Hercules:
Open Hercules and go to the Serial tab.
Set the Port to COM3.
Set the parameters:
Baud rate: 9600
Data bits: 8
Parity: None
Stop bits: 1
Flow control: None
Click Open to connect Hercules to COM3.
Send Data:
In the Send field, type any message (e.g., Hello from Hercules) and click Send.

## Testing Communication
Start Hercules:

Open Hercules, set the port to COM3, and click Open.
In the Send field, type a test message (e.g., Test message) and click Send.
Run the Python Script

Output:
Connected to port: COM3
Waiting for data (Press CTRL+C to exit)...
Received data: Test message

## Requirements

Before starting, ensure you have the following:
- Python (3.6+)
- Required Python libraries (install from `requirements.txt`):
  pip install -r requirements.txt

## References
Virtual Serial Port Emulator
https://eterlogic.com/products.vspe.html

Hercules
https://www.hw-group.com/software/hercules-setup-utility