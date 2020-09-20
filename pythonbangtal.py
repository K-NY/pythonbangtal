

from bangtal import  *

scene1 = Scene('룸1', 'Images/배경-3.png')  # 룸 1 배경

door1 = Object('Images/문-오른쪽-닫힘.png')
door1.locate(scene1,800,270)
door1.show()

desk = Object('Images/책상.png')
desk.setScale(0.3)
desk.locate(scene1,200,200)
desk.show()

paper = Object('Images/문제.png')
paper.setScale(0.05)
paper.locate(scene1,350,400)
paper.show()

key = Object('Images/열쇠.png')
key.setScale(0.4)
key.locate(scene1,300,280)

box = Object('Images/상자-닫힘.png')
box.setScale(0.2)
box.locate(scene1,200,50)
box.show()

keypad = Object('Images/키패드.png')
keypad.setScale(3)
keypad.locate(scene1,350,120)
keypad.show()

scene2 = Scene('룸2', 'Images/배경-2.png')  # 룸 2 배경

door2 = Object('Images/문-왼쪽-열림.png')
door2.locate(scene2,290,270)
door2.show()

vase = Object('Images/화분.png')
vase.locate(scene2,500,300)
vase.show()

paper2 = Object('Images/문제-2.png')
paper2.setScale(0.1)
paper2.locate(scene2,500,300)

keypad2 = Object('Images/키패드.png')
keypad2.setScale(4)
keypad2.locate(scene2,500,600)
keypad2.show()

switch = Object('Images/스위치.png')
switch.setScale(3)
switch.locate(scene2,970,450)

password = Object('Images/비밀번호.png')
password.setScale(2)
password.locate(scene2,400,50)

keypad3 = Object('Images/키패드.png')
keypad3.setScale(3)
keypad3.locate(scene2,970,400)

door3 = Object('Images/문-오른쪽-닫힘.png')  # 나가는 문
door3.locate(scene2,1100,240)


door1.closed = True
def door1_onMouseAction(x,y,action):  # 문을 열때
    if door1.closed :
        if key.inHand():
            door1.setImage('Images/문-오른쪽-열림.png')
            door1.closed = False
        else:
            showMessage('........문을 여는 열쇠가 필요할 것 같다.')
     
    else:
        scene2.enter()
door1.onMouseAction = door1_onMouseAction   


def door2_onMouseAction(x,y,action): # 룸 2에서 룸 1로 이동
    scene1.enter()  
door2.onMouseAction = door2_onMouseAction   


def paper_onMouseAction(x,y,action): # 종이를 주울때
    paper.pick()
    showMessage('종이 쪽지를 주웠다...! 글씨가 적혀있는것 같다...')
paper.onMouseAction = paper_onMouseAction


def key_onMouseAction(x,y,action):  # 키를 주울때
    key.pick()
key.onMouseAction = key_onMouseAction 


box.locked = True # 상자 잠금
box.closed = True # 상자 닫힘
def box_onMouseAction(x,y,action):
    if box.locked:   # 박스가 잠겨있음
         showMessage('상자가 잠겨있군... 암호를 풀어야 될것 같아.')

    elif box.closed:  # 암호 풀린 박스가 닫혀있음
         box.setImage('Images/상자-열림.png')
         key.show()
         showMessage('열쇠가 나왔네. 문을 여는 용도인가....')
         box.closed = False

    else:   # 열려있음
         showMessage('상자가 열려있다.')
box.onMouseAction = box_onMouseAction


def box_onKeypad():
    box.locked = False
    showMessage('상자의 잠금이 해제 되었다....!')
box.onKeypad = box_onKeypad


def keypad_onMouseAction(x,y,action):
    showKeypad('3110',box)
keypad.onMouseAction = keypad_onMouseAction


vase.moved = False
def vase_onMouseAction(x,y,action):
    if vase.moved == False:
        if action == MouseAction.DRAG_LEFT:
            vase.locate(scene2,400,300)
            paper2.show()
            showMessage('화분뒤에 무엇인가 있다.')
            vase.moved = True

        elif action == MouseAction.DRAG_RIGHT:
            vase.locate(scene2,600,300)
            paper2.show()  
            showMessage('화분뒤에 무엇인가 있다.')
            vase.moved = True
vase.onMouseAction = vase_onMouseAction

def paper2_onMouseAction(x,y,action): # 종이2를 주울때
    paper2.pick()
    showMessage('또다른 종이 쪽지를 주웠다. 숫자가 적혀있네..?')
paper2.onMouseAction = paper2_onMouseAction


def switch_onKeypad(): # 스위치 숨김해제
    showMessage('스위치 숨김이 해제 되었네. 아! 스위치가 오른쪽에 있구나.')
    switch.show()
    keypad3.show()
switch.onKeypad = switch_onKeypad


def keypad2_onMouseAction(x,y,action): # 키패드2 번호
    showKeypad('11571',switch)
keypad2.onMouseAction = keypad2_onMouseAction


switch.lighted = True
def switch_onMouseAction(x,y,action): # 스위치 온오프
    switch.lighted = not switch.lighted
    if switch.lighted:
        scene2.setLight(1)
        password.hide()

    else:
        scene2.setLight(0.3)
        password.show()
switch.onMouseAction = switch_onMouseAction


def door3_onKeypad():
    showMessage('키패드의 잠금이 해제 되었다....!')
    door3.show()
    showMessage('숨겨져 있던 문이 나타났다!!!')
door3.onKeypad = door3_onKeypad


def keypad3_onMouseAction(x,y,action):
    showKeypad('python',door3)
keypad3.onMouseAction = keypad3_onMouseAction


door3.closed = True
def door3_onMouseAction(x,y,action):
    if door3.closed:
        door3.setImage('Images/문-오른쪽-열림.png')
        door3.closed = False

    else:
        endGame()
door3.onMouseAction = door3_onMouseAction 


startGame(scene1)

