# Assignment 2A - Launch Notepad with WMI
# Name: Miroslav Stojanovic
# Week 2 Project
#
# This code shows how python can use WMI (Windows Management Instrumentation)
# to start a program. In this case, we are just opening Notepad as an example.
# In real life, malware could use this trick to run something harmful,
# but here it is safe since Notepad is harmless.

import wmi   # import the wmi module so we can talk to Windows

# make a connection to WMI on my computer
c = wmi.WMI()

# try to create a new process (open notepad.exe)
process_id, result = c.Win32_Process.Create(CommandLine="notepad.exe")

# check if it worked (0 means success)
if result == 0:
    print("Notepad opened! Process ID is:", process_id)
else:
    print("Something went wrong. Error code:", result)