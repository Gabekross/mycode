#!/usr/bin/env python3

def main():
    #Creating a list containing three items 
    my_list = [ "192.168.0.5", 5060, "UP" ]
    #Display the first item in the list
    print("The first item in the list (IP): " + my_list[0] )
    #Display the seocnd item in the list;str is used to convert the integer to a string.
    print("The second item in the list (port): " + str(my_list[1]) )
    #Display the third item in the list
    print("The last item in the list (state): " + my_list[2] )
    #create a new list
    
    iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
    #display the IP addresses in the string
    print("The IP addressess are : " + iplist[3] + ",and " + iplist[4])
main()

