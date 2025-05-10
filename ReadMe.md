# Untitled

```markdown
# Sorting Algorithm Visualizer in Python

This is a Python-based interactive application that allows users to **input arrays**, choose among three classic **sorting algorithms** (Quick Sort, Merge Sort, Insertion Sort), and **analyze their performance** under different input scenarios (Best, Worst, and Average cases). It also measures execution time and can visualize the results.

---

## 📌 Project Objectives

- Implement Quick Sort, Merge Sort, and Insertion Sort in Python.
- Analyze and compare the **time complexity** in Best, Worst, and Average cases.
- Allow the user to interactively input arrays and choose sorting algorithms.
- Visualize sorting results and execution times.

---

## 📁 Project Structure

```

SortingAlgorithmApp/

├── sorting_algorithms.py   # Sorting algorithm implementations

├── analysis.py             # Case generation and timing functions

├── gui.py                  # GUI logic (Tkinter or PyQt6)

├── main.py                 # Application entry point

├── utils.py                # (Optional) Helper functions

├── requirements.txt        # List of required libraries

└── README.md               # Project documentation

```

---

## 🚀 Features

- Manual input of one or more arrays.
- Option to choose the sorting algorithm (Quick, Merge, or Insertion).
- Automatic generation of:
  - Best-case (sorted array)
  - Worst-case (reversed array)
  - Average-case (randomly shuffled array)
- Timing of sorting operations using the built-in `time` library.
- Visual comparison of algorithm performance (optional charts with `matplotlib`).
- Simple and user-friendly interface (built using `tkinter` or `PyQt6`).

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SortingAlgorithmApp.git
cd SortingAlgorithmApp

```

### 2. Install Required Libraries

```bash
pip install -r requirements.txt

```

If you didn’t generate a `requirements.txt` file yet, you can use:

```bash
pip install matplotlib seaborn PyQt6

```

(Tkinter is built-in with Python.)

---

## 🧠 Sorting Algorithms

### ✅ Quick Sort

- **Best Case:** O(n log n)
- **Worst Case:** O(n²)
- **Average Case:** O(n log n)

### ✅ Merge Sort

- **All Cases:** O(n log n)

### ✅ Insertion Sort

- **Best Case:** O(n)
- **Worst/Average Case:** O(n²)

---

## 📊 How Performance is Measured

- Time is measured using Python’s `time.time()` before and after the algorithm is run.
- Arrays are tested in three conditions:
    - **Sorted (Best Case)**
    - **Reversed (Worst Case)**
    - **Random Order (Average Case)**

---

## 🖼️ (Optional) Data Visualization

If `matplotlib` is installed, the app can generate comparison charts showing execution times for each algorithm and case.

---

## 🧪 Example Usage

```bash
python main.py

```

Then follow the GUI prompts to:

- Enter an array
- Select a sorting algorithm
- View sorted outputs and timing for different input types

---

## 📘 Report Guidelines

You can use this app to generate:

- Code explanations (well-commented)
- Test case outputs
- Time complexity tables (from measured timings)
- Graphs/charts for performance comparison

---

## ✍️ Author

- Nada Elmokdem
- Project for Design and analysis of algorithm

---

## 📄 License

This project is for educational purposes. You may adapt or extend it for learning or academic projects.