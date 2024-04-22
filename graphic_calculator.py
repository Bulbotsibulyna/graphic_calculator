from tkinter import*
import math

tx = 0
a = ''
tk = Tk()
c = Canvas(tk, width = 500, height = 20)
c.grid()


def cre1():
    global tx
    global a
    global i
    tx = tx + 10
    c.create_text(tx, 10, text = '1', font = ('Times', 10))
    a = a + '1'

def cre2():
    global tx
    global a
    global i
    tx = tx + 10
    c.create_text(tx, 10, text = '2', font = ('Times', 10))
    a = a + '2'

def cre3():
    global tx
    global a
    global i
    tx = tx + 10
    c.create_text(tx, 10, text = '3', font = ('Times', 10))
    a = a + '3'

def cre4():
    global tx
    global a
    global i
    tx = tx + 10
    c.create_text(tx, 10, text = '4', font = ('Times', 10))
    a = a + '4'

def cre5():
    global tx
    global a
    global i
    tx = tx + 10
    c.create_text(tx, 10, text = '5', font = ('Times', 10))
    a = a + '5'

def cre6():
    global tx
    global a
    global i
    tx = tx + 10
    c.create_text(tx, 10, text = '6', font = ('Times', 10))
    a = a + '6'

def cre7():
    global tx
    global a
    global i
    tx = tx + 10
    c.create_text(tx, 10, text = '7', font = ('Times', 10))
    a = a + '7'


def cre8():
    global tx
    global a
    global i
    tx = tx + 10
    c.create_text(tx, 10, text = '8', font = ('Times', 10))
    a = a + '8'


def cre9():
    global tx
    global a
    global i
    tx = tx + 10
    c.create_text(tx, 10, text = '9', font = ('Times', 10))
    a = a + '9'

def cre0():
    global tx
    global a
    global i
    tx = tx + 10
    c.create_text(tx, 10, text = '0', font = ('Times', 10))
    a = a + '0'

def cremi():
    global tx
    global a
    global i
    tx = tx + 10
    c.create_text(tx, 10, text = '-', font = ('Times', 10))
    a = a + '-'

def cremn():
    global tx
    global a
    global i
    tx = tx + 10
    c.create_text(tx, 10, text = '*', font = ('Times', 10))
    a = a + '*'


def crepo():
    global tx
    global a
    global i
    tx = tx + 10
    c.create_text(tx, 10, text = '/', font = ('Times', 10))
    a = a + '/'

def crest():
    global tx
    global a
    global i
    tx = tx + 10
    c.create_text(tx, 10, text = '^', font = ('Times', 10))
    a = a + '**'

def crep():
    global tx
    global a
    global i
    tx = tx + 10
    c.create_text(tx, 10, text = '+', font = ('Times', 10))
    a = a + '+'

def cree():
    global tx
    global a
    global i
    tx = tx + 10
    c.create_text(tx, 10, text = ')', font = ('Times', 10))
    a = a + ')'

def cred():
    global tx
    global a
    global i
    tx = tx + 10
    c.create_text(tx, 10, text = '.', font = ('Times', 10))
    a = a + '.'

def cres():
    global tx
    global a
    global i
    tx = tx + 20
    c.create_text(tx, 10, text = 'sin( ', font = ('Times', 10))
    a = a + 'math.sin('
    tx = tx + 10

def crec():
    global tx
    global a
    global i
    tx = tx + 20
    c.create_text(tx, 10, text = 'cos( ', font = ('Times', 10))
    a = a + 'math.cos('
    tx = tx + 10

def cret():
    global tx
    global a
    global i
    tx = tx + 30
    c.create_text(tx, 10, text = 'tg( ', font = ('Times', 10))
    a = a + 'math.tan('
    tx = tx + 10

def crect():
    global tx
    global a
    global i
    tx = tx + 30
    c.create_text(tx, 10, text = 'ctg( ', font = ('Times', 10))
    a = a + 'math.cot('

def crex():
    global tx
    global a
    global i
    tx = tx + 10
    c.create_text(tx, 10, text = 'x', font = ('Times', 10))
    a = a + 'x'

def crem():
    global tx
    global a
    global i
    tx = tx + 30
    c.create_text(tx, 10, text = 'mod( ', font = ('Times', 10))
    a = a + 'abs('
    tx = tx + 10

def creq():
    global tx
    global a
    global i
    tx = tx + 30
    c.create_text(tx, 10, text = 'sqrt(', font = ('Times', 10))
    a = a + 'math.sqrt('
    tx = tx + 10


def draw():
    global a
    tk1 = Tk()
    c1 = Canvas(tk1, width = 500, height = 500)
    c1.pack()
    c1.create_line(0, 250, 500, 250)
    c1.create_line(250, 0, 250, 500)
    for i in range(0, 50):
        c1.create_line(i*10, 248, i*10, 253)
    for i in range(0, 50):
        c1.create_line(248, i*10, 253, i*10)
    x = -25
    while x < 25:
        y = eval(a) * -1
        c1.create_line(round(x*10 + 250) - 1, round(y*10 + 250), round(x*10 + 250), round(y*10 + 250))
        x += 0.001
 
empty_label = Label(c, text="", height=1)
empty_label.grid(row=0)


buttons = [
    ('1', cre1), ('2', cre2), ('3', cre3),
    ('4', cre4),  ('5', cre5), ('6', cre6),
    ('7', cre7), ('8', cre8),  ('9', cre9),
    ('0', cre0), ('+', crep), ('-', cremi), ('.', cred),
    ('*', cremn), ('/', crepo),('sin(', cres), ('cos(', crec), ('tg(', cret),
    ('ctg(', crect), (')', cree),
    ('mod(', crem), ('^', crest), 
    ('x', crex), ('DRAW', draw)
    ]

for i, (text, command) in enumerate(buttons):
    button = Button(c, text=text, command=command, width=5, height=2)
    button.grid(row=(i // 5) + 1, column=i % 5)
