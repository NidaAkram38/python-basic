import sys
import re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit,
    QVBoxLayout, QHBoxLayout, QGridLayout, QProgressBar, QMessageBox, QScrollArea, QSizePolicy
)
from PyQt5.QtCore import Qt, QTimer

# ---------------------------
# Simple word -> number map (no external lib)
# Supports zero..ninety and hyphenated like 'twenty-five'
# ---------------------------
WORD_MAP = {
    "zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,
    "ten":10,"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19,
    "twenty":20,"thirty":30,"forty":40,"fifty":50,"sixty":60,"seventy":70,"eighty":80,"ninety":90
}

def word_to_num(word: str) -> int:
    word = word.strip().lower()
    if not word:
        raise ValueError("Empty input")
    # direct int?
    if re.fullmatch(r"-?\d+", word):
        return int(word)
    # handle hyphen (twenty-five)
    if '-' in word:
        parts = word.split('-')
        total = 0
        for p in parts:
            if p in WORD_MAP:
                total += WORD_MAP[p]
            else:
                raise ValueError(f"Unknown word '{p}'")
        return total
    # handle space separated like "twenty five"
    if ' ' in word:
        parts = word.split()
        total = 0
        for p in parts:
            if p in WORD_MAP:
                total += WORD_MAP[p]
            else:
                raise ValueError(f"Unknown word '{p}'")
        return total
    # single word
    if word in WORD_MAP:
        return WORD_MAP[word]
    raise ValueError(f"Unknown word '{word}'")

def parse_number_input(value: str, allow_zero=True, positive_only=False):
    """
    Tries to parse user input which might be digits or words.
    Raises ValueError on invalid.
    """
    val = word_to_num(value)
    if positive_only and val < 0:
        raise ValueError("Negative not allowed")
    if not allow_zero and val == 0:
        raise ValueError("Zero not allowed")
    return val

