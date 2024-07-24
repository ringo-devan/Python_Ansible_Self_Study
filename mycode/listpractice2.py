

def main():

    interface = [ "192.168.0.5", 5060, "UP" ]
    # create a list called interface

    print("The first item in the list is(IP):", interface[0])
    
    print("The last item n the list is (State)", interface[-1])

    interface.append("Sip Phone Servers")
    print("Added SIP servers via .append" , interface[-1] )
    
    print(interface)


if __name__ == "__main__":
    main()
