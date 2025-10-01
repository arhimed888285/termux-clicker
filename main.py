from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class Clicker(App):
    def build(self):
        self.count = 0
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='0', font_size=100)
        btn = Button(text='CLICK', font_size=50, on_press=self.click)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout
    
    def click(self, instance):
        self.count += 1
        self.label.text = str(self.count)

Clicker().run()
