from manim import *
from manim import Scene


class MergeSort(Scene):
    def construct(self):
        cpp_code = """
void merge(vector<int> &vec, int start, int mid, int end) {
    int i = start;
    int j = mid + 1;
    vector<int> temp(end - start + 1);
    int k = 0;
    while (i <= mid && j <= end) {
        if (vec[i] < vec[j]) {
            temp[k++] = vec[i++];
        } else {
            temp[k++] = vec[j++];
        }
    }
    while (i <= mid) {
        temp[k++] = vec[i++];
    }
    while (j <= end) {
        temp[k++] = vec[j++];
    }
    k = 0;
    for (int i = start; i <= end; i++) {
        vec[i] = temp[k++];
    }
}

void merge_sort(vector<int> &vec, int start, int end) {
    if (start < end) {
        int mid = (start + end) / 2;
        merge_sort(vec, start, mid);
        merge_sort(vec, mid + 1, end);
        merge(vec, start, mid, end);
    }
}

void mergeSort(vector<int> &arr) {
    merge_sort(arr, 0, arr.size() - 1);
}
"""
        code = Code(
            code_string=cpp_code,
            language="cpp",
            background="window",  # "rectangle" or "window"
            add_line_numbers=True,
            line_numbers_from=1,
            formatter_style="monokai",  # or any: 'emacs', 'vim', 'dracula'...
            paragraph_config={"font": "Monospace", "font_size": 20},
            background_config={"stroke_color": WHITE, "fill_color": "#1e1e1e"},
        )
        code.scale(0.5)  # Try between 0.5 to 0.75
        self.play(FadeIn(code))
        self.wait(3)
