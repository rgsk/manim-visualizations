from manim import *
from manim import Scene


class Example(Scene):
    def construct(self):
        text = Text("Hello World")
        self.play(Write(text))
        self.wait()
