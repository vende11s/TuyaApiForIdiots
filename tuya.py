import os
import argparse

IP = ""
ID = ""
KEY = ""
PROTOCOL_VERSION = "3.3"

parser = argparse.ArgumentParser()

parser.add_argument('--on', help="turns light on", required=False, action='store_true')
parser.add_argument('--off', help="turns light off", required=False, action='store_true')
parser.add_argument('--bright','-b', help="sets bright of the light, <1-100>", required=False, type=int)
parser.add_argument('-w', '--warm', help="sets warmness level for white color, <0-1000>", required=False, type=int)
parser.add_argument('-c', '--color', help="sets color to: white, red, blue, green, pink", required=False, type=str)
parser.add_argument('-k', '--key', help="you can specify key here, useful when you use more than one bulb", required=False, type=str)

args = parser.parse_args()

if args.key != None:
    KEY = args.key

if args.on:
    os.system("tuya-cli set --ip %s --id %s --key %s --protocol-version %s --dps 20 --set true" % (IP, ID, KEY,PROTOCOL_VERSION))

if args.off:
    os.system("tuya-cli set --ip %s --id %s --key %s --protocol-version %s --dps 20 --set false" % (IP, ID, KEY,PROTOCOL_VERSION))
    
if args.bright != None:
    if args.bright < 1:
        print("for bright you can use only values <1-100>")
        quit()
    os.system("tuya-cli set --ip %s --id %s --key %s --protocol-version %s --dps 22 --set %d" % (IP, ID, KEY,PROTOCOL_VERSION, args.bright*10))

if args.warm != None:
    os.system("tuya-cli set --ip %s --id %s --key %s --protocol-version %s --dps 23 --set %d" % (IP, ID, KEY,PROTOCOL_VERSION, args.warm))

def setColor(color):
    if color == "white":
        os.system("tuya-cli set --ip %s --id %s --key %s --protocol-version %s --dps 21 --set white" % (IP, ID, KEY,PROTOCOL_VERSION))
        return
    #those hex values are hsv color but hue goes normally, and saturation/value goes from 10-1000
    colors = {
        "red" : "016803e803e8",
        "blue" : "00F003e803e8",
        "green" :  "007303e803e8",
        "pink" :  "012c03e803e8"
    }

    if color not in colors:
        print("not supported color")
        return
        
    os.system("tuya-cli set --ip %s --id %s --key %s --protocol-version %s --dps 21 --set colour" % (IP, ID, KEY,PROTOCOL_VERSION))
    os.system("tuya-cli set --ip %s --id %s --key %s --protocol-version %s --dps 24 --set %s" % (IP, ID, KEY,PROTOCOL_VERSION, colors.get(color)))

if args.color != None:
    setColor(args.color)


