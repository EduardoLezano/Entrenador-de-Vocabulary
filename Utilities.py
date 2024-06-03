def waitForKey() :
    print("\nPress enter to continue ... ")
    input('')

def printPorcentage( porcentage ) :
    print( f"Progress: {0} %".format( porcentage))
    if(porcentage > 100) : porcentage = 100
    if(porcentage < 0)   :porcentage = 0
    count = porcentage/10
    print("[",end='')
    for i in range(count):
        print("=",end='')
    for i in range(count):
        print(".",end='')
    
    print("]",end='')


def sec2min( _sec) :
    sec = _sec
    min = 0
    while ( _sec >= 60 ) :
        min += 1
        sec -= 60
        if ( sec < 0 ) :
            break
    
    return min

def min2hours(  _min ) :    
    return (_min / 60.0)


def printCaraError( mensaje ):
    print(" ... ")
    print("(X X)  ")
    print("  U  ")