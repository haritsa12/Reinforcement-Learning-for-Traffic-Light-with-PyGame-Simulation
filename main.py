from ast import dump
import pygame as pg
import string
import json
import sys
 
class TextBox(object):
    def __init__(self,rect,**kwargs):
        '''
        Optional kwargs and their defaults:
            "id" : None,
            "command" : None,
                function to execute upon enter key
                Callback for command takes 2 args, id and final (the string in the textbox)
            "active" : True,
                textbox active on opening of window
            "color" : pg.Color("white"),
                background color
            "font_color" : pg.Color("black"),
            "outline_color" : pg.Color("black"),
            "outline_width" : 2,
            "active_color" : pg.Color("blue"),
            "font" : pg.font.Font(None, self.rect.height+4),
            "clear_on_enter" : False,
                remove text upon enter
            "inactive_on_enter" : True
            "blink_speed": 500
                prompt blink time in milliseconds
            "delete_speed": 500
                backspace held clear speed in milliseconds
             
        Values:
            self.rect = pg.Rect(rect)
            self.buffer = []
            self.final = None
            self.rendered = None
            self.render_rect = None
            self.render_area = None
            self.blink = True
            self.blink_timer = 0.0
            self.delete_timer = 0.0
            self.accepted = string.ascii_letters+string.digits+string.punctuation+" "
        '''
        self.name_=None
        self.password_=None
        self.rect = pg.Rect(rect)
        self.buffer = []
        self.final = None
        self.rendered = None
        self.render_rect = None
        self.render_area = None
        self.blink = True
        self.blink_timer = 0.0
        self.delete_timer = 0.0
        self.accepted = string.ascii_letters+string.digits+string.punctuation+" "
        self.process_kwargs(kwargs)

    def process_kwargs(self,kwargs):
        defaults = {"id" : None,
                    "command" : None,
                    "active" : True,
                    "color" : pg.Color("white"),
                    "font_color" : pg.Color("black"),
                    "outline_color" : pg.Color("black"),
                    "outline_width" : 2,
                    "active_color" : pg.Color("blue"),
                    "font" : pg.font.Font(None, self.rect.height+4),
                    "clear_on_enter" : False,
                    "inactive_on_enter" : True,
                    "blink_speed": 500,
                    "delete_speed": 75}
        for kwarg in kwargs:
            if kwarg in defaults:
                defaults[kwarg] = kwargs[kwarg]
            else:
                raise KeyError("TextBox accepts no keyword {}.".format(kwarg))
        self.__dict__.update(defaults)
 
    def get_event(self,event, mouse_pos=None):
        ''' Call this on your event loop
         
            for event in pg.event.get():
                TextBox.get_event(event)
        '''
        if event.type == pg.KEYDOWN and self.active:
            if event.key in (pg.K_RETURN,pg.K_KP_ENTER):
                self.execute()
            elif event.key == pg.K_BACKSPACE:
                if self.buffer:
                    self.buffer.pop()
            elif event.unicode in self.accepted:
                self.buffer.append(event.unicode)
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if not mouse_pos:
                mouse_pos = pg.mouse.get_pos()
            self.active = self.rect.collidepoint(mouse_pos)
 
    def execute(self):
        if self.command:
            self.command(self.id,self.final)
        self.active = not self.inactive_on_enter
        if self.clear_on_enter:
            self.buffer = []
             
    def switch_blink(self):
        if pg.time.get_ticks()-self.blink_timer > self.blink_speed:
            self.blink = not self.blink
            self.blink_timer = pg.time.get_ticks()
 
    def update(self):
        '''
        Call once on your main game loop
        '''
        new = "".join(self.buffer)
        if new != self.final:
            self.final = new
            self.rendered = self.font.render(self.final, True, self.font_color)
            self.render_rect = self.rendered.get_rect(x=self.rect.x+2,
                                                      centery=self.rect.centery)
            if self.render_rect.width > self.rect.width-6:
                offset = self.render_rect.width-(self.rect.width-6)
                self.render_area = pg.Rect(offset,0,self.rect.width-6,
                                           self.render_rect.height)
            else:
                self.render_area = self.rendered.get_rect(topleft=(0,0))
        self.switch_blink()
        self.handle_held_backspace()
         
    def handle_held_backspace(self):
        if pg.time.get_ticks()-self.delete_timer > self.delete_speed:
            self.delete_timer = pg.time.get_ticks()
            keys = pg.key.get_pressed()
            if keys[pg.K_BACKSPACE]:
                if self.buffer:
                    self.buffer.pop()
 
    def draw(self,surface):
        '''
        Call once on your main game loop
        '''
        outline_color = self.active_color if self.active else self.outline_color
        outline = self.rect.inflate(self.outline_width*2,self.outline_width*2)
        surface.fill(outline_color,outline)
        surface.fill(self.color,self.rect)
        if self.rendered:
            surface.blit(self.rendered,self.render_rect,self.render_area)
        if self.blink and self.active:
            curse = self.render_area.copy()
            curse.topleft = self.render_rect.topleft
            surface.fill(self.font_color,(curse.right+1,curse.y,2,curse.h))
