from manim import *
from manim import Scene


class Main(Scene):
    def construct(self):
        values = [1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10]
        target = 8
        n = len(values)

        square_side_length = 0.75
        square_spacing = 1.3

        squares = [Square(side_length=square_side_length) for v in values]
        numbers = [Tex(f"${v}$") for v in values]

        # Arrange squares
        for i, rect in enumerate(squares):
            rect.shift(
                RIGHT * (i - (len(squares) - 1) / 2) *
                square_side_length * square_spacing
            )

        for i, number in enumerate(numbers):
            number.move_to(squares[i])

        # Add heading
        heading = Tex(r"\textbf{Binary Search}").to_edge(UP * 1.5)
        self.play(Write(heading))

        # Index labels above the squares
        index_labels = [
            Tex(f"{i}").scale(0.7).next_to(squares[i], UP, buff=0.3)
            for i in range(len(squares))
        ]

        self.play(*[Write(s) for s in squares], *[Write(n)
                  for n in numbers], *[Write(i) for i in index_labels])

        # Show target text
        text = Tex(f"Target: ${target}$").shift(UP * 2)
        self.play(Write(text))

        pointer_length = 0.4
        l_pointer = Arrow(start=DOWN * pointer_length,
                          end=UP).next_to(squares[0], DOWN)
        l_pointer_text = Tex('lo').scale(.6).next_to(squares[0], DOWN * 6)
        r_pointer = Arrow(start=DOWN * pointer_length,
                          end=UP).next_to(squares[-1], DOWN)
        r_pointer_text = Tex('hi').scale(.6).next_to(squares[-1], DOWN * 6)

        self.play(Write(l_pointer), Write(r_pointer), Write(
            l_pointer_text), Write(r_pointer_text))

        lo, hi = 0, len(values) - 1

        def color_in_range(objects, color, range_indices):
            return [o.animate.set_color(color) for i, o in enumerate(objects) if i in range_indices]

        while lo <= hi:
            mid = (lo + hi) // 2

            current_arrow = (
                Arrow(start=DOWN * pointer_length, end=UP)
                .next_to(squares[mid], DOWN)
                .set_color(ORANGE)
            )
            mid_text = Tex('mid').scale(.6).next_to(
                squares[mid], DOWN * 6).set_color(ORANGE)
            optional = []
            if mid == lo:
                optional.append(FadeOut(l_pointer_text))
                l_pointer_text = None
            if mid == hi:
                optional.append(FadeOut(r_pointer_text))
                r_pointer_text = None
            if optional:
                self.play(*optional)
            self.play(Write(current_arrow), Write(mid_text))

            if values[mid] < target:
                self.play(
                    FadeOut(current_arrow),
                    FadeOut(mid_text),
                    l_pointer.animate.next_to(squares[mid + 1], DOWN),
                    l_pointer_text.animate.next_to(
                        squares[mid + 1], DOWN * 8) if mid + 1 == hi else l_pointer_text.animate.next_to(
                        squares[mid + 1], DOWN * 6),
                    * color_in_range(squares, DARK_GRAY, range(lo, mid + 1)),
                    *color_in_range(numbers, DARK_GRAY, range(lo, mid + 1)),
                    *color_in_range(index_labels, DARK_GRAY,
                                    range(lo, mid + 1)),
                )
                lo = mid + 1

            elif values[mid] > target:
                self.play(
                    FadeOut(current_arrow),
                    FadeOut(mid_text),
                    r_pointer.animate.next_to(squares[mid - 1], DOWN),
                    r_pointer_text.animate.next_to(
                        squares[mid - 1], DOWN * 8) if mid - 1 == lo else r_pointer_text.animate.next_to(
                        squares[mid - 1], DOWN * 6),
                    * color_in_range(squares, DARK_GRAY, range(lo, mid + 1)),
                    * color_in_range(squares, DARK_GRAY, range(mid, hi + 1)),
                    *color_in_range(numbers, DARK_GRAY, range(mid, hi + 1)),
                    *color_in_range(index_labels, DARK_GRAY,
                                    range(mid, hi + 1)),
                )
                hi = mid - 1

            else:
                optional = []
                if l_pointer_text:
                    optional.append(FadeOut(l_pointer_text))
                if r_pointer_text:
                    optional.append(FadeOut(r_pointer_text))
                self.play(
                    *color_in_range(squares, DARK_GRAY, range(mid)),
                    *color_in_range(squares, DARK_GRAY, range(mid + 1, n)),
                    *color_in_range(numbers, DARK_GRAY, range(mid)),
                    *color_in_range(numbers, DARK_GRAY, range(mid + 1, n)),
                    *color_in_range(index_labels, DARK_GRAY, range(mid)),
                    *color_in_range(index_labels, DARK_GRAY,
                                    range(mid + 1, n)),
                    numbers[mid].animate.set_color(GREEN),
                    squares[mid].animate.set_color(GREEN),
                    index_labels[mid].animate.set_color(GREEN),
                    FadeOut(l_pointer),
                    FadeOut(r_pointer),
                    *optional
                )
                break

        self.play(*[FadeOut(obj) for obj in numbers + squares +
                  index_labels + [current_arrow,  text, mid_text, heading]])
