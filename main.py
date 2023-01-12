from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        #add widgets to window
        self.window.cols = 1

        self.window.add_widget(Image(source = ''))
        self.greeting = Label(text = "what is your name")

        self.window.add_widget(self.greeting)

        self.user = TextInput(multiline = False)
        self.window.add_widget(self.user)

        self.botton = Button(text = "GREET")
        self.botton.bind (on_press=self.callback)
        self.window.add_widget(self.botton)

        return self.window

    def callback(self):
        self.greeting.text = "hello" + self.user.text



if __name__ == "__main__":
    SayHello().run()