# ---------------------------
# Main GUI
# ---------------------------
class BucketApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bucket Water Redistributor — PyQt")
        self.setMinimumSize(820, 620)
        self.setStyleSheet("""
            QWidget { background: #0f1720; color: #e6eef6; font-family: Arial; }
            QLabel#title { color: #7ef0c7; font-size: 20px; font-weight: bold; }
            QLineEdit { background: #111827; border: 1px solid #264653; padding: 6px; color: #e6eef6; border-radius: 6px; }
            QPushButton { background:#2a9d8f; color: #042a2b; padding: 8px; border-radius:8px; font-weight:600; }
            QPushButton:hover { background:#21a48e; }
            QTextEdit { background:#071015; border:1px solid #264653; color:#cfeee0; border-radius:6px; padding:6px; }
        """)
        self.bucket_size_entries = []
        self.bucket_water_entries = []
        self.progress_bars = []
        self.num_buckets = 0
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()

        header = QLabel("Bucket Water Redistribution")
        header.setObjectName("title")
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)

        # controls row
        ctrl_layout = QHBoxLayout()
        lbl = QLabel("Number of buckets:")
        self.num_buckets_edit = QLineEdit()
        self.num_buckets_edit.setPlaceholderText("e.g. 3 or three")
        btn_create = QPushButton("Create Inputs")
        btn_create.clicked.connect(self.on_create_inputs)
        ctrl_layout.addWidget(lbl)
        ctrl_layout.addWidget(self.num_buckets_edit, 1)
        ctrl_layout.addWidget(btn_create)
        main_layout.addLayout(ctrl_layout)

        # scroll area for dynamic bucket inputs and progressbars
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout()
        scroll_content.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(scroll_content)
        main_layout.addWidget(self.scroll_area, 1)

        # Buttons row
        btn_layout = QHBoxLayout()
        self.btn_calculate = QPushButton("Calculate & Animate")
        self.btn_calculate.clicked.connect(self.on_calculate)
        self.btn_clear = QPushButton("Clear")
        self.btn_clear.clicked.connect(self.on_clear)
        btn_layout.addWidget(self.btn_calculate)
        btn_layout.addWidget(self.btn_clear)
        main_layout.addLayout(btn_layout)

        # output text
        out_label = QLabel("Summary & Redistribution Log:")
        main_layout.addWidget(out_label)
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setFixedHeight(200)
        main_layout.addWidget(self.output)

        self.setLayout(main_layout)

    def on_create_inputs(self):
        # clear previous
        for w in self.scroll_layout.children():
            pass
        # remove old widgets
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()
        self.bucket_size_entries.clear()
        self.bucket_water_entries.clear()
        self.progress_bars.clear()

        # parse number of buckets
        try:
            n = parse_number_input(self.num_buckets_edit.text(), allow_zero=False, positive_only=True)
            if n <= 0:
                raise ValueError("Number of buckets must be > 0")
        except Exception as e:
            QMessageBox.warning(self, "Invalid input", f"Enter valid number of buckets.\n{e}")
            return

        self.num_buckets = n
        grid = QGridLayout()

        header_labels = ["Bucket", "Size (capacity)", "Initial water", "Fill Animation"]
        for c, text in enumerate(header_labels):
            lbl = QLabel(f"<b>{text}</b>")
            grid.addWidget(lbl, 0, c)

        # create rows
        for i in range(n):
            lbl = QLabel(f"Bucket {i+1}")
            size_edit = QLineEdit()
            size_edit.setPlaceholderText("e.g. 10 or ten")
            water_edit = QLineEdit()
            water_edit.setPlaceholderText("e.g. 5 or five")
            prog = QProgressBar()
            prog.setRange(0, 100)   # percent; we'll map later
            prog.setValue(0)
            prog.setTextVisible(True)
            prog.setFormat("0%")

            grid.addWidget(lbl, i+1, 0)
            grid.addWidget(size_edit, i+1, 1)
            grid.addWidget(water_edit, i+1, 2)
            grid.addWidget(prog, i+1, 3)

            self.bucket_size_entries.append(size_edit)
            self.bucket_water_entries.append(water_edit)
            self.progress_bars.append(prog)

        self.scroll_layout.addLayout(grid)
        # small tip
        tip = QLabel("Tip: You can type numeric words like 'five' or 'twenty-one' or digits like '21'.")
        tip.setStyleSheet("color:#9ad3c8; margin-top:8px;")
        self.scroll_layout.addWidget(tip)

    def on_clear(self):
        self.num_buckets_edit.clear()
        self.output.clear()
        # clear dynamic widgets
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            w = item.widget()
            if w: w.deleteLater()
        self.bucket_size_entries.clear()
        self.bucket_water_entries.clear()
        self.progress_bars.clear()
        self.num_buckets = 0

    def on_calculate(self):
        # parse inputs with validation
        try:
            n = self.num_buckets
            if n <= 0:
                raise ValueError("Create inputs first (press Create Inputs).")
            sizes = []
            waters = []
            for i in range(n):
                s_text = self.bucket_size_entries[i].text()
                w_text = self.bucket_water_entries[i].text()
                s = parse_number_input(s_text, allow_zero=False, positive_only=True)
                w = parse_number_input(w_text, allow_zero=True, positive_only=True)
                if s == 0:
                    raise ValueError(f"Bucket {i+1} size cannot be zero.")
                if w < 0:
                    raise ValueError(f"Bucket {i+1} water cannot be negative.")
                sizes.append(s)
                waters.append(w)
        except Exception as e:
            QMessageBox.warning(self, "Invalid input", str(e))
            return

        # Copy arrays (we will mutate waters)
        bucket_sizes = list(sizes)
        water_levels = list(waters)

        # Prepare logs
        initial_extra = {}
        redistribution_log = {f"Bucket {i+1}": 0 for i in range(n)}

        # Step 1: detect overflow and cap, collect extra
        overflow_list = []
        for i in range(n):
            if water_levels[i] > bucket_sizes[i]:
                extra = water_levels[i] - bucket_sizes[i]
                initial_extra[f"Bucket {i+1}"] = extra
                water_levels[i] = bucket_sizes[i]
                overflow_list.append((i, extra))

        # Step 2: redistribute extras (first-fit)
        for idx, extra in overflow_list:
            if extra <= 0:
                continue
            for j in range(n):
                if j == idx: 
                    continue
                space = bucket_sizes[j] - water_levels[j]
                if space > 0:
                    transfer = min(space, extra)
                    water_levels[j] += transfer
                    redistribution_log[f"Bucket {j+1}"] += transfer
                    extra -= transfer
                if extra <= 0:
                    break
            # leftover extra (if any) remains (we'll show in summary)

        # Step 3: compute classification and remaining capacity
        full = []
        empty = []
        partial = []
        remaining_capacity = []
        for i in range(n):
            if water_levels[i] == bucket_sizes[i]:
                full.append(i+1)
                remaining_capacity.append(0)
            elif water_levels[i] == 0:
                empty.append(i+1)
                remaining_capacity.append(bucket_sizes[i])
            else:
                partial.append(i+1)
                remaining_capacity.append(bucket_sizes[i] - water_levels[i])

        # Prepare summary text
        summary_lines = []
        summary_lines.append("___Summary___")
        summary_lines.append(f"Full buckets: {full}")
        summary_lines.append(f"Empty buckets: {empty}")
        summary_lines.append(f"Partially filled buckets: {partial}")
        summary_lines.append(f"Remaining capacity in each bucket: {remaining_capacity}")
        if initial_extra:
            summary_lines.append("")
            summary_lines.append("Initial extra water (before redistribution):")
            for b, ex in initial_extra.items():
                summary_lines.append(f"  {b}: {ex} litres")
        summary_lines.append("")
        summary_lines.append("Redistribution result (extra water added to each bucket):")
        for b, added in redistribution_log.items():
            if added > 0:
                summary_lines.append(f"  {b}: {added} litres")
        summary_lines.append("")
        summary_lines.append("Final water levels in each bucket:")
        for i in range(n):
            summary_lines.append(f"  Bucket {i+1}: {water_levels[i]} litres")

        # Display summary text
        self.output.setPlainText("\n".join(summary_lines))

        # Animate progress bars to reflect percentage filled
        # Calculate percent mapping
        percents = []
        for i in range(n):
            pct = int(round((water_levels[i] / bucket_sizes[i]) * 100)) if bucket_sizes[i] > 0 else 0
            percents.append(pct)

        # Animate using QTimer incremental updates
        self.animate_progress(percents)

    def animate_progress(self, target_percents):
        # Reset progress bars first
        for p in self.progress_bars:
            p.setValue(0)
            p.setFormat("0%")

        self._anim_index = 0
        self._target = target_percents
        self._timer = QTimer(self)
        self._timer.setInterval(12)  # small step speed
        self._timer.timeout.connect(self._step_animation)
        self._timer.start()

    def _step_animation(self):
        done = True
        for i, prog in enumerate(self.progress_bars):
            cur = prog.value()
            if cur < self._target[i]:
                prog.setValue(cur + 1)
                prog.setFormat(f"{prog.value()}%")
                done = False
        if done:
            self._timer.stop()

# ---------------------------
# Run App
# ---------------------------
def main():
    app = QApplication(sys.argv)
    win = BucketApp()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
