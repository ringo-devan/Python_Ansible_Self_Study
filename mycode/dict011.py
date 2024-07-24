
def main():
    switch = { 'hostname' : ' sw-1', 'ip' : '1.1.1.1', 'version' : '1.2', 'sequence' : [5,4,3,2,1]}
    print(switch['hostname'])
    print(switch['ip'])
    print(switch['sequence'])

    print("First Test of - .get()")
    print(switch.get('lynx'))

    print("Second Test of - .get()")
    print(switch.get('lynx', "The Key is in another castle"))
    
    print(switch)
    
    print( "dictionairy keys - .keys()")
    print(switch.keys())

    print( " dictionary value - .values()")
    print( switch.values())

    print("\n")

    print(switch)

    print(" - .pop()")
    switch.pop('sequence')
    
    print(switch)
    print('\n')

    print(" add a new value")
    switch['adminlogin'] = 'karlo8'

    print(switch)


if __name__ == "__main__":
    main()

