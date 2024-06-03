class Word :
    def __init__(self) -> None:
        self.word = ""
        self.traslation = ""
        self.tras_sin : list[str]= []
        self.word_sin = []
        self.mening =  ""

    def PrintWord( self ) :
        print(self.word)
        print('================')
        print(self.mening)
        print('Traducciones similares')
        print(self.tras_sin)
        print('Sinonimos ')
        print(self.word_sin)



