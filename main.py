import pygame, sys

class Termometro():
    def __init__(self):
        self.custom = pygame.image.load("images/termo1.png")
    
    def convertir(self, grados, toUnidad):
        resultado = 0
        if toUnidad == "F":
            resultado = grados * 9/5 + 32
        elif toUnidad == "C":
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
        return resultado
        

class Selector():
    __tipoUnidad = None
    def __init__(self, um = "C"):
        self.__customes = []
        self.__customes.append(pygame.image.load("images/posiF.png"))
        self.__customes.append(pygame.image.load("images/posiC.png"))
        self.__tipoUnidad = um
    
    def custom(self):
        if self.__tipoUnidad == "F":
            return self.__customes[0]
        elif self.__tipoUnidad == "C":
            return self.__customes[1]
    
    def change(self):
        if self.__tipoUnidad == "F":
            self.__tipoUnidad = "C"
        else:
            self.__tipoUnidad = "F"
    
    def unidad(self):
        return self.__tipoUnidad
        

class NumberInput():
    __value = 0
    __strValue = ""
    __position = [0, 0]
    __size = [0, 0]
    
    def __init__(self, value = 0):
        self.__font = pygame.font.SysFont("Arial", 24)
        self.value(value)
    
    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.unicode in '0123456789' and len(self.__strValue) < 10:
                self.__strValue += event.unicode
                self.value(self._strValue)
            elif event.key == pygame.K_BACKSPACE:
                self.__strValue = self.__strValue[0:-1]
                self.value(self._strValue)
    
    def render(self):
        textBlock = self.__font.render(self.__strValue, True, (74, 74, 74))
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size
        
        return {
            "fondo": rect,
            "texto": textBlock
            }
    
    def value(self, val = None):
        if val == None:
            return self.__value
        else:
            val = str(val)
            try:
                self.__value = int(val)
                self.__strValue = val
            except:
                pass

    def width(self, val = None):
        if val == None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(val)
            except:
                pass
    
    def height(self, val = None):
        if val == None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(val)
            except:
                pass
    
    def size(self, val = None):
        if val == None:
            return self.__size
        else:
            try:
                self.__size = [int(val[0]), int(val[1])]
            except:
                pass

    def posX(self, val = None):
        if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                pass
    
    def posY(self, val = None):
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass
    
    def pos(self, val = None):
        if val == None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]), int(val[1])]
            except:
                pass

class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termometro")
        self.__screen.fill((244, 236, 203))
        
        self.termometro = Termometro()
        self.entrada = NumberInput(15)
        self.entrada.pos((106, 58))
        self.entrada.size((133, 28))
        
        self.selector = Selector()
    
    def __on_close(self):
        pygame.quit()
        sys.exit()
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__on_close()
                self.entrada.on_event(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.change()
                    grados = self.entrada.value()
                    nuevaUnidad = self.selector.unidad()
                    temperatura = self.termometro.convertir(grados, nuevaUnidad)
                    self.entrada.value(int(temperatura))
            self.__screen.fill((244, 236, 203))            
            # pintar el termometro
            self.__screen.blit(self.termometro.custom, (50, 34))
            # pintar el cuadro de texto
            text = self.entrada.render()
            pygame.draw.rect(self.__screen, (255, 255,255), text["fondo"])
            self.__screen.blit(text["texto"], self.entrada.pos())
            # pintar el selector
            self.__screen.blit(self.selector.custom(), (112, 153))
            # refresh
            pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    app = mainApp()
    app.start()