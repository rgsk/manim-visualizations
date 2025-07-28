from manim import *


def clear(scene: Scene):
    scene.play(*[FadeOut(mobj) for mobj in scene.mobjects])


square_side_length = 0.75
square_spacing = 1.3


def intro(scene: Scene):
    heading = Tex("Binary Search")
    scene.play(Write(heading))


def search_for_target_small_array(scene: Scene):
    text = Tex(
        f"We are given an array of numbers, and we want to know if a certain number ``target'' exists in it or not.",
        font_size=40
    ).to_edge(UP)
    scene.play(Write(text))
    scene.wait(3)
    target = 2
    array = [5, 4, 2, 1, 3]
    square_side_length = 0.75
    square_spacing = 1.3

    squares = [Square(side_length=square_side_length) for v in array]
    numbers = [Tex(f"${v}$") for v in array]

    # Arrange squares
    for i, rect in enumerate(squares):
        rect.shift(
            RIGHT * (i - (len(squares) - 1) / 2) *
            square_side_length * square_spacing
        )

    for i, number in enumerate(numbers):
        number.move_to(squares[i])

    scene.play(*[Write(s) for s in squares], *[Write(n)
                                               for n in numbers])

    text = Tex(f"Target: ${target}$", font_size=40).shift(UP * 1)
    scene.play(Write(text))

    text = Tex(f"Can you tell, if 2 exists or not?",
               font_size=34).shift(DOWN * 1)
    scene.play(Write(text))
    scene.wait(1)
    text = Tex(
        f"Pretty easy right, can you tell if 3 exists or not, and what about 9?", font_size=34).next_to(text, DOWN)
    scene.play(Write(text))
    scene.wait(1)
    text = Tex(
        f"How are we coming to the conclusion that 9 doesn't exists?", font_size=34).next_to(text, DOWN)
    scene.play(Write(text))
    scene.wait(3)
    text = Tex(
        f"Answer: By checking each element from the beginning of the array to the end.", font_size=34).next_to(text, DOWN)
    scene.play(Write(text))
    scene.wait(2)


def search_for_target_large_array(scene: Scene):
    text = Tex(
        f"Let's try it for a larger array?", font_size=40).to_edge(UP)
    scene.play(Write(text))
    array = [20, 12, 4, 21, 1, 3, 9, 10, 2, 11, 15, 19]
    squares = [Square(side_length=square_side_length) for v in array]
    numbers = [Tex(f"${v}$") for v in array]

    # Arrange squares
    for i, rect in enumerate(squares):
        rect.shift(
            RIGHT * (i - (len(squares) - 1) / 2) *
            square_side_length * square_spacing
        )

    for i, number in enumerate(numbers):
        number.move_to(squares[i])

    scene.play(*[Write(s) for s in squares], *[Write(n)
                                               for n in numbers])

    target = 11
    text = Tex(f"Target: ${target}$", font_size=40).shift(UP * 1)
    scene.play(Write(text))

    text = Tex(f"Try finding 11",
               font_size=34).shift(DOWN * 1)
    scene.play(Write(text))
    scene.wait(3)
    index = array.index(target)
    scene.play(numbers[index].animate.set_color(GREEN),
               squares[index].animate.set_color(GREEN),)
    scene.wait(1)
    text = Tex(f"It took longer than before right?",
               font_size=34).next_to(text, DOWN)
    scene.play(Write(text))
    scene.wait(2)

    text = Tex(f"But what if we sort the array?",
               font_size=34).next_to(text, DOWN)
    scene.play(Write(text))
    scene.wait(2)

    text = Tex(f"Ok I am going ahead and sorting the array next.",
               font_size=34).next_to(text, DOWN)
    scene.play(Write(text))
    scene.wait(2)


