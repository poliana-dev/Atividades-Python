from turtle import Turtle


class minhaTartaruga(Turtle):
    __nome = " Maria Poliana"
    __matricula= "20211181110016"

    def __init__(self,cor):
        super().__init__("turtle")
        self.color(cor)
        self.penup()
        self.pendown()
        self.pensize(2)
        self.shape("turtle")
       

    def getNome(self):
        return self.__nome

    def getMatricula(self):
        return self.__matricula


    def desenharSapo(self):

        #ajustando posicao
        self.penup()
        self.goto(400,-100)
        
        self.pendown()

        #primeira parte do corpo
        self.circle(150,130)
        self.right(85)
        self.circle(45,190)
        self.right(73)
        self.circle(260,35)

        #segunda parte do corpo
        self.right(73)
        self.circle(45,190)
        self.right(85)
        self.circle(150,130)
        self.forward(70)

        #organizando 
        self.penup()
        self.forward(40)
        self.setx(250)
        self.sety(160)

        for olhos in range(2):
            self.color("black")
            self.begin_fill()
            self.circle(20,400)
            self.end_fill()
            self.penup()
            self.right(40)
            self.forward(220)

        self.back(385)
        self.color("green")
        self.pendown()
        self.right(50)
        self.circle(40,100)


    def desenharMariaPoliana(self):
        self.penup()
        self.goto(-600,200)
        self.right(139)
        self.pensize(3)

        def m():
            self.pendown()
            self.forward(70)
            self.back(70)
            self.left(40)

            for linha in range(2):
                self.forward(40)
                self.left(94)

            self.left(132)
            self.forward(70)
        
        def a():
            self.pendown()
            self.circle(20,400)
            self.penup()
            self.left(50)
            self.forward(35)
            self.right(90)
            self.pendown()
            self.back(35)
            self.forward(40)

        def r():
            self.pendown()
            self.back(45)
            self.forward(20)
            self.circle(13,-150)

        def i():
            self.pendown()
            self.fd(8)
            self.back(40)

        def p():
            self.pendown()
            self.back(70)
            self.forward(20)
            self.circle(23,400)

        def o():
            self.down()
            self.circle(20,400)

        def l():
            self.down()
            self.fd(65)

        def n():
            self.down()
            self.back(50)
            self.forward(20)
            self.circle(13,-160)
            self.rt(200)
            self.fd(36)
        


            
        #escrevendo na tela        
        m()
        self.penup()
        self.sety(145)
        self.setx(-530)
        a()
        self.penup()
        self.setx(-470)
        r()
        self.penup()
        self.setx(-430)
        self.rt(30)
        i()
        self.up()
        self.setx(-410)
        self.sety(146)
        self.right(180)
        a()
        self.up()
        self.setx(-300)

        p()
        self.up()
        self.setx(-250)
        self.sety(131)
        o()
        self.up()
        self.setx(-200)
        self.lt(100)
        l()
        self.up()
        self.setx(-180)
        self.sety(155)
        i()
        self.up()
        self.setx(-160)
        self.sety(140)
        self.rt(180)
        a()
        self.up()
        self.setx(-100)
        n()
        self.up()
        self.setx(-60)
        self.sety(140)
        a()



    


poli= minhaTartaruga("green")
poli.desenharSapo()
poli.desenharMariaPoliana()