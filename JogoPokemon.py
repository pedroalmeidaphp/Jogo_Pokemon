# Pedro Henrique de Almeida e Padua 
import random
import turtle

# Abrir uma janela
janela = turtle.Screen()
janela.title("Pokemon: Pikachu caça pokebolas ")
janela.bgpic('fd.gif')
janela.setup(800, 650)
janela.tracer(3, 20)

# Criandoacaneta
caneta = turtle.Turtle()
caneta.shapesize(3)
caneta.shape('arrow')
caneta.up()
caneta.pensize(10)
caneta.color('white')
caneta.speed(0)


# criando a area de jogo
def quadrado():
    caneta.goto(-300, -300)
    caneta.down()
    for i in range(4):
        caneta.forward(600)
        caneta.left(90)
    caneta.hideturtle()


quadrado()
# criando o jogador
p = turtle.Turtle()
janela.addshape('pika2.gif')
p.shape('pika2.gif')
p.shapesize(3)
p.left(90)
p.up()
# criando a inimigo(jiglypuff)
inimigo = turtle.Turtle()
janela.addshape('jp2.gif')
inimigo.shape('jp2.gif')
inimigo.up()
inimigo.setx(random.randint(-300, 300))
inimigo.setx(random.randint(-300, 300))
# criando vida(Pokebola)
vida = turtle.Turtle()
janela.addshape('poke2.gif')
vida.shape('poke2.gif')
vida.up()
# criando vidas
quantidadevida = 3

life1 = turtle.Turtle()
janela.addshape('raio.gif')
life1.speed(0)
life1.shape('raio.gif')
life1.up()
life1.ht()
life1.goto(-350, 0)
life1.st()
life2 = turtle.Turtle()
life2.speed(0)
life2.shape('raio.gif')
life2.up()
life2.ht()
life2.goto(-350, -45)
life2.st()
life3 = turtle.Turtle()
life3.speed(0)
life3.shape('raio.gif')
life3.up()
life3.ht()
life3.goto(-350, -90)
life3.st()
lifemsg = turtle.Turtle()
lifemsg.color("gold")
lifemsg.speed(0)
lifemsg.up()
lifemsg.ht()
lifemsg.goto(-350, 45)
lifemsg.down()
lifemsg.write("Vidas:", align="center", font=('Arial Black', 20))
poke = turtle.Turtle()
poke.speed(0)
poke.shape('poke2.gif')  # desenho pokebola do lado da pontuação
poke.up()
poke.ht()
poke.goto(-340, 288)
poke.st()

corrida_do_pikapika = 12  # velocidade do personagem(pikachu)


# movimentações personagem
def cima():
    global pontos
    global corrida_do_pikapika
    p.setheading(90)
    p.fd(corrida_do_pikapika)
    while p.ycor() > 300:
        if p.ycor() > 300:
            p.speed(0)
            p.sety(300)


def baixo():
    global pontos
    global corrida_do_pikapika
    p.setheading(270)
    p.fd(corrida_do_pikapika)
    while p.ycor() < -300:
        if p.ycor() < -300:
            p.speed(0)
            p.sety(-300)


def esquerda():
    global pontos
    global corrida_do_pikapika
    p.setheading(180)
    p.fd(corrida_do_pikapika)
    while p.xcor() < -300:
        if p.xcor() < -300:
            p.speed(0)
            p.setx(-300)


def direita():
    global pontos
    global corrida_do_pikapika
    p.setheading(0)
    p.fd(corrida_do_pikapika)
    while p.xcor() > 300:
        if p.xcor() > 300:
            p.speed(0)
            p.setx(300)


corrida_dopikapika = 15  # velocidade do inimigo e da vida
pontos = -1  # pontos do jogo


