from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    def __init__(self, name='main'):
        super().__init__(name=name)


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