def search_for_target_sorted_array(scene: Scene):
    array = [20, 12, 4, 21, 1, 3, 9, 10, 2, 11, 15, 19]
    text = Tex(
        f"Here is the same array in sorted order", font_size=40).to_edge(UP)
    scene.play(Write(text))
    array.sort()

    squares = [Square(side_length=square_side_length) for v in array]
    numbers = [Tex(f"${v}$") for v in array]

    # Arrange squares
    for i, rect in enumerate(squares):
        rect.shift(
            RIGHT * (i - (len(squares) - 1) / 2) *
            square_side_length * square_spacing
        )

    for i, number in enumerate(numbers):
        number.move_to(squares[i])

    scene.play(*[Write(s) for s in squares], *[Write(n)
                                               for n in numbers])

    target = 11
    text = Tex(f"Target: ${target}$", font_size=40).shift(UP * 1)
    scene.play(Write(text))

    texts = []

    text = Tex(f"Try finding 11 now",
               font_size=34).shift(DOWN * 1)

    texts.append(text)
    scene.play(Write(text))
    scene.wait(3)
    index = array.index(target)
    scene.play(numbers[index].animate.set_color(GREEN),
               squares[index].animate.set_color(GREEN),)
    scene.wait(1)

    text = Tex(f"Why could you find the element, faster than before?",
               font_size=34).next_to(text, DOWN)
    texts.append(text)
    scene.play(Write(text))
    scene.wait(2)
    text = Tex(f"Because, you could quickly discard the left part, where elements are smaller than 11.",
               font_size=34).next_to(text, DOWN)
    texts.append(text)
    scene.play(Write(text))
    scene.wait(2)
    scene.play(*[FadeOut(t) for t in texts])
    scene.play(numbers[index].animate.set_color(WHITE),
               squares[index].animate.set_color(WHITE),)

    text = Tex(f"What if I ask you, tell me if 100 is present or not?",
               font_size=34).shift(DOWN * 1)
    scene.play(Write(text))
    scene.wait(2)

    text = Tex(f"You would glance at numbers from left to right, and since the largest number is 21, you conclude that 100 is not present.",
               font_size=34).next_to(text, DOWN)
    scene.play(Write(text))
    scene.wait(2)

    text = Tex(f"So, if the array is present in sorted order, we can search faster through it.",
               font_size=34).next_to(text, DOWN)
    scene.play(Write(text))
    scene.wait(2)

    text = Tex(f"Let's dive into concepts next.",
               font_size=34).next_to(text, DOWN)
    scene.play(Write(text))
    scene.wait(2)


def linear_search(scene: Scene):
    text = Tex(
        f"Linear Search").to_edge(UP)
    scene.play(Write(text))

    array = [20, 12, 4, 21, 1, 3, 9, 10, 2, 11, 15, 19]

    squares = [Square(side_length=square_side_length) for v in array]
    numbers = [Tex(f"${v}$") for v in array]

    # Arrange squares
    for i, rect in enumerate(squares):
        rect.shift(
            RIGHT * (i - (len(squares) - 1) / 2) *
            square_side_length * square_spacing
        )

    for i, number in enumerate(numbers):
        number.move_to(squares[i])

    # Index labels above the squares
    index_labels = [
        Tex(f"{i}").scale(0.7).next_to(squares[i], UP, buff=0.3)
        for i in range(len(squares))
    ]

    scene.play(*[Write(s) for s in squares], *[Write(n)
                                               for n in numbers], *[Write(i) for i in index_labels])

    target = 11
    text = Tex(f"Target: ${target}$", font_size=40).shift(UP * 2)
    scene.play(Write(text))

    text = Tex(f"Linear search algorithm works by searching for target in the array from the beginning.",
               font_size=34).shift(DOWN * 2)
    scene.play(Write(text))
    scene.wait(2)

    scene.play(FadeOut(text))

    pointer_length = 0.4
    i_pointer = Arrow(start=DOWN * pointer_length,
                      end=UP).next_to(squares[0], DOWN)
    i_pointer_text = Tex('i').scale(.6).next_to(squares[0], DOWN * 5)

    scene.play(Write(i_pointer),  Write(
        i_pointer_text), )

    i = 0
    n = len(array)
    while i < n:
        if i == 0:
            text = Tex(f"At each step we are evaluating, if arr[i] == target",
                       font_size=34).shift(DOWN * 2)
            scene.play(Write(text))
            scene.wait(2)
            scene.play(FadeOut(text))
        scene.play(
            i_pointer.animate.next_to(squares[i], DOWN),
            i_pointer_text.animate.next_to(squares[i], DOWN * 5)
        )

        if array[i] == target:
            scene.play(numbers[i].animate.set_color(GREEN),
                       squares[i].animate.set_color(GREEN),)

            text = Tex(f"We have found our target - {target}, so the algorithm concludes, and we return the index at which target is found ie. {i}.",
                       font_size=34).shift(DOWN * 2)
            scene.play(Write(text))
            scene.wait(2)
            break
        i += 1

    scene.play(FadeOut(text))
    text = Tex(f"But Linear search is slow, in worst case, you would have to search through all the elements to determine the index of target element.",
               font_size=34).shift(DOWN * 2)
    scene.play(Write(text))
    t1 = text
    scene.wait(2)
    text = Tex(f"So, time complexity is O(n).",
               font_size=34).next_to(text, DOWN)
    scene.play(Write(text))
    scene.wait(2)
    t2 = text
    scene.play([FadeOut(t1), FadeOut(t2)])
    text = Tex(f"We saw earlier that if array is sorted, we humans can search faster.",
               font_size=34).shift(DOWN * 2)
    scene.play(Write(text))
    scene.wait(2)
    text = Tex(f"Let's see next, how linear search performs on a sorted array.",
               font_size=34).next_to(text, DOWN)
    scene.play(Write(text))
    scene.wait(2)


