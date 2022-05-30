from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.button import Button
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivy.core.window import Window
from kivy.config import Config

#Config.set('graphics', 'borderless', False)
#Config.set('graphics', 'resizable', True)
#Window.clearcolor = (1,1,1,0.5)
Window.clearcolor = (0.5,0.5,0.5,1)
Window.size = 300,120
#Window.size = 380,200
Builder.load_file('mycal.kv')

class sel:
    bg = 0.7,0.7,0.7,1
class unsel:
    bg = 0.8,0.8,0.8,1
class today:
    fg = 0,1,0,1
    import calendar
    from datetime import datetime
    now = datetime.now()
    year, month ,day = now.year, now.month, now.day
    TextCalendar = calendar.TextCalendar(calendar.SUNDAY)

class MyCalendar(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        for col,weekday in enumerate('SUN MON TUS WED THU FRI SAT'.split()):
            button = Button(text=weekday)
            button.font_size = 12
            if weekday == 'SUN':   button.color = 1,0,0,1
            elif weekday == 'SAT': button.color = 0,0,1,1
            else:                  button.color = 1,1,1,1
            #button.background_color = 1,1,1,0.7
            #self.ids[f'rc{0}{col}'] = button 
            #self.ids.id_table6x7.add_widget(button)
        self.update_dates()
    def update_dates(self):
        #import calendar
        #from datetime import datetime
        #now = datetime.now()
        #year, month ,day = now.year, now.month, now.day
        #year,month, = today[:2]
        #weekday, numofdays = calendar.monthrange(today.year, today.month)
        #c = calendar.TextCalendar(calendar.SUNDAY)
        row = 1
        for ayear,amonth,aday,aweekday in today.TextCalendar.itermonthdays4(today.year,today.month): 
            col = (aweekday+1) % 7
            button = Button(text=str(aday))
            button.bind(on_release = self.on_click)
            if amonth == today.month:
                if col == 0: button.color = 1,0,0,1
                if col == 6: button.color = 0,0,1,1
            else:
                button.color = 0,0,0,0.5
            if (today.year, today.month, today.day) == (ayear, amonth, aday):
                button.color = today.fg
                button.background_color = sel.bg
            if col == 6: row += 1
            self.ids[f'rc{row}{col}'] = button 
            self.ids.id_table6x7.add_widget(button)
    def on_click(self,btn):
        for id in self.ids:
            if self.ids[id] == btn:
                btn.background_color = sel.bg
            else:
                self.ids[id].background_color = unsel.bg
                print(id,btn.text)
        #print(self.ids[id])
        #print(btn,btn.uid, btn.text)
        #print( dir(btn) )

class TestApp(MDApp):
    def build(self):
        return MyCalendar()

TestApp().run()
