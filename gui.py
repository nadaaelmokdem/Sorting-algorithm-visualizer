import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import webbrowser
import sorting_algorithms
import analysis

class SortingAppTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        self.root.configure(bg='#333333')  # Lighter black for main window

        # --- Icon ---
        try:
            # Use a more reliable method to set the icon
            self.root.iconbitmap("icon.ico")  # If the file is in the same directory
        except Exception as e:
            print(f"Error setting icon: {e}")
            # You can choose to log the error or show a message to the user

        # --- Style Configuration ---
        style = ttk.Style()
        style.theme_use('default')

        style.configure('TFrame', background='#333333')  # Lighter black for frames
        style.configure('TLabel', background='#333333', foreground='white', font=('Helvetica', 12))
        style.configure('TButton', background='#333333', foreground='white', font=('Helvetica', 12), padding=10)
        style.map('TButton', background=[('active', 'gray')])
        style.configure('TEntry', fieldbackground='#444444', font=('Helvetica', 18), foreground='white')  # Lighter black for entry
        style.configure('TCombobox', fieldbackground='white', background='#333333', font=('Helvetica', 12))  # Lighter black for combobox
        style.configure('Status.TLabel', background='#333333', foreground='white', font=('Helvetica', 11))
        style.configure('Header.TLabel', background='#333333', foreground='white', font=('Helvetica', 24, 'bold'))

        # --- Main Frame ---
        main_frame = ttk.Frame(root, padding="20", style='TFrame')
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # --- Header Frame (Title & Clickable Link) ---
        header_frame = ttk.Frame(main_frame, padding="10", style='TFrame')
        header_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E))

        self.title_label = ttk.Label(header_frame, text="Sorting Algorithm Visualizer", style='Header.TLabel')
        self.title_label.pack(anchor=tk.CENTER)

        self.link_label = tk.Label(header_frame, text="Link from here", fg="lightblue", bg="#333333",
                                    font=('Arial', 12, 'italic'), cursor="hand2")
        self.link_label.pack(anchor=tk.CENTER, pady=(0, 10))
        self.link_label.bind("<Button-1>", lambda _: self.open_link())

        # --- Input Frame ---
        input_frame = ttk.Frame(main_frame, padding="10", borderwidth=2, relief=tk.GROOVE, style='TFrame')
        input_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=(0, 10))

        ttk.Label(input_frame, text="Enter array (comma-separated):", style='TLabel').grid(row=0, column=0, sticky=tk.W, pady=2)
        self.array_entry = ttk.Entry(input_frame, width=40)
        self.array_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=2)

        self.generate_random_button = ttk.Button(input_frame, text="Generate Random Array", command=self.generate_random_array)
        self.generate_random_button.grid(row=1, column=0, sticky=tk.W, pady=2, padx=(0, 10))

        ttk.Label(input_frame, text="Array Size:", style='TLabel').grid(row=1, column=1, sticky=tk.W, pady=2)
        self.array_size_entry = ttk.Entry(input_frame, width=10)
        self.array_size_entry.grid(row=1, column=2, sticky=(tk.W, tk.E), pady=2)
        self.array_size_entry.insert(0, "10")

        # --- Algorithm Selection Frame ---
        algorithm_frame = ttk.Frame(main_frame, padding="10", borderwidth=2, relief=tk.GROOVE, style='TFrame')
        algorithm_frame.grid(row=1, column=1, sticky=(tk.W, tk.E))

        ttk.Label(algorithm_frame, text="Select Algorithm:", style='TLabel').grid(row=0, column=0, sticky=tk.W, pady=2)
        self.algorithm_var = tk.StringVar()
        self.algorithm_combobox = ttk.Combobox(algorithm_frame, textvariable=self.algorithm_var,
                                             values=["Quick Sort", "Merge Sort", "Insertion Sort"],
                                             state="readonly")
        self.algorithm_combobox.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=2)
        self.algorithm_combobox.current(0)

        self.sort_button = ttk.Button(algorithm_frame, text="Sort", command=self.run_sort)
        self.sort_button.grid(row=0, column=2, sticky=tk.W, pady=2, padx=(10, 0))

        # --- Output Frame ---
        output_frame = ttk.Frame(main_frame, padding="10", borderwidth=2, relief=tk.GROOVE, style='TFrame')
        output_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.N, tk.S, tk.E, tk.W), pady=(10, 0))

        ttk.Label(output_frame, text="Output:", style='TLabel').grid(row=0, column=0, sticky=tk.W, pady=2)
        self.output_text = scrolledtext.ScrolledText(output_frame, width=90, height=20, wrap=tk.WORD, font=('Arial', 12))
        self.output_text.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=2)
        self.output_text.config(state=tk.DISABLED, bg='#333333', fg='white', insertbackground='white')  # Lighter black

        # --- Status Bar ---
        self.status_var = tk.StringVar()
        self.status_label = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W, style='Status.TLabel')
        self.status_label.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        self.status_var.set("Ready")

        # --- Menu ---
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=helpmenu)
        root.config(menu=menubar)

        # --- Layout Config ---
        root.columnconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        output_frame.columnconfigure(0, weight=1)

    def generate_random_array(self):
        try:
            size = int(self.array_size_entry.get())
            if size <= 0:
                self.display_error("Array size must be positive.")
                return
            random_array = analysis.generate_random_array(size)
            self.array_entry.delete(0, tk.END)
            self.array_entry.insert(0, ','.join(map(str, random_array)))
            self.status_var.set("Random array generated.")
        except ValueError:
            self.display_error("Invalid array size. Please enter a valid number.")

    def run_sort(self):
        input_text = self.array_entry.get()
        algorithm_name = self.algorithm_var.get()

        try:
            arr = list(map(int, input_text.split(',')))
        except ValueError:
            self.display_error("Invalid input. Please enter comma-separated integers.")
            return

        if not arr:
            self.display_error("Input array is empty.")
            return

        if algorithm_name == "Quick Sort":
            sort_function = sorting_algorithms.quick_sort
        elif algorithm_name == "Merge Sort":
            sort_function = sorting_algorithms.merge_sort
        elif algorithm_name == "Insertion Sort":
            sort_function = sorting_algorithms.insertion_sort
        else:
            self.display_error("Invalid algorithm selected.")
            return

        self.status_var.set(f"Running {algorithm_name}...")
        self.root.update_idletasks()

        try:
            results = analysis.run_and_analyze_sort(sort_function, arr)
            self.display_results(results, algorithm_name)
            self.status_var.set(f"{algorithm_name} completed.")
        except Exception as e:
            self.display_error(f"An error occurred: {e}")

    def display_results(self, results, algorithm_name):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"Results for {algorithm_name}:\n\n")
        self.output_text.insert(tk.END, f"Original Array: {results['original_array']}\n\n")
        self.output_text.insert(tk.END, f"Best Case: {results['best_case_array']}\nTime: {results['best_case_time']:.6f} seconds\n\n")
        self.output_text.insert(tk.END, f"Worst Case: {results['worst_case_array']}\nTime: {results['worst_case_time']:.6f} seconds\n\n")
        self.output_text.insert(tk.END, f"Average Case: {results['average_case_array']}\nTime: {results['average_case_time']:.6f} seconds\n")
        self.output_text.config(state=tk.DISABLED)

    def display_error(self, message):
        self.status_var.set(f"Error: {message}")
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"Error: {message}\n")
        self.output_text.config(state=tk.DISABLED)

    def show_about(self):
        about_message = "Sorting Algorithm Visualizer\n\n" \
                        "Visualize and compare the performance of sorting algorithms.\n" \
                        "Implemented: Quick Sort, Merge Sort, Insertion Sort.\n" \
                        "Theme: Black\n" \
                        "Developed by Nada Elmokdem\n"
        messagebox.showinfo("About", about_message)

    def open_link(self):
        webbrowser.open_new("https://github.com/nadaaelmokdem/Sorting-algorithm-visualizer.git")

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingAppTkinter(root)
    root.mainloop()