pg.init()
screen = pg.display.set_mode((600,400))
width = screen.get_width()
  
# stores the height of the
# screen into a variable
height = screen.get_height()

# light shade of the button
background = pg.image.load('600x400.jpg').convert()
color_light = (170,170,170)

# dark shade of the button
color_dark = (100,100,100)
black = (0, 0, 0)
white = (255, 255, 255)
done = False
font = pg.font.Font(None, 30)
screen.blit(background,(0,0))
alpha_text = font.render(('Alpha:'), True, white, black)
screen.blit(alpha_text,(70,75))

gamma_text = font.render(('Gamma:'), True, white, black)
screen.blit(gamma_text,(70,175))

text = font.render('Done' , True , white,black)

def write_json(new_data, filename='alpha & gamma.json'):
    with open(filename,'w+') as file:
          # First we load existing data into a dict.
        # file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        # file_data["emp_details"].append(new_data)
        # Sets file's current position at offset.
        # file.seek(0)
        # convert back to json.
        json.dump(new_data, file, indent = 4)

def name_on_enter(id, final):
    
    alpha_temp='{}'.format(final)
    print(alpha_temp)
    alpha='%s'%alpha_temp
    # alpha_json={"alpha":alpha}
    with open("alpha & gamma.json", "r") as file:
        data = json.load(file)
    data['Parameters']['Alpha']=alpha
    write_json(data)
    # print('password:',str(password))
    return alpha
    
def pass_on_enter(id, final):
    gamma_temp='{}'.format(final)
    print(gamma_temp)
    gamma='%s'%gamma_temp
    with open("alpha & gamma.json", "r") as file:
        data = json.load(file)
    data['Parameters']['Gamma']=gamma
    write_json(data)
    return gamma
 
username_settings = {
    "command" : name_on_enter,
    "inactive_on_enter" : False,
}
password_settings = {
    "command" : pass_on_enter,
    "inactive_on_enter" : False,
}
 
name_entry = TextBox(rect=(70,100,150,30), **username_settings)
pass_entry = TextBox(rect=(70,200,150,30), **password_settings)

# print ('hello',dump_pass)
while not done:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # execfile("Traffic_Q_Learning3.py")
            done = True
        if event.type == pg.MOUSEBUTTONDOWN:
              
            #if the mouse is clicked on the
            # button the game is terminated
            # if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
            if 70 <= mouse[0] <= 112 and 250 <= mouse[1] <= 290:    
                execfile("Traffic_Q_Learning3.py")
        name_entry.get_event(event)
        pass_entry.get_event(event)
    mouse = pg.mouse.get_pos()
    # if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
    if 70 <= mouse[0] <= 112 and 250 <= mouse[1] <= 290:
        # pg.draw.rect(screen,color_light,[width/2,height/2,140,40])
        pg.draw.rect(screen,color_light,[70,250,67,40])
          
    else:
        # pg.draw.rect(screen,color_dark,[width/2,height/2,140,40])
        pg.draw.rect(screen,color_dark,[70,250,67,40])
      
    # superimposing the text onto our button
    screen.blit(text , (78,260))
    name_entry.update()
    pass_entry.update()
    name_entry.draw(screen)
    pass_entry.draw(screen)
    
    # print (pass_on_enter.gamma)
    # execfile('Traffic_Q_Learning3.py')
    
    # pg.display.flip()
    pg.display.update()
    