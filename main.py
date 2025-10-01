from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import time

class TermuxClicker(App):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.start_time = time.time()
    
    def build(self):
        # Главный layout
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Заголовок
        title_label = Label(
            text='[color=#3498db]🎯 TERMUX CLICKER[/color]',
            markup=True,
            font_size='24sp'
        )
        
        # Счетчик
        self.count_label = Label(
            text=f'[color=#e74c3c]{self.count}[/color]',
            markup=True,
            font_size='48sp'
        )
        
        count_text = Label(
            text='[color=#95a5a6]кликов[/color]',
            markup=True,
            font_size='16sp'
        )
        
        # Кнопка клика
        click_btn = Button(
            text='КЛИКНУТЬ!',
            font_size='20sp',
            background_color=(0.2, 0.8, 0.2, 1),
            size_hint=(1, 0.3),
            on_press=self.click
        )
        
        # Layout для дополнительных кнопок
        btn_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.2))
        
        reset_btn = Button(
            text='СБРОС',
            font_size='16sp',
            background_color=(0.9, 0.2, 0.2, 1),
            on_press=self.reset
        )
        
        auto_btn = Button(
            text='АВТО x10',
            font_size='16sp',
            background_color=(1, 0.6, 0, 1),
            on_press=self.auto_click
        )
        
        btn_layout.add_widget(reset_btn)
        btn_layout.add_widget(auto_btn)
        
        # Добавляем все в главный layout
        main_layout.add_widget(title_label)
        main_layout.add_widget(self.count_label)
        main_layout.add_widget(count_text)
        main_layout.add_widget(click_btn)
        main_layout.add_widget(btn_layout)
        
        return main_layout
    
    def click(self, instance):
        self.count += 1
        self.count_label.text = f'[color=#e74c3c]{self.count}[/color]'
    
    def reset(self, instance):
        self.count = 0
        self.start_time = time.time()
        self.count_label.text = f'[color=#e74c3c]{self.count}[/color]'
    
    def auto_click(self, instance):
        for i in range(10):
            self.count += 1
            self.count_label.text = f'[color=#e74c3c]{self.count}[/color]'

if __name__ == '__main__':
    TermuxClicker().run()