def andaebateinimi():
    global pontos
    global corrida_dopikapika
    inimigo.forward(corrida_dopikapika)
    if inimigo.xcor() > 300:
        inimigo.setheading(random.randint(90, 270))
    elif inimigo.xcor() < -300:
        inimigo.setheading([random.randint(0, 90), random.randint(270, 360)][random.randint(0, 1)])
    elif inimigo.ycor() > 300:
        inimigo.setheading(random.randint(180, 360))  # movimentação do inimigo
    elif inimigo.ycor() < -300:
        inimigo.setheading(random.randint(0, 180))
    janela.ontimer(andaebateinimi, 1000 // 24)
    difex = p.xcor() - inimigo.xcor()
    difey = p.ycor() - inimigo.ycor()
    if difex > -20 and difex < 20 and difey > -20 and difey < 20:
        global quantidadevida
        quantidadevida -= 1
        inimigo.setposition(random.randint(-300, 300), random.randint(-300, 300))
        if quantidadevida == 2:
            life1.ht()
        elif quantidadevida == 1:  # contagem de vida
            life2.ht()
        elif quantidadevida == 0:
            life3.ht()
            janela.bye()
        if pontos == 5:
            corrida_dopikapika = 17
        elif pontos == 10:
            corrida_dopikapika = 19
        elif pontos == 15:  # niveis de dificuladade de acordo com os pontos
            corrida_dopikapika = 21
        elif pontos == 20:
            corrida_dopikapika = 24


def andaebatevida():  # movimento da vida e contagem de pontos
    global pontos
    global corrida_dopikapika
    vida.forward(corrida_dopikapika)
    if vida.xcor() > 300:
        vida.setheading(random.randint(90, 270))
    elif vida.xcor() < -300:
        vida.setheading([random.randint(0, 90), random.randint(270, 360)][random.randint(0, 1)])
    elif vida.ycor() > 300:
        vida.setheading(random.randint(180, 360))  # movimento da vida
    elif vida.ycor() < -300:
        vida.setheading(random.randint(0, 180))
    janela.ontimer(andaebatevida, 1000 // 24)
    distanciax = p.xcor() - vida.xcor()
    distanciay = p.ycor() - vida.ycor()
    if distanciax > -20 and distanciax < 20 and distanciay > -20 and distanciay < 20:
        global pontos
        vida.goto(random.randint(-300, 300), random.randint(-300, 300))
        pontos += 1  # contagem de pontos
        contaPokebolasContador.clear()
        contaPokebolasContador.write((pontos), align="center", font=("Arial black", 24, "bold"))
    if pontos == 5:
        corrida_dopikapika = 17
    elif pontos == 10:
        corrida_dopikapika = 19  # NIVEIS DE DIFICULDADE
    elif pontos == 15:
        corrida_dopikapika = 21
    elif pontos == 20:
        corrida_dopikapika = 24


contaPokebolasCorpo = turtle.Turtle()
contaPokebolasCorpo.speed(0)
contaPokebolasCorpo.color('gold')
contaPokebolasCorpo.up()  # cria o texto "pokebolas:"
contaPokebolasCorpo.ht()
contaPokebolasCorpo.goto(-395, 300)
contaPokebolasCorpo.down()
contaPokebolasCorpo.write(('Pokebolas:'), align="left", font=('Arial Black', 15))

contaPokebolasContador = turtle.Turtle()
contaPokebolasContador.speed(0)
contaPokebolasContador.color('gold')
contaPokebolasContador.up()
contaPokebolasContador.ht()
contaPokebolasContador.goto(-380, 265)  # cria a contagem de pontos
contaPokebolasContador.down()
contaPokebolasContador.write((pontos), align="center", font=('Arial Black', 20))

andaebateinimi()
andaebatevida()
janela.onkeypress(cima, 'Up')
janela.onkeypress(baixo, 'Down')  # coordena as movimentações do personagem
janela.onkeypress(esquerda, "Left")
janela.onkeypress(direita, 'Right')
janela.listen()

# mantem a janela aberta
while True:
    janela.update()
