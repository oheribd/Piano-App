from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.config import Config
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout

class MyPianoApp(App):
    def build(self):
        self.title="CHOPIN"
        parent = Widget()

        # layout
        layout = BoxLayout(orientation='horizontal')

        # load all the sound files
        self.sound_a_note = SoundLoader.load('a.wav')
        self.sound_b_note = SoundLoader.load('b.waw')
        self.sound_c_note = SoundLoader.load('c.wav')
        self.sound_d_note = SoundLoader.load('d.wav')
        self.sound_e_note = SoundLoader.load('e.wav')
        self.sound_f_note = SoundLoader.load('f.wav')
        self.sound_g_note = SoundLoader.load('g.wav')

        # a note
        a_note_button = Button(text='A')
        a_note_button.bind(on_release=self.play_note)
        layout.add_widget(a_note_button)

        # c note
        c_note_button = Button(text='C')
        c_note_button.bind(on_release=self.play_note)
        layout.add_widget(c_note_button)
        
        # d note
        d_note_button = Button(text='D')
        d_note_button.bind(on_release=self.play_note)
        layout.add_widget(d_note_button)

        parent.add_widget(layout)

        return parent 
    
    def play_note(self, obj):
        if obj.text == 'A':
            self.sound_a_note.play()
        elif obj.text == 'C':
            self.sound_c_note.play()
        elif obj.text == 'D':
           self.sound_d_note.play()


if __name__=='__main__':
    # set the window size
    Config.set('graphics', 'width', '800')
    Config.set('graphics', 'height', '800')
    MyPianoApp().run()
