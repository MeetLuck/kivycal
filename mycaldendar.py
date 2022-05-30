from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.button import Button
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivy.core.window import Window
from kivy.config import Config

Window.clearcolor = (0.5,0.5,0.5,1)
Window.size = 300,120
Builder.load_file('mycal.kv')

#class sel:
#    bg = 0.7,0.7,0.7,1
#class unsel:
#    bg = 0.8,0.8,0.8,1

class sel:
    bg = 0.7,0.7,0.7,1
class unsel:
    bg = 0.8,0.8,0.8,1
class today:
    fg = 0,1,0,1
class MyCalendar(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        for col,weekday in enumerate('SUN MON TUS WED THU FRI SAT'.split()):
            button = Button(text=weekday)
            button.font_size = 12
            button.background_color = 0.75,0.75,0.75,1
            if weekday == 'SUN':   button.color = 1,0,0,1
            elif weekday == 'SAT': button.color = 0,0,1,1
            else:                  button.color = 0,0,0,1
            self.ids.id_table6x7.add_widget(button)
        for row in range(1,6+1):
            for col in range(7):
                button = Button()
                id = f'rc{row}{col}'
                button.bind(on_release = self.on_click)
                self.ids[id] = button 
                self.ids.id_table6x7.add_widget(button)
        import calendar
        from datetime import datetime
        self.now = datetime.now()
        self.TextCalendar = calendar.TextCalendar(calendar.SUNDAY)
        self.update_dates(self.now.year,self.now.month)
    def update_dates(self,year,month):
        row = 1
        for ayear,amonth,aday,aweekday in self.TextCalendar.itermonthdays4(year,month): 
            col = (aweekday+1) % 7
            id = f'rc{row}{col}'
            button = self.ids[id]
            button.text = str(aday)
            button.background_color = 0.8,0.8,0.8,1
            button.color = 0,0,0,1
            if amonth == month:
                if col == 0: button.color = 1,0,0,1
                if col == 6: button.color = 0,0,1,1
                if (ayear, amonth, aday) == (self.now.year, self.now.month, self.now.day):
                    button.color = today.fg
                    button.background_color = sel.bg
            else:
                button.color = 0,0,0,0.3
            if col == 6: row += 1
    def on_click(self,btn):
        for id in self.ids:
            if self.ids[id] == btn:
                btn.background_color = sel.bg
            else:
                self.ids[id].background_color = unsel.bg
                #print(id,btn.text)
    def on_change_month(self,updown):
        month = int(self.ids['id_month'].text)
        if updown == -1: # decrease month
            month += -1
            self.ids['id_month'].text = str(month)
        if updown == +1: # decrease month
            month += +1
            self.ids['id_month'].text = str(month)
        self.update_dates(self.now.year, month)

class TestApp(MDApp):
    def build(self):
        return MyCalendar()

TestApp().run()
