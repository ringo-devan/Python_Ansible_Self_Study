import json

def main():

    with open('ciscoAPIC.json', 'r') as jf:
        fog = json.load(jf)
        
        print(fog)
      
    print("the number of instances:", len(fog['imdata']))

    for instance in fog['imdata']:
        print("Firmware version running - ", instance.get('firmwareCtrlrRunning').get('attributes').get('version'))
        

if __name__ == "__main__":
    main()
