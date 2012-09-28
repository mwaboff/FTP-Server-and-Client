####################
#
#    File Transfer Protocol Server & Client
#    CPS375 Project
#
#    Michael Aboff
#    mwaboff (at) gmail.com
#
####################

This was a project written for CPS375 (Computer Networking).

The goal of the project was to create a simple FTP process where a client
would connect to a server, request a file, and download the file from 
the server process.

To Use:

Start the server with the command:
    python FTP_Server.py
    
Run the client with the following command:
    python FTP_Client.py
    
The client will prompt for a file name. If the file exists, the server 
transmits the file to the client. The client writes the file data to a 
file titled "boff_ftp_success!.txt".
