from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from datetime import datetime
from kivy.core.window import Window

Window.size = (360, 640) 
class DreamDiary(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        self.label = Label(text="✨ Write✨", font_size=24)
        self.add_widget(self.label)

        self.input = TextInput(hint_text="Write right here (:", multiline=True, size_hint=(1, 0.6))
        self.add_widget(self.input)

        self.save_button = Button(text="save it😍", size_hint=(1, 0.2))
        self.save_button.bind(on_press=self.save_dream)
        self.add_widget(self.save_button)

        self.status = Label(text="", font_size=16)
        self.add_widget(self.status)

    def save_dream(self, instance):
        dream_text = self.input.text
        if dream_text.strip() == "":
            self.status.text = "First Write😅"
            return

        with open("dreams.txt", "a", encoding='utf-8') as file:
            file.write(f"{datetime.now()}:\n{dream_text}\n\n")

        self.input.text = ""
        self.status.text = "Has saves... 💾🌙"

class DreamApp(App):
    def build(self):
        return DreamDiary()

if __name__ == "__main__":
    DreamApp().run()
