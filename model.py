from datetime import datetime as dt

def Data_csv(data):
    with open ('log.csv', 'a',  encoding = 'utf-8') as file:
        file.write('{}\n'
                    .format(";".join(data)))
def openn():
    file = open ('log.csv', 'r',  encoding = 'utf-8')
    phone = file.read()
    print(phone) 
    file.close 

