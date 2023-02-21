import pygame
import time
import random
import webbrowser
from money import *
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.messagebox import askyesno
import os
import MySQLdb

pygame.init()
screen = pygame.display.set_mode((1024, 650))
pygame.display.set_caption('Tài Xỉu v3.1')
running = True
clock = pygame.time.Clock()
font = pygame.font.SysFont('sans', 30)
font_2 = pygame.font.SysFont('Arial BLACK', 70)
font_3 = pygame.font.SysFont('sans', 25)
font_4 = pygame.font.SysFont('sans', 20)
font_5 = pygame.font.SysFont('Arial BLACK', 25, "bold")

link_ins = 'https://www.instagram.com/dovanduy552'
link_mess = 'https://www.facebook.com/messages/t/duy552.py'
image_ins = pygame.image.load("data_server/images/instagram.png")
image_mes = pygame.image.load("data_server/images/mess1.png")

txt = 'Total: None'
obj = Money("admin", 0)
so_du = obj.show_sodu()[0][0]
tien_cuoc = 0
player_choice = [0, 0]
x, y = 270, 380

GRAY = (153, 76, 0)
YELLOW = (255, 153, 51)
WHITE = (255, 255, 255)
WHITE_2 = (160, 160, 160)
WHITE_3 = (160, 160, 160)
WHITE_4 = (160, 160, 160)
WHITE_5 = (160, 160, 160)
WHITE_6 = (160, 160, 160)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GREEN_2 = (0, 255, 128)
COLER_C_1 = (0, 25, 51)
COLER_C_2 = (0, 25, 51)

img = pygame.image.load("data_server/images/back_ground.png")
img = pygame.transform.scale(img, (1024, 650))

first_dice = 0
second_dice = 0
third_dice = 0

#Face dice
pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(435, 200, 60, 60),  0, 10)
pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(515, 200, 60, 60),  0, 10)
pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(460, 280, 60, 60),  0, 10)

face_1 = pygame.image.load("data_server/images/face_1.png")
face_2 = pygame.image.load("data_server/images/face_2.png")
face_3 = pygame.image.load("data_server/images/face_3.png")
face_4 = pygame.image.load("data_server/images/face_4.png")
face_5 = pygame.image.load("data_server/images/face_5.png")
face_6 = pygame.image.load("data_server/images/face_6.png")

face_dice = [face_1, face_1, face_2, face_3, face_4, face_5, face_6]

def convert(money):
    money_new = []
    money = list(str(money))
    money.reverse()
    for i in range(1, len(money)+1):
        money_new.append(money[i-1])
        if i == len(money):
            break
        if not i%3:
            money_new.append(",")
    money_new.reverse()
    money_new = ''.join(money_new)
    return money_new

def _nap_():
    window = Tk()
    window.geometry("390x160")
    window.iconbitmap("data_server/images/icon.ico")
    window.resizable(0,0)
    window.config(background="#444444")
    window.title('Nap Tien')

    money = Label(window, text = "Number Money", fg = "white", bg = "#444444")
    money.place(x = 30, y = 30)

    t_money = Entry(window, width = 25)
    t_money.place(x = 150, y = 30)

    def get_text():
        so_tien = t_money.get().strip("\n")
        so_tien = int(so_tien)
        obj = Money("admin", so_tien)
        obj.nap_tien()
        messagebox.showinfo("Notify","Nap Tien Thanh Cong!")
        window.destroy()

    btn = Button(window, width = 7, height = 1, text = "ACTION", bd=5, command=get_text)
    btn.place(x = 180, y = 100)

    window.mainloop()

def _rut_():
    window = Tk()
    window.geometry("390x160")
    window.iconbitmap("data_server/images/icon.ico")
    window.resizable(0,0)
    window.config(background="#444444")
    window.title('Rut Tien')

    money = Label(window, text = "Number Money", fg = "white", bg = "#444444")
    money.place(x = 30, y = 30)

    t_money = Entry(window, width = 25)
    t_money.place(x = 150, y = 30)

    def get_text():
        so_tien = t_money.get().strip("\n")
        so_tien = int(so_tien)
        obj = Money("admin", so_tien)
        obj.rut_tien()
        window.destroy()

    btn = Button(window, width = 7, height = 1, text = "ACTION", bd=5, command=get_text)
    btn.place(x = 180, y = 100)

    window.mainloop()

