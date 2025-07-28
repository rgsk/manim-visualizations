from typing import Any, List

from manim import *


class Main(Scene):
    def construct(self):
        text = Text("Merge Sort")
        self.play(Write(text))
        self.wait()
        self.play(text.animate.shift(2 * UP))

        arr = [5, 4, 2, 5, 3, 1, 3, 11]
        square_side_length = 0.75
        square_spacing = 1.3

        squares = [Square(side_length=square_side_length) for v in arr]
        numbers = [Tex(f"${v}$") for v in arr]

        # Arrange squares
        for i, rect in enumerate(squares):
            rect.shift(
                RIGHT * (i - (len(squares) - 1) / 2) *
                square_side_length * square_spacing
            )

        for i, number in enumerate(numbers):
            number.move_to(squares[i])

        self.play(*[Write(s) for s in squares], *[Write(n)
                  for n in numbers])

        def merge(arr: List[int], start: int, mid: int, end: int):
            self.play(*[sq.animate.set_color(WHITE if start <= i <= end else DARK_GRAY)
                        for i, sq in enumerate(squares)],
                      *[number.animate.set_color(WHITE if start <= i <= end else DARK_GRAY)
                          for i, number in enumerate(numbers)]
                      )
            aux = [0 for _ in range(end - start + 1)]
            aux_square_text: List[Any] = [None for _ in range(end - start + 1)]
            i = start
            j = mid + 1
            k = 0
            pointer_length = 0.4
            i_pointer = Arrow(start=DOWN * pointer_length,
                              end=UP).next_to(squares[i], DOWN)
            i_pointer_text = Tex('i').scale(.6).next_to(squares[i], DOWN * 6)
            j_pointer = Arrow(start=DOWN * pointer_length,
                              end=UP).next_to(squares[j], DOWN)
            j_pointer_text = Tex('j').scale(.6).next_to(squares[j], DOWN * 6)
            mid_line = Line(start=DOWN * pointer_length,
                            end=UP).next_to(squares[mid], RIGHT * .5)
            self.play(Write(i_pointer), Write(j_pointer), Write(
                i_pointer_text), Write(j_pointer_text), Write(mid_line))

            def build_aux_square(smaller_index):
                self.play(squares[smaller_index].animate.set_color(GREEN))
                aux_square = Square(side_length=square_side_length).next_to(
                    squares[start + k], UP)
                aux_text = Tex(f"${aux[k]}$").move_to(aux_square)
                aux_square_text[k] = [aux_square, aux_text]
                self.play(
                    Write(aux_square),
                    Write(aux_text),
                    squares[smaller_index].animate.set_color(WHITE),
                )

            def move_i():
                self.play(
                    i_pointer.animate.next_to(squares[i], DOWN),
                    i_pointer_text.animate.next_to(squares[i], DOWN * 6),
                )

            def move_j():
                if j < len(squares):
                    self.play(
                        j_pointer.animate.next_to(squares[j], DOWN),
                        j_pointer_text.animate.next_to(
                            squares[j], DOWN * 6),
                    )
                else:
                    last_square = squares[-1]
                    target = last_square.copy().shift(RIGHT * square_side_length * square_spacing)
                    self.play(
                        j_pointer.animate.next_to(target, DOWN),
                        j_pointer_text.animate.next_to(
                            target, DOWN * 6),
                    )
            while i <= mid and j <= end:
                if arr[i] <= arr[j]:
                    aux[k] = arr[i]
                    build_aux_square(i)
                    k += 1
                    i += 1
                    move_i()
                else:
                    aux[k] = arr[j]
                    build_aux_square(j)
                    k += 1
                    j += 1
                    move_j()
            while i <= mid:
                aux[k] = arr[i]
                build_aux_square(i)
                k += 1
                i += 1
                move_i()
            while j <= end:
                aux[k] = arr[j]
                build_aux_square(j)
                k += 1
                j += 1
                move_j()
            self.play(
                FadeOut(i_pointer),
                FadeOut(i_pointer_text),
                FadeOut(j_pointer),
                FadeOut(j_pointer_text),
                FadeOut(mid_line)
            )
            i = start
            k = 0
            while i <= end:
                arr[i] = aux[k]
                i += 1
                k += 1
            self.play(
                *[FadeOut(s) for s, t in aux_square_text],
                *[FadeOut(t) for s, t in aux_square_text],
                *[number.animate.become(Tex(f"${arr[i]}$").move_to(number)) for i, number in enumerate(numbers)]
            )

        def merge_sort(arr: List[int], start: int, end: int):
            if start < end:
                self.play(*[sq.animate.set_color(WHITE if start <= i <= end else DARK_GRAY)
                            for i, sq in enumerate(squares)],
                          *[number.animate.set_color(WHITE if start <= i <= end else DARK_GRAY)
                          for i, number in enumerate(numbers)]
                          )

                mid = (start + end) // 2
                merge_sort(arr, start, mid)
                merge_sort(arr, mid + 1, end)
                merge(arr, start, mid, end)

        class Solution:
            def mergeSort(self, arr: List[int]) -> List[int]:
                merge_sort(arr, 0, len(arr) - 1)
                return arr

        sol = Solution()
        sol.mergeSort(arr)
