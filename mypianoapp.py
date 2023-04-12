from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.config import Config
from kivy.core.audio import SoundLoader

class PianoWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # load all the sound files    
        self.sound_c_note = SoundLoader.load('c.wav')
        self.sound_c_note.play()

class MyPianoApp(App):
    def build(self):
        self.title="CHOPIN"
        return PianoWidget()

if __name__=='__main__':
    # set the window size
    Config.set('graphics', 'width', '800')
    Config.set('graphics', 'height', '800')
    MyPianoApp().run()