def linear_search_sorted_array(scene: Scene):
    text = Tex(
        f"Linear Search On Sorted Array").to_edge(UP)
    scene.play(Write(text))

    array = [20, 12, 4, 21, 1, 3, 9, 10, 2, 11, 15, 19]
    array.sort()

    squares = [Square(side_length=square_side_length) for v in array]
    numbers = [Tex(f"${v}$") for v in array]

    # Arrange squares
    for i, rect in enumerate(squares):
        rect.shift(
            RIGHT * (i - (len(squares) - 1) / 2) *
            square_side_length * square_spacing
        )

    for i, number in enumerate(numbers):
        number.move_to(squares[i])

    # Index labels above the squares
    index_labels = [
        Tex(f"{i}").scale(0.7).next_to(squares[i], UP, buff=0.3)
        for i in range(len(squares))
    ]

    scene.play(*[Write(s) for s in squares], *[Write(n)
                                               for n in numbers], *[Write(i) for i in index_labels])

    target = 11
    text = Tex(f"Target: ${target}$", font_size=40).shift(UP * 2)
    scene.play(Write(text))

    pointer_length = 0.4
    i_pointer = Arrow(start=DOWN * pointer_length,
                      end=UP).next_to(squares[0], DOWN)
    i_pointer_text = Tex('i').scale(.6).next_to(squares[0], DOWN * 5)

    scene.play(Write(i_pointer),  Write(
        i_pointer_text), )

    i = 0
    n = len(array)
    while i < n:
        scene.play(
            i_pointer.animate.next_to(squares[i], DOWN),
            i_pointer_text.animate.next_to(squares[i], DOWN * 5)
        )

        if array[i] == target:
            scene.play(numbers[i].animate.set_color(GREEN),
                       squares[i].animate.set_color(GREEN),)

            t1 = Tex(f"We have found our target - {target}, and we return the index at which target is found ie. {i}.",
                     font_size=34).shift(DOWN * 2)
            scene.play(Write(t1))
            scene.wait(2)
            break
        i += 1

    t2 = Tex(f"But you can notice that linear search didn't took any advantage of the fact that array is sorted.",
             font_size=34).next_to(t1, DOWN)
    scene.play(Write(t2))
    scene.wait(2)

    scene.play(FadeOut(t1), FadeOut(t2))

    text = Tex(f"Linear Search is a computer algorithm, and it can't make guesses like us, we need to define a definite procedure to perform faster search operations if the array is sorted.",
               font_size=34).shift(DOWN * 2)
    scene.play(Write(text))
    scene.wait(2)

    text = Tex(f"This takes us to main topic of this video ie. Binary Search",
               font_size=34).next_to(text, DOWN)
    scene.play(Write(text))
    scene.wait(2)


