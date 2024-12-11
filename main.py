from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import Label as CoreLabel
from kivy.uix.widget import Widget
from kivy import metrics

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)
        label = Label(text='hi', font_size=30, bold=True)
        layout.add_widget(label)
        return layout

if __name__ == "__main__":
    MyApp().run()
