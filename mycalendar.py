from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.config import Config
from os.path import dirname,abspath,join

#Window.clearcolor = (0.5,0.5,0.5,1)
Window.size = 300,120
kvfile = join(dirname(__file__),'mycalendar.kv')
Builder.load_file(kvfile)

class MyCalendar(BoxLayout):

    import calendar
    from datetime import datetime
    now = datetime.now()
    year,month = now.year, now.month
    TextCalendar = calendar.TextCalendar(calendar.SUNDAY)
    unsel = type("unselect", (), {'bg':(0.8,0.8,0.8,0)})
    sel = type("select", (), {'bg':(0.8,0.8,0.8,1)})
    today = type("today", (), {'fg':(0,0.8,0,1)})

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.create_weekdays()
        self.create_dates()
        print(self.unsel.bg)

    def create_weekdays(self):
        for col,weekday in enumerate('SUN MON TUS WED THU FRI SAT'.split()):
            button = Button(text=weekday)
            button.font_size = 12
            button.background_color = 0.95,0.95,0.95,1
            if weekday == 'SUN':   button.color = 1,0,0,0.7
            elif weekday == 'SAT': button.color = 0,0,1,0.7
            else:                  button.color = 0,0,0,0.7
            self.ids['id_table6x7'].add_widget(button)

    def create_dates(self):
        from functools import partial
        for row in range(1,6+1):
            for col in range(7):
                button = Button()
                id = f'rc{row}{col}'
                button.bind(on_release = self.on_click)
                self.ids[id] = button 
                self.ids.id_table6x7.add_widget(button)
        self.update_dates(self.year,self.month)

    def initialize(self):
        print(self.unsel, self.unsel.bg)
        for row in range(1,6+1):
            for col in range(7):
                id = f'rc{row}{col}'
                button = self.ids[id]
                button.text = ''
                button.bold = False
                button.background_color = self.unsel.bg
                button.color = 0,0,0,1

    def update_dates(self,year,month):
        self.initialize()
        row = 1
        for ayear,amonth,aday,aweekday in self.TextCalendar.itermonthdays4(year,month): 
            col = (aweekday+1) % 7
            id = f'rc{row}{col}'
            button = self.ids[id]
            button.text = str(aday)
            if amonth == month:
                if col == 0: button.color = 1,0,0,1 # SUNDAY
                if col == 6: button.color = 0,0,1,1 # SATERDAY
                if (ayear, amonth, aday) == (self.now.year, self.now.month, self.now.day):
                    button.bold = True
                    button.color = self.today.fg
                    button.background_color = self.sel.bg
            else:  # not this month
                button.color = 0,0,0,0.3
            if col == 6: row += 1
            #print(id,button.text)

    def on_click(self,btn):
        for id in self.ids:
            if self.ids[id] == btn:
                btn.background_color = self.sel.bg
            else:
                self.ids[id].background_color = self.unsel.bg

    def on_change_month(self,nextmonth):
        self.month = int(self.ids['id_month'].text)
        if nextmonth == -1: self.month += -1
        if nextmonth == +1: self.month += +1
        if self.month == 13: 
            self.year += 1
            self.month = self.month % 12
        if self.month == 0:
            self.year += -1
            self.month = 12
        self.ids['id_month'].text = str(self.month)
        self.update_dates(self.year, self.month)

if __name__ ==  '__main__':
    class TestApp(MDApp):
        def build(self):
            return MyCalendar()
    TestApp().run()
