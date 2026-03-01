from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.color_definitions import colors
from kivy.animation import Animation

#Initilize Screens
class WelcomeScreen(Screen): pass
class SignInScreen(Screen): pass
class OnBoardingScreen(Screen): pass
class PlanScreen(Screen): pass
class MainScreen(Screen):
    def on_enter(self):
        # Reset to 0 when entering the screen
        self.ids.progress.value = 0

        # Animate to 100% over 2 seconds with a 'bounce' effect
        anim = Animation(value=100, duration=2, t='out_quad')
        anim.start(self.ids.progress)
    pass
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