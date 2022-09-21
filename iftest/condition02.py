#!/usr/bin/env python3

# Check hostname against expected value
def main():
    ## Collect input from user
    hostname = input("What value should we set for hostname?")

    ## userse the lower method to test if input value matches expected value
    if hostname.lower() == "mtg":
        print("The hostname was found to be mtg")
        print("hostname matches expected config")

        ## Always print out to the user
    print("Exiting the script")
main()