def random_face():
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    third_dice = random.randint(1, 6)
    return first_dice, second_dice, third_dice
def check_mouse(mouse_x, mouse_y, tien_cuoc):
    if event.button == 1:
        if 270 <= mouse_x <= 345 and 460 <= mouse_y <= 505:
            tien_cuoc += 100000
        elif 370 <= mouse_x <= 445 and 460 <= mouse_y <= 505:
            tien_cuoc += 500000
        elif 470 <= mouse_x <= 545 and 460 <= mouse_y <= 505:
            tien_cuoc += 1000000
        elif 570 <= mouse_x <= 645 and 460 <= mouse_y <= 505:
            tien_cuoc += 10000000
        elif 670 <= mouse_x <= 745 and 460 <= mouse_y <= 505:
            tien_cuoc += 50000000
    return tien_cuoc
def print_tien_cuoc(tien_cuoc, x, y):
    text = font_3.render("%d" %tien_cuoc, True, WHITE)
    screen.blit(text, (x,y))

def Dat_cuoc(sec, mouse_x, mouse_y, tien_cuoc, so_du, txt):
    if event.button == 1:
        if 440 <= mouse_x <= 615 and 520 <= mouse_y <= 565 and sec > 7 and tien_cuoc > 0 and player_choice[0] != 0:
            root = Tk()
            answer = askyesno(title='Confirm', message=f'Bạn có muốn "Đặt Cược" thêm {tien_cuoc} VNĐ?')
            if answer:
                if (so_du-tien_cuoc >= 50000): 
                    player_choice[1] += tien_cuoc
                    txt = "Total: " + str(convert(player_choice[1])) + "đ"
                    root.destroy()
                    obj = Money("admin", tien_cuoc)
                    obj.rut_tien()
                else:
                    messagebox.showerror("Erorr","Số tiền còn lại\nphải lớn hơn 50K")
                    root.destroy()
            else:
                root.destroy()
        elif 440 <= mouse_x <= 615 and 520 <= mouse_y <= 565 and sec > 7 and so_du <= tien_cuoc > 0 and player_choice[0] != 0:
            root = Tk()
            messagebox.showerror("Error","Không đủ tiền!\nHãy nạp thêm!")
            root.destroy()
    return txt
def nap_rut(mouse_x, mouse_y, tien_cuoc, so_du):
    if event.button == 1:
        if 325 <= mouse_x <= 445 and 520 <= mouse_y <= 565:
            _nap_()
        if 610 <= mouse_x <= 730 and 520 <= mouse_y <= 565 and so_du >= tien_cuoc:
            _rut_()
    return so_du

def print_tk(screen):
    obj = Money("admin", 0)
    so_du = obj.show_sodu()

    money_new = convert(so_du[0][0])
    
    pygame.draw.rect(screen, (255,105,180), pygame.Rect(5, 5, 300, 30),  0, 10)
    text = font_3.render(f"Money: ${money_new} VNĐ", True, WHITE)
    screen.blit(text, (15,7))
    return so_du[0][0]

def print_icon(screen):
    screen.blit(image_ins, (895, 598))
    screen.blit(image_mes, (965, 598))

def print_face_dice():
    pass

def open_link(screen, mouse_x, mouse_y):
    if event.button == 1:
        if 900 < mouse_x < 930 and 600 < mouse_y < 630:
            webbrowser.open_new_tab(link_ins)
        elif 970 < mouse_x < 1000 and 600 < mouse_y < 630:
            webbrowser.open_new_tab(link_mess)

def show_kq(first_dice, second_dice, third_dice):
    tong_face = first_dice + second_dice + third_dice
    if tong_face > 9:
        return "Tai"
    elif tong_face < 10:
        return "Xiu"
    else:
        return "---"

def game_play(first_dice, second_dice, third_dice):
    tong_face = first_dice + second_dice + third_dice
    if player_choice[0]:
        if player_choice[1]:
            if tong_face > 9 and player_choice[0] == 9 or tong_face < 10 and player_choice[0] == 1:
                tien_win = player_choice[1]*1.8
                obj = Money("admin", tien_win)
                obj.nap_tien()
            else:
                pass

