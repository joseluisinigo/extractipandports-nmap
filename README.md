# extractipandports-nmap
if you have many ips with ports in nmap format and you want only ip ports , you can use this script

This code is a Python script that extracts the IP addresses and open ports from an Nmap output file. Nmap is a popular network scanner used to map devices and services on a network. The Nmap output file contains detailed information about the scanned devices, including IP addresses and open ports.

The script starts by importing the "re" (regular expressions) library, which is used to search for patterns in the text. Then, the function "extract_ips_ports" is defined, which takes in the Nmap output file as a string, and uses regular expressions to search for the IP addresses and open ports.

The IP addresses are identified using the regular expression "Nmap scan report for (.*)", which searches for the string "Nmap scan report for" followed by any characters. The open ports are identified using the regular expression "^(\d+)", which searches for any digits at the beginning of a line. The script then creates a dictionary with the IP addresses as keys and the open ports as values.

The main function reads the Nmap output file and calls the "extract_ips_ports" function, passing the file's content as a string. The resulting dictionary is then written to an output file 'extract.txt' and printed on the console, in the format of IP followed by ports separated by comma.
