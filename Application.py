import enum
import time
import os

from datetime import date
from datetime import datetime
import Utilities
import Filemanager
import Word

class APP_STATE(enum.IntEnum) :
    INIT     = 0,
    RUNING   = 10,
    EXIT_APP = 8

class MENU_OPC (enum.IntEnum) :
    PLAY     = 1,
    LST_ALL_TASKS   = 2,
    LST_IMP_TASKS   = 3,
    DELETE_TASK     = 4,
    LOAD_DATA       = 5,
    SAVE_DATA       = 6,
    WORK            = 7,
    QUIT            = 8,

class App :
    def __init__( self, Name="Unknow" ) :
        print("App Created")
        self.Name = Name
        self.state = APP_STATE.INIT
        self.myWords : Word = []        

    def Run ( self ):
        while self.state != APP_STATE.EXIT_APP : 
            if self.state == APP_STATE.INIT :
                # self.loadData()
                # print (self.Name)
                # print("Init :)")
                self.state =  APP_STATE.RUNING 
                continue

            if self.state == APP_STATE.RUNING :
                self.running()
                continue

            if self.state == APP_STATE.EXIT_APP :
                print("Exit")
                continue
        
    def running(self) :
        option = 0
        option = self.mainMenu()

        if option == MENU_OPC.CREATE_TASK:
            # self.createTask()
            self.play()
        
        if option == MENU_OPC.LST_ALL_TASKS:
            os.system("clear")
            self.printListTask( self.myTasks , "All Task")
            Utilities.waitForKey()
            os.system("clear")

        if option == MENU_OPC.LST_IMP_TASKS:
            pass

        if option == MENU_OPC.DELETE_TASK:
            pass

        if option == MENU_OPC.LOAD_DATA:
            self.loadData()
    
        if option == MENU_OPC.SAVE_DATA:
            self.saveData()

        if option == MENU_OPC.WORK:
            self.working()
            
        if option == MENU_OPC.QUIT:
            self.state = APP_STATE.EXIT_APP
            self.saveData()
    
    def mainMenu(self) : 
        opc = 0
        print(self.Name)
        print( " Main Menu " )
        print("(",MENU_OPC.PLAY  ,") Play")
        print("(",MENU_OPC.LST_ALL_TASKS,") List all tasks")
        print("(",MENU_OPC.LST_IMP_TASKS,") List important tasks")
        print("(",MENU_OPC.DELETE_TASK  ,") Delete")
        print("(",MENU_OPC.LOAD_DATA    ,") Load data")
        print("(",MENU_OPC.SAVE_DATA    ,") Save data")
        print("(",MENU_OPC.WORK         ,") Work")
        print("(",MENU_OPC.QUIT         ,") Quit")
        opc = input("[ Input ]:  " ); 

        return int(opc)

    def play( self ) :
        return
    
    def createTask( self ) :
        os.system("clear")
        print( "Create New Task" )
        t_name        = input( "Task Name   : " )
        t_description = input( "Description : " )
        print( "Importance:" )
        print( "[1]URG [2]PRI [3]OPT : ",end="")
        t_importance = input("")

        print( 'Are you sure to add this new task?')
        print( '[Y] Add ' )
        print( '[N] Discard ' )
        option_add = input('')
        if option_add == "Y" :
            pass
            # n_task = Word( t_name , t_description , t_importance, T_TYPE.TIMED, 0 , 0, 0 )
            # self.myTasks.append(n_task) 

    def printListTask( self, task , tableTitle ) :
        if (len(self.myTasks) == 0):
            print('Any task to show you!')
            return
        
        str_div = '-'
        maxLen  = 95

        numLen  = 5 
        nameLen = 15
        typeLen = 8
        descLen = 30
        impLen  = 15
        minLen  = 10
        isDLen  = 7

        print( tableTitle.center( maxLen ,' ') )
        print( str_div.center( maxLen ,'-'))
        print( "Num".center(numLen,' ') , end=''  )
        print( "Name".center(nameLen,' ') , end=''  )
        print( "Type".center(typeLen,' ') , end=''  )
        print( "Importance".center(impLen,' ') , end=''  )
        print( "Description".center(descLen,' ') , end=''  )
        print( "Min".center(minLen,' ') , end=''  )
        print( "isDone".center(isDLen,' ') )
        
        num = 1
        for  task in self.myTasks :
            if task.IsDone :
                taskColor = ''
            print( str_div.center( maxLen , '-' )  )
            
            print( str(num).center(numLen , ' ') , end=''  )
            if len (task.Name) > (nameLen -6) :
                print( task.Name[0:nameLen-6].center( nameLen , ' ') , end=''  )
            else:
                print( task.Name.center( nameLen , ' ') , end=''  )
            
            print( task.TaskTypeStr().center( typeLen , ' ') , end=''   )
            print( task.ImportanceStr().center( impLen , ' ') , end=''  )
            print( task.Description[0:descLen].center( descLen , ' ') , end=''  )
            print( str(f'{task.MinutesWorks:.1f}').center( minLen , ' ') , end=''  )
            print( str(task.IsDone).center( isDLen , ' ')  )
            num += 1
        print( str_div.center( maxLen , '-' ))

    def working( self ) :
        os.system("clear")
        if ( len(self.myTasks) == 0 ) :
            print('No task to work')
            return
        self.printListTask( self.myTasks , "All Task")
        print( "<< 0 >> salir")
        print( "What do you want to work on? ")
        numberToWork = int(input('-> : '))
        if numberToWork == 0 :
           return
    
        numberToWork -= 1
        currentTask = self.myTasks[ numberToWork ]
        os.system("clear")
        print( "You are working on: \n" )
        currentTask.printTask2()
 
        t1 = time.time()
        Utilities.waitForKey()
        t2 = time.time()
        seconds = t2 - t1
        minutes = Utilities.sec2min(seconds)
        # print(minutes)
        print(f'Your Work  for {minutes} [min]')
        currentTask.AppendMinutes(minutes)
        print('You done task?')
        print('[Y] Yes ')
        print('[N] NO ')
        is_done = input('')
        if is_done == 'Y' :
            currentTask.IsDone = True
        os.system("clear")
    
    def loadData( self ) : 
        os.system("clear")
        loadData = Filemanager.read_task_registers()
        if  loadData != None  and len(loadData) > 0:
            self.myTasks = loadData 
        else : 
            print('No data')
        return loadData

    def saveData ( self ) :
        os.system("clear")
        if ( len(self.myTasks) == 0) :
                print('NO hay tareas para guardar')
                return
        # tem = self.loadData()
        # if len(tem) >= len(self.myTasks) :
        #     print('el archivo tiene mas datos que los almacenados en memoria ')
        #     print('1.- Continuar')
        #     print('2.- Salir')
        #     desc = int(input(''))
        #     if int(desc) == 1 :
        #         Filemanager.write_task_registers(self.myTasks)
        #     else :
        #         print('No se ha guardado nada')
        Filemanager.write_task_registers(self.myTasks)

