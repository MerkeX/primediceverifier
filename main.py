#!/usr/bin/python

import hashlib
import hmac

server_seed = str(input("Insert server seed: "));  # <-- Your server seed
client_seed = str(input("Insert client seed: "));  # <-- Your client seed
nonce = str(input("Insert nonce: "));              # <-- Your nonce (nr of bets)

# Hexadecimal to decimal function
def hex2dec(number):
    return int(number,16);

def get_number(start_index,end_index,hex_string):
    string2convert="";
    for n in range(start_index,end_index+1):
        string2convert = string2convert+hex_string[n];
    return string2convert;
        
string2 = server_seed;
string1 = client_seed+"-"+nonce;
hex_string = hmac.new(string2.encode(),string1.encode(),hashlib.sha512).hexdigest();
i=0;
string2convert=get_number(i*5,i*5+4,hex_string);
while(1):
    if((i*5+4)>128):
        result = 99.99;
        break;
    dec_num = int(string2convert,16);
    if(dec_num > 999999):
        i+=1;
        string2convert = get_number(i*5,i*5+4,hex_string);
    else:
        break;
if((i*5+4)>128):
    result = 99.99;
    print("Your roll is:",result);
else:
    result = (dec_num % 10000)/100;
    print("Your roll is:",result);





    
