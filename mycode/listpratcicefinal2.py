
def main():
    
    network = []

    with open('ipdata.txt', 'r') as ipdata:
        for line in ipdata:
            line = line.rstrip("\n")
            network.append(line)
            print(line)

if __name__ == "__main__":
    main()
