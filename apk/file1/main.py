from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.core.audio import SoundLoader
from kivy.clock import Clock


class AudioApp(App):
    def build(self):
        self.audio = SoundLoader.load('Lukas_Graham_-_7_Years_(Naijay.com).mp3')

        self.layout = BoxLayout(orientation='vertical')

        self.play_button = Button(text='Play Audio')
        self.play_button.bind(on_press=self.play_audio)

        self.volume_slider = Slider(min=0, max=1, value=1)
        self.volume_slider.bind(value=self.adjust_volume)

        self.layout.add_widget(self.play_button)
        self.layout.add_widget(self.volume_slider)

        return self.layout

    def play_audio(self, instance):
        if self.audio:
            self.audio.play()
            Clock.schedule_once(self.stop_audio, 180)  # Stop audio after 3 minutes

    def adjust_volume(self, instance, value):
        if self.audio:
            self.audio.volume = value

    def stop_audio(self, dt):
        if self.audio and self.audio.state == 'play':
            self.audio.stop()


if __name__ == '__main__':
    AudioApp().run()
