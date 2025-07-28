from manim import *
from manim import Scene


class Main(Scene):
    def construct(self):
        text = Text("Merge Sort")
        self.play(Write(text))
        self.wait()
