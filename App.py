from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.color_definitions import colors
from kivy.animation import Animation
import random
from kivymd.uix.label import MDLabel
from kivy.clock import Clock

#Initilize Screens
class WelcomeScreen(Screen): pass
class SignInScreen(Screen): pass
class InfoScreen(Screen): pass
class OnBoardingScreen(Screen): pass
class PlanScreen(Screen): pass
class MainScreen(Screen):
    def on_enter(self):
        # 1. Reset progress bar and ensure GIF is hidden when entering screen
        self.ids.progress.value = 0
        self.ids.confetti_gif.opacity = 0
        self.ids.confetti_gif.anim_delay = -1 

        # 2. Start the progress bar animation
        anim = Animation(value=100, duration=3, t='out_quad')
        anim.bind(on_complete=self.play_lottie_gif)
        anim.start(self.ids.progress)

    def play_lottie_gif(self, *args):
        # 3. Make the GIF visible and start playing it
        gif = self.ids.confetti_gif
        gif.opacity = 1
        gif.anim_delay = 0.05  # Standard GIF frame speed (lower is faster)
        
        # 4. Schedule the GIF to hide again after 2.5 seconds
        # (Change the 2.5 to match however long your GIF is)
        Clock.schedule_once(self.hide_gif, 2.5)

    def hide_gif(self, dt):
        # 5. Hide and pause the GIF
        self.ids.confetti_gif.opacity = 0
        self.ids.confetti_gif.anim_delay = -1
class WrappedScreen(Screen): pass


class ConfettiCashApp(MDApp):
    def build(self):
        # 1. HIJACK TEAL: Replace the '500' (main) and '700' (dark) shades
        # with your specific Green (#A2C8C8)
        colors["Teal"]["500"] = "A2C8C8"
        colors["Teal"]["700"] = "8BAEAE"  # A slightly darker version of your green

        # 2. HIJACK AMBER: Replace the '500' shade with your Tan (#EFEBE2)
        colors["Amber"]["500"] = "EFEBE2"

        # 3. Now use them normally!
        # Every widget that uses "Primary" will now be your Green.
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Teal"
        self.theme_cls.theme_style = "Light"

        return  # Your Root Widget or Builder.load_file("confetticash.kv")

    def on_checkbox_active(self, checkbox, value):
        if value:
            print("User accepted the terms!")
        else:
            print("User unchecked the terms!")


if __name__ == "__main__":
    ConfettiCashApp().run()