'''secure password checker uses api to get the hash list then comes it offline   git:PrakashDanabal'''


import requests
import hashlib



def checkpwd(res_hash,pwdhash):
    passlist=[]
    for line in res_hash:
        res_pass,res_time=line.split(':')
        if(res_pass==pwdhash[5:]):
            return res_time
    return 0
    

def password_check(passwd):
    #passwd=input('Please enter your password: ')
    passwd=passwd.encode(encoding='UTF-8')
    pass_hash=hashlib.sha1(passwd)
    passwd=pass_hash.hexdigest()
    passwd=passwd.upper()
    url='https://api.pwnedpasswords.com/range/'+passwd[:5]
    api_res=requests.get(url)
    res_hash=api_res.text
    res_hash=res_hash.split('\n')
    if(api_res.status_code==200):
        is_safe=checkpwd(res_hash,passwd)
        if is_safe:
            return 'red'
        else:
            return 'green'
    else:
        return ('API error kindly try later or contact admin')

#Test script
if __name__=='__main__':
    result=password_check(input('Please enter Password: '))
    if result=='green':
        print('Hard Password')
    elif result=='red':
        print('Weak Password')
    else:
        print (result)