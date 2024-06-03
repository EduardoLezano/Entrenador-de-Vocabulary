tryTimes = 3
nWords   = 3

class Game :
    def __init__(self,
                 _lan1,
                 _lan2) -> None:
        
        lang1 = _lan1
        lang2 = _lan2
        listWords = []
        self.tryTimes = tryTimes
        self.numWords = nWords

        

    def Verificar( self ) :
        pass

    def PrintWord( self , word ) :
        print(f'[{self.lan1}] : {word}')
        print(f'[{self.lan2}] : ')


    def CreateGame( self ) :
        pass

    def PLay( self ) :
        self.CreateGame()
        
        for w in range( self.numWords ):
            for t in range( self.tryTimes ) :
                self.PrintWord(self.listWords[w])
                