# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Import required modules/packages/library
import pexpect
ip_address = "192.168.56.101"
username = "prne"
password = "cisco123!"
password_enable = "class123!"
# Create the SSH session
session = pexpect.spawn('ssh ' + username + '@' + ip_address,
                        encoding='utf-8', timeout=20)
result = session.expect(['[password:', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result !=0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()
# Enter enable mode
session.sendline('enable')
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result !=0:
    print('--- Failure! entering enable mode')
    exit()
# Send enable password details
session.sendline(password_enable)
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result !=0:
    print('--- Faulure! entering enable mode after sending password')
    exit()
# Enter configuration mode
session.sendline('configure terminal')
result = session.expect([r'.\(config\)#', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result !=0:
    print ('--- Failure! entering config mode')
    exit()
# Change the hostname to R1
session.sendline('hostname R1')
result = session.expect([r'R1\(config\)#', pexpect.TIMEOUT, pexpect.EOF])
#Check for error, if exists then display error and exit
if result !=0:
    print('--- Failure! setting hostname')
# Exit config mode
session.sendline('exit')
# Exist enable mode
session.sendline('exit')
#Display a seuccess message if works
print('---------------------------------------')
print('')
print('--- Success! connecting to: ', ip_address)
print('---               username: ', username)
print('---               password: ', password)
print('')
print('_______________________________________')
# Terminate the SSH session
session.close()
#Save, run and verify application
#~/labs/prne$ python3 establish-a-ssh-connection.py

