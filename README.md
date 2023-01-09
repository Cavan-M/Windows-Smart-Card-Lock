# Windows-Smart-Card-Lock
Automatically lock your PC when your SmartCard or Yubikey is removed. Allows users to bypass the Domain requirements for the SmartCard Removal Policy, in GroupPolicy

# Quickstart
Run the python file called "service.py" to force Windows to lock your PC when the SmartCard/Yubikey is removed.

Run the script using pyw.exe to run the script in windowless mode (comes with every python install)

Move the script to the startup folder to run the script on startup

# Dependencies
 - Python 3.X
 - pyscard
 - subproccess
 - time