def binary_search(scene: Scene):
    array = [20, 12, 4, 21, 1, 3, 9, 10, 2, 11, 15, 19]
    array.sort()
    target = 11
    n = len(array)

    square_side_length = 0.75
    square_spacing = 1.3

    squares = [Square(side_length=square_side_length) for v in array]
    numbers = [Tex(f"${v}$") for v in array]

    # Arrange squares
    for i, rect in enumerate(squares):
        rect.shift(
            RIGHT * (i - (len(squares) - 1) / 2) *
            square_side_length * square_spacing
        )

    for i, number in enumerate(numbers):
        number.move_to(squares[i])

    # Add heading
    heading = Tex("Binary Search").to_edge(UP)
    scene.play(Write(heading))

    # Index labels above the squares
    index_labels = [
        Tex(f"{i}").scale(0.7).next_to(squares[i], UP, buff=0.3)
        for i in range(len(squares))
    ]

    scene.play(*[Write(s) for s in squares], *[Write(n)
                                               for n in numbers], *[Write(i) for i in index_labels])

    # Show target text
    text = Tex(f"Target: ${target}$").shift(UP * 2)
    scene.play(Write(text))

    pointer_length = 0.4
    l_pointer = Arrow(start=DOWN * pointer_length,
                      end=UP).next_to(squares[0], DOWN)
    l_pointer_text = Tex('lo').scale(.6).next_to(squares[0], DOWN * 6)
    r_pointer = Arrow(start=DOWN * pointer_length,
                      end=UP).next_to(squares[-1], DOWN)
    r_pointer_text = Tex('hi').scale(.6).next_to(squares[-1], DOWN * 6)

    scene.play(Write(l_pointer), Write(r_pointer), Write(
        l_pointer_text), Write(r_pointer_text))

    lo, hi = 0, len(array) - 1

    def color_in_range(objects, color, range_indices):
        return [o.animate.set_color(color) for i, o in enumerate(objects) if i in range_indices]
    first_mid_text = True
    first_left_discard = True
    first_right_discard = True

    while lo <= hi:
        mid = (lo + hi) // 2

        if first_mid_text:
            first_mid_text = False
            t1 = Tex(
                r"We calculate the mid index using the formula:" r"\\"
                r"$\text{mid} = \frac{\text{lo} + \text{hi}}{2}$",
                font_size=34
            ).shift(DOWN * 3)

            scene.play(Write(t1))
            scene.wait(2)
            scene.play(FadeOut(t1))
            t2 = Tex(
                rf"$\text{{mid}} = \frac{{{lo} + {hi}}}{{2}} = {mid}$",
                font_size=34
            ).shift(DOWN * 3)

            scene.play(Write(t2))
            scene.wait(2)
            scene.play(FadeOut(t2))

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
            scene.play(*optional)
        scene.play(Write(current_arrow), Write(mid_text))

        if array[mid] < target:
            if first_left_discard:
                first_left_discard = False

                t1 = Tex(f"Since, target is greater than element at mid, and array is sorted, we are sure we would find our target element in right of mid index, so we discard the left part of the array from the search space",
                         font_size=34).shift(DOWN * 3)
                scene.play(Write(t1))
                scene.wait(4)
                scene.play(FadeOut(t1))

            scene.play(
                FadeOut(current_arrow),
                FadeOut(mid_text),
                l_pointer.animate.next_to(squares[mid + 1], DOWN),
                l_pointer_text.animate.next_to(
                    squares[mid + 1], DOWN * 8) if mid + 1 == hi else l_pointer_text.animate.next_to(
                    squares[mid + 1], DOWN * 6),
                *color_in_range(squares, DARK_GRAY,
                                range(lo, mid + 1)),
                *color_in_range(numbers, DARK_GRAY,
                                range(lo, mid + 1)),
                *color_in_range(index_labels, DARK_GRAY,
                                range(lo, mid + 1)),
            )
            lo = mid + 1

        elif array[mid] > target:
            if first_right_discard:
                first_right_discard = False

                t1 = Tex(f"Since, target is lesser than element at mid, and array is sorted, we are sure we would find our target element in left of mid index, so we discard the right part of the array from the search space",
                         font_size=34).shift(DOWN * 3)
                scene.play(Write(t1))
                scene.wait(4)
                scene.play(FadeOut(t1))

            scene.play(
                FadeOut(current_arrow),
                FadeOut(mid_text),
                r_pointer.animate.next_to(squares[mid - 1], DOWN),
                r_pointer_text.animate.next_to(
                    squares[mid - 1], DOWN * 8) if mid - 1 == lo else r_pointer_text.animate.next_to(
                    squares[mid - 1], DOWN * 6),
                * color_in_range(squares, DARK_GRAY,
                                 range(lo, mid + 1)),
                * color_in_range(squares, DARK_GRAY,
                                 range(mid, hi + 1)),
                *color_in_range(numbers, DARK_GRAY,
                                range(mid, hi + 1)),
                *color_in_range(index_labels, DARK_GRAY,
                                range(mid, hi + 1)),
            )

            hi = mid - 1

        else:
            t1 = Tex(f"Mid index points to the target element, so we return index - {mid}",
                     font_size=34).shift(DOWN * 2)
            scene.play(Write(t1))
            scene.wait(2)
            scene.play(FadeOut(t1))
            optional = []
            if l_pointer_text:
                optional.append(FadeOut(l_pointer_text))
            if r_pointer_text:
                optional.append(FadeOut(r_pointer_text))

            scene.play(
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

    t1 = Tex(f"Time Complexity of Binary Search",
             font_size=34).shift(DOWN * 2)
    scene.play(Write(t1))
    scene.wait(2)
    t1 = Tex(f"Since, each time we reduce search space by half, time complexity is O(log(n))",
             font_size=34).next_to(t1, DOWN)
    scene.play(Write(t1))
    scene.wait(2)


class Intro(Scene):
    def construct(self):
        intro(self)


class SearchForTargetSmallArray(Scene):
    def construct(self):
        search_for_target_small_array(self)


class SearchForTargetLargeArray(Scene):
    def construct(self):
        search_for_target_large_array(self)


class SearchForTargetSortedArray(Scene):
    def construct(self):
        search_for_target_sorted_array(self)


class LinearSearch(Scene):
    def construct(self):
        linear_search(self)


class LinearSearchSortedArray(Scene):
    def construct(self):
        linear_search_sorted_array(self)


class BinarySearch(Scene):
    def construct(self):
        binary_search(self)


class FullVideo(Scene):
    def construct(self):
        intro(self)
        clear(self)
        search_for_target_small_array(self)
        clear(self)
        search_for_target_large_array(self)
        clear(self)
        search_for_target_sorted_array(self)
        clear(self)
        linear_search(self)
        clear(self)
        linear_search_sorted_array(self)
        clear(self)
        binary_search(self)
        clear(self)
