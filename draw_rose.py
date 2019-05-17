import turtle
#rose_data为存储数据的py文件
import rose_data

def draw_line(pix_list):
    '''依据pix_list的像素点数据画图'''
    turtle.penup()
    turtle.goto(*pix_list[0])
    turtle.pendown()
    for pix in pix_list:
        turtle.goto(*pix)
        
def draw_pic(pic_data):
    '''pic_data为字典，每个item储存每一笔的像素点数据'''
    for i in range(1,len(pic_data)+1):
        pix_list = pic_data[i]
        draw_line(pix_list)
    
def init():
    turtle.title('rose')
    turtle.pensize(2)
    turtle.hideturtle()
    turtle.color('red','red')
    turtle.setup(width=800, height=500, startx=0, starty=0)

if __name__ == '__main__':
    init()
    draw_pic(rose_data.data)
    turtle.mainloop()
    
