import random
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ListProperty
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class ConfettiParticle:
    def __init__(self, width, height):
        self.pos = [random.uniform(0, width), random.uniform(height, height + 100)]
        self.size = [random.uniform(5, 12), random.uniform(5, 12)]
        self.color = [random.random(), random.random(), random.random(), 1]
        self.speed = random.uniform(2, 5)
        self.drift = random.uniform(-1, 1)


class ConfettiWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.particles = []
        Clock.schedule_interval(self.update, 1 / 60)

    def update(self, dt):
        if not self.particles and self.width > 1:
            self.particles = [ConfettiParticle(self.width, self.height) for _ in range(50)]

        self.canvas.clear()
        with self.canvas:
            for p in self.particles:
                p.pos[1] -= p.speed
                p.pos[0] += p.drift

                # Reset particle to top if it goes off-screen
                if p.pos[1] < 0:
                    p.pos[1] = self.height
                    p.pos[0] = random.uniform(0, self.width)

                Color(*p.color)
                Rectangle(pos=p.pos, size=p.size)


class WelcomeScreen(MDScreen):
    pass


class ConfettiCashApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.accent_palette = "Amber"
        return Builder.load_file("welcome.kv")


if __name__ == "__main__":
    ConfettiCashApp().run()