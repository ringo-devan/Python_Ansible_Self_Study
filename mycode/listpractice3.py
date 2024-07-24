

def main():

    servers = [['ios', '1.1.1.1'], ['ios', '2.2.2.2'], ['ios-xr' , '3.3.3.3'], ['junos' , '4.4.4.4']]
    print(servers)
    print(servers[1])
    print(servers[-1][-1])

    servers.pop(2)
    print(servers)


if __name__ == "__main__":

            main()
