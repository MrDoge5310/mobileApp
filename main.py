from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        label1 = Label(text="Hello!")
        button1 = Button(text="Click me!")
        button2 = Button(text="Click me!")
        button3 = Button(text="Click me!")
        button4 = Button(text="Click me!")

        h1 = BoxLayout(orientation="horizontal", padding=10)
        h1.add_widget(button1)
        h1.add_widget(button2)
        h1.add_widget(button3)
        h1.add_widget(button4)

        h2 = BoxLayout(orientation="vertical")
        h2.add_widget(label1)
        h2.add_widget(h1)
        return h2


app = MyApp()
app.run()
