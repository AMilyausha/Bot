import view as dt
import model as log
#сохранить данные
def Data_view():
    data = dt.get_Data()
    log.Data_csv(data)
    return data
# открыть файл

def menu_sel():
    while True:
        ch = dt.menu()
        match ch:
            case 1:
                log.openn()   
            case 2:
                Data_view()
            case 3:
                searchcontact()
            case 4:
                print ()
            case 5:
                break
 # поиск контакта
def searchcontact(): 
    searchname = input( "Введите данные абонента: ")  
    firstchar = searchname[0] 
    searchname = firstchar.upper()
    myfile = open ('log.csv', 'r')
    filecontents = myfile.readlines() 
      
    found = False 
    for line in filecontents: 
        if searchname in line: 
            print( "Данные абонента:", end = " ") 
            print( line) 
            found = True 
            break 
    if found == False: 
        print( "По заданным данным абонент не найден", searchname) 

def init():
    menu_sel()