while running:
    clock.tick(60)
    screen.fill((0, 255, 0))

    #current time
    localtime = time.localtime(time.time())
    current_sec = localtime[5]
    sec = 50 - current_sec

    #back ground and windows
    screen.blit(img, (0, 0))
    pygame.draw.rect(screen, (153, 51, 255), pygame.Rect(160, 70, 700, 400),  0, 130)

    #get index mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()

    so_du = print_tk(screen)
    print_icon(screen)
    #Button tien
    pygame.draw.rect(screen, WHITE_2, pygame.Rect(270, 460, 75, 45),  0, 40)
    text_4_1 = font_4.render("100K", True, (0, 0, 0))
    screen.blit(text_4_1, (287,470))
    pygame.draw.rect(screen, WHITE_3, pygame.Rect(370, 460, 75, 45),  0, 40)
    text_4_2 = font_4.render("500K", True, (0, 0, 0))
    screen.blit(text_4_2, (387,470))
    pygame.draw.rect(screen, WHITE_4, pygame.Rect(470, 460, 75, 45),  0, 40)
    text_4_3 = font_4.render("1M", True, (0, 0, 0))
    screen.blit(text_4_3, (495,470))
    pygame.draw.rect(screen, WHITE_5, pygame.Rect(570, 460, 75, 45),  0, 40)
    text_4_4 = font_4.render("10M", True, (0, 0, 0))
    screen.blit(text_4_4, (590,470))
    pygame.draw.rect(screen, WHITE_6, pygame.Rect(670, 460, 75, 45),  0, 40)
    text_4_5 = font_4.render("50M", True, (0, 0, 0))
    screen.blit(text_4_5, (690,470))

    if 270 <= mouse_x <= 345 and 460 <= mouse_y <= 505:
        WHITE_2 = GREEN_2
    else:
        WHITE_2 = (160, 160, 160)
    if 370 <= mouse_x <= 445 and 460 <= mouse_y <= 505:
        WHITE_3 = GREEN_2
    else:
        WHITE_3 = (160, 160, 160)
    if 470 <= mouse_x <= 545 and 460 <= mouse_y <= 505:
        WHITE_4 = GREEN_2
    else:
        WHITE_4 = (160, 160, 160)
    if 570 <= mouse_x <= 645 and 460 <= mouse_y <= 505:
        WHITE_5 = GREEN_2
    else:
        WHITE_5 = (160, 160, 160)
    if 670 <= mouse_x <= 745 and 460 <= mouse_y <= 505:
        WHITE_6 = GREEN_2
    else:
        WHITE_6 = (160, 160, 160)

    #Button Dat - Nap - Rut
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(325,520,120,45),  0, 0, 20, 50, 20)
    text_5 = font_3.render(r"Nap Tien", True, (255, 255, 255))
    screen.blit(text_5, (335,530))
    pygame.draw.rect(screen, (0,255,0), pygame.Rect(440, 520, 175, 45),  0, border_bottom_left_radius = 40, border_bottom_right_radius = 40)
    text_5 = font_3.render(r"DAT CUOC", True, (0, 0, 0))
    screen.blit(text_5, (475,530))
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(610, 520, 120, 45),  0, 20, 50, 20, 0)
    text_5 = font_3.render(r"Rut Tien", True, (255, 255, 255))
    screen.blit(text_5, (630,530))

    #Chữ Tài Xỉu
    text_3 = font_3.render(str(txt), True, (0, 0, 0))
    screen.blit(text_3, (445,400))
    pygame.draw.rect(screen, GRAY, pygame.Rect(230, 100, 200, 150),  0, border_bottom_left_radius=80)
    text_3 = font_2.render("TAI", True, (0, 0, 0))
    screen.blit(text_3, (270,120))
    pygame.draw.rect(screen, GRAY, pygame.Rect(570, 100, 200, 150),  0, border_bottom_right_radius=80)
    text_3 = font_2.render("XIU", True, (255, 255, 255))
    screen.blit(text_3, (620,120))

    # Hình tròn time và đĩa
    pygame.draw.circle(screen, (102, 0, 205), (500, 260), 120, 120)
    pygame.draw.circle(screen, (102, 178, 255), (590, 340), 30, 30)

    #button đặt cược
    if sec > 0:
        #Face dice
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(435, 200, 60, 60),  0, 10)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(515, 200, 60, 60),  0, 10)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(460, 280, 60, 60),  0, 10)
        COLER_C_1 = COLER_C_1
        COLER_C_2 = COLER_C_2
        text = font.render("%d" %sec, True, (0, 0, 0))
        screen.blit(text, (575, 327))
        print_tien_cuoc(tien_cuoc, x, y)
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(450, 75, 100, 50),  0, 10)
        text = font_3.render("", True, WHITE)
        screen.blit(text, (480,85))
    else:
        COLER_C_1 = (0, 25, 51)
        COLER_C_2 = (0, 25, 51)
        WHITE_2 = (160, 160, 160)
        tien_cuoc = 0
        txt = 'Total: None'
        kq =show_kq(first_dice, second_dice, third_dice)
        text = font.render(f"{9-abs(sec)}", True, (0, 0, 0))
        screen.blit(text, (580, 323))
        screen.blit(face_dice[first_dice], (438, 204))
        screen.blit(face_dice[second_dice], (518, 204))
        screen.blit(face_dice[third_dice], (464, 282))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(450, 75, 100, 50),  0, 10)
        text = font_5.render(f"{kq}", True, WHITE)
        screen.blit(text, (475,85))

    if sec == 0:
        game_play(first_dice, second_dice, third_dice)
        time.sleep(1)
    
    pygame.draw.rect(screen, COLER_C_1, pygame.Rect(210, 300, 140, 50),  0, 100)
    text = font_3.render("Cuoc", True, WHITE)
    screen.blit(text, (250,310))
    pygame.draw.rect(screen, COLER_C_2, pygame.Rect(650, 300, 140, 50),  0, 100)
    text = font_3.render("Cuoc", True, WHITE)
    screen.blit(text, (690,310))

    if sec == 5:
        first_dice, second_dice, third_dice = random_face()
        time.sleep(1)
    if sec == -5:
        player_choice = [0, 0]

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 210 < mouse_x < 350 and 300 < mouse_y < 350 and sec > 7:
                    COLER_C_1, COLER_C_2 = YELLOW, (0, 25, 51)
                    x, y = 230, 380
                    pygame.draw.rect(screen, COLER_C_1, pygame.Rect(210, 300, 140, 50),  0, 100)
                    text = font_3.render("Cuoc", True, WHITE)
                    screen.blit(text, (250,310))
                    pygame.draw.rect(screen, COLER_C_2, pygame.Rect(650, 300, 140, 50),  0, 100)
                    text = font_3.render("Cuoc", True, WHITE)
                    screen.blit(text, (690,310))
                    player_choice[0] = 9
                    print_tien_cuoc(tien_cuoc, x, y)
                elif 650 < mouse_x < 790 and 300 < mouse_y < 350 and sec > 7:
                    COLER_C_2, COLER_C_1 = YELLOW, (0, 25, 51)
                    x, y = 680, 380
                    pygame.draw.rect(screen, COLER_C_1, pygame.Rect(210, 300, 140, 50),  0, 100)
                    text = font_3.render("Cuoc", True, WHITE)
                    screen.blit(text, (250,310))
                    pygame.draw.rect(screen, COLER_C_2, pygame.Rect(650, 300, 140, 50),  0, 100)
                    text = font_3.render("Cuoc", True, WHITE)
                    screen.blit(text, (690,310))
                    player_choice[0] = 1
                    print_tien_cuoc(tien_cuoc, x, y)
                tien_cuoc = check_mouse(mouse_x, mouse_y, tien_cuoc)
                txt = Dat_cuoc(sec, mouse_x, mouse_y, tien_cuoc, so_du, txt)
                so_du = nap_rut(mouse_x, mouse_y, tien_cuoc, so_du)
                open_link(screen, mouse_x, mouse_y)
        
        if event.type == pygame.QUIT:
            running = False  

    pygame.display.flip()

pygame.quit()