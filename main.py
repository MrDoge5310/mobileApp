from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    def __init__(self, name='main'):
        super().__init__(name=name)
        instr = Label(text="Instructions")
        name_input = TextInput(text='name', multiline=False, size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5})
        age_input = TextInput(text='age', multiline=False, size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5})
        self.next_button = Button(text="Next", size_hint=(0.4, None), height='60sp', pos_hint={'center_x': 0.5})
        self.next_button.on_press = self.next

        line1 = BoxLayout()
        line2 = BoxLayout(orientation="vertical", spacing=5, size_hint=(1, 0.3))
        layout = BoxLayout(orientation="vertical", padding=5)

        line1.add_widget(instr)
        line2.add_widget(name_input)
        line2.add_widget(age_input)
        line2.add_widget(self.next_button)
        layout.add_widget(line1)
        layout.add_widget(line2)

        self.add_widget(layout)

    def next(self):
        self.manager.current = 'heart_beat_check'


class HeartBeatCheckScreen(Screen):
    def __init__(self, name='heart_beat_check'):
        super().__init__(name="heart_beat_check")


class SeatSetScreen(Screen):
    def __init__(self, name="seat_set"):
        super().__init__(name="seat_set")


class RestScreen(Screen):
    def __init__(self, name="rest"):
        super().__init__(name="rest")


class ResultsScreen(Screen):
    def __init__(self, name="results"):
        super().__init__(name="results")


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen())
        sm.add_widget(HeartBeatCheckScreen())
        sm.add_widget(SeatSetScreen())
        sm.add_widget(RestScreen())
        sm.add_widget(ResultsScreen())
        return sm


app = MyApp()
app.run()
