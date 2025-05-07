import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2
import threading


class ImageProcessor:
    @staticmethod
    def adjust_brightness(img_array, value):
        hsv = cv2.cvtColor(img_array, cv2.COLOR_RGB2HSV)
        h, s, v = cv2.split(hsv)
        v = cv2.add(v, value)
        v = np.clip(v, 0, 255)
        return cv2.cvtColor(cv2.merge((h, s, v)), cv2.COLOR_HSV2RGB)

    @staticmethod
    def invert_image(img_array):
        return cv2.bitwise_not(img_array)

    @staticmethod
    def gamma_correction(img_array, gamma=1.0):
        inv_gamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** inv_gamma) * 255
                          for i in np.arange(0, 256)]).astype("uint8")
        return cv2.LUT(img_array, table)

    @staticmethod
    def log_transform(img_array):
        c = 255 / np.log(1 + np.max(img_array))
        log_image = c * (np.log(img_array + 1))
        return np.array(log_image, dtype=np.uint8)

    @staticmethod
    def median_filter(img_array, kernel_size):
        return cv2.medianBlur(img_array, kernel_size)

    @staticmethod
    def mean_filter(img_array, kernel_size):
        return cv2.blur(img_array, (kernel_size, kernel_size))


class PhotoshopClone:
    def __init__(self, root):
        self.root = root
        self.root.title("PyPhoto Editor Pro")
        self.root.geometry("1200x800")

        # Inisialisasi state
        self.original_image = None
        self.current_image = None
        self.filter_params = {
            "brightness": 0,
            "gamma": 1.0,
            "kernel_size": 3
        }
        self.undo_stack = []
        self.redo_stack = []

        # Setup UI
        self._setup_style()
        self._create_widgets()
        self._setup_bindings()
        self._toggle_controls(False)

    def _setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", padding=6, font=("Helvetica", 10))
        style.configure("TLabel", background="#333", foreground="white")
        style.configure("TFrame", background="#333")
        style.map("TScale",
                  troughcolor=[("active", "#444"), ("!active", "#444")],
                  sliderthickness=[("active", 15), ("!active", 15)]
                  )

    def _create_widgets(self):
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        left_panel = ttk.Frame(main_frame, width=250)
        left_panel.pack(side=tk.LEFT, fill=tk.Y)

        ttk.Button(left_panel, text="Buka Gambar",
                   command=self._open_image).pack(pady=10, fill=tk.X)
        ttk.Button(left_panel, text="Simpan Hasil",
                   command=self._save_image).pack(pady=10, fill=tk.X)

        # Tambahkan tombol undo/redo
        ttk.Button(left_panel, text="Undo",
                   command=self._undo).pack(pady=5, fill=tk.X)
        ttk.Button(left_panel, text="Redo",
                   command=self._redo).pack(pady=5, fill=tk.X)

        self._create_adjustment_panel(left_panel)

        self.canvas = tk.Canvas(main_frame, bg="#252526",
                                bd=0, highlightthickness=0)
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.split_line = self.canvas.create_line(
            0, 0, 0, 0, fill="yellow", width=2)

    def _create_adjustment_panel(self, parent):
        adjustment_frame = ttk.LabelFrame(parent, text="Adjustments")
        adjustment_frame.pack(pady=10, fill=tk.X)

        ttk.Label(adjustment_frame, text="Filter:").grid(
            row=0, column=0, sticky="w")
        self.filter_var = tk.StringVar()
        self.filter_menu = ttk.Combobox(
            adjustment_frame,
            textvariable=self.filter_var,
            values=[
                "Brightness",
                "Gamma",
                "Invert",
                "Log Transform",
                "Mean Filter",
                "Median Filter"
            ],
            state="readonly"
        )
        self.filter_menu.grid(row=0, column=1, sticky="ew", padx=5)

        self.kernel_scale = ttk.Scale(
            adjustment_frame,
            from_=3,
            to=15,
            command=lambda e: self._update_filter("kernel_size")
        )
        self.kernel_label = ttk.Label(adjustment_frame, text="Kernel Size:")

        self.brightness_scale = ttk.Scale(
            adjustment_frame,
            from_=-100,
            to=100,
            command=lambda e: self._update_filter("brightness")
        )
        self.brightness_label = ttk.Label(adjustment_frame, text="Brightness:")

        self.gamma_scale = ttk.Scale(
            adjustment_frame,
            from_=0.1,
            to=5.0,
            command=lambda e: self._update_filter("gamma")
        )
        self.gamma_label = ttk.Label(adjustment_frame, text="Gamma:")

    def _toggle_controls(self, visible):
        widgets = [
            self.brightness_label, self.brightness_scale,
            self.gamma_label, self.gamma_scale,
            self.kernel_label, self.kernel_scale
        ]
        for widget in widgets:
            widget.grid_remove()

        if visible:
            current_filter = self.filter_var.get()

            if current_filter == "Brightness":
                self.brightness_label.grid(row=1, column=0, sticky="w")
                self.brightness_scale.grid(
                    row=1, column=1, sticky="ew", padx=5)
            elif current_filter == "Gamma":
                self.gamma_label.grid(row=1, column=0, sticky="w")
                self.gamma_scale.grid(row=1, column=1, sticky="ew", padx=5)
            elif current_filter in ["Mean Filter", "Median Filter"]:
                self.kernel_label.grid(row=1, column=0, sticky="w")
                self.kernel_scale.grid(row=1, column=1, sticky="ew", padx=5)

    def _open_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        if path:
            try:
                self.original_image = np.array(Image.open(path))
                self.current_image = self.original_image.copy()
                self.undo_stack.clear()
                self.redo_stack.clear()
                self._update_canvas()
                self._toggle_controls(True)
            except Exception as e:
                messagebox.showerror(
                    "Error", f"Gagal membuka gambar: {str(e)}")

    def _update_filter(self, param_type):
        try:
            value = {
                "brightness": self.brightness_scale.get(),
                "gamma": self.gamma_scale.get(),
                "kernel_size": int(self.kernel_scale.get())
            }[param_type]

            if param_type == "kernel_size":
                value = value if value % 2 == 1 else value + 1
                self.filter_params[param_type] = value
                self.kernel_scale.set(value)

            self.filter_params[param_type] = value
            self._apply_filter()
        except KeyError:
            pass

    def _apply_filter(self):
        if self.original_image is None:
            return

        try:
            # Simpan state saat ini untuk undo
            self.undo_stack.append(self.current_image.copy())
            self.redo_stack.clear()

            current_filter = self.filter_var.get()

            # Terapkan filter ke current image
            if current_filter == "Brightness":
                self.current_image = ImageProcessor.adjust_brightness(
                    self.current_image,
                    int(self.filter_params["brightness"])
                )
            elif current_filter == "Gamma":
                self.current_image = ImageProcessor.gamma_correction(
                    self.current_image,
                    float(self.filter_params["gamma"])
                )
            elif current_filter == "Invert":
                self.current_image = ImageProcessor.invert_image(
                    self.current_image)
            elif current_filter == "Log Transform":
                self.current_image = ImageProcessor.log_transform(
                    self.current_image)
            elif current_filter == "Mean Filter":
                self.current_image = ImageProcessor.mean_filter(
                    self.current_image,
                    int(self.filter_params["kernel_size"])
                )
            elif current_filter == "Median Filter":
                self.current_image = ImageProcessor.median_filter(
                    self.current_image,
                    int(self.filter_params["kernel_size"])
                )

            self._update_canvas()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _update_canvas(self):
        if self.current_image is not None:
            try:
                img = Image.fromarray(self.current_image)
                img.thumbnail(
                    (self.canvas.winfo_width(), self.canvas.winfo_height()),
                    Image.Resampling.LANCZOS
                )
                self.tk_image = ImageTk.PhotoImage(img)
                self.canvas.delete("all")
                self.canvas.create_image(
                    self.canvas.winfo_width() // 2,
                    self.canvas.winfo_height() // 2,
                    anchor=tk.CENTER,
                    image=self.tk_image
                )
            except Exception as e:
                messagebox.showerror(
                    "Render Error", f"Gagal menampilkan gambar: {str(e)}")

    def _save_image(self):
        if self.current_image is not None:
            try:
                save_path = filedialog.asksaveasfilename(
                    defaultextension=".png",
                    filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")]
                )
                if save_path:
                    Image.fromarray(self.current_image).save(save_path)
                    messagebox.showinfo(
                        "Berhasil", f"Gambar disimpan di:\n{save_path}")
            except Exception as e:
                messagebox.showerror(
                    "Save Error", f"Gagal menyimpan gambar: {str(e)}")

    def _setup_bindings(self):
        self.filter_menu.bind("<<ComboboxSelected>>", self._on_filter_change)
        self.canvas.bind("<Motion>", self._update_split_view)
        self.canvas.bind("<Leave>", lambda e: self.canvas.coords(
            self.split_line, 0, 0, 0, 0))
        self.root.bind("<Control-o>", lambda e: self._open_image())
        self.root.bind("<Control-s>", lambda e: self._save_image())
        self.root.bind("<Control-z>", lambda e: self._undo())
        self.root.bind("<Control-y>", lambda e: self._redo())

    def _on_filter_change(self, event):
        current_filter = self.filter_var.get()
        self._toggle_controls(True)

        if current_filter == "Brightness":
            self.brightness_scale.set(0)
            self.filter_params["brightness"] = 0
        elif current_filter == "Gamma":
            self.gamma_scale.set(1.0)
            self.filter_params["gamma"] = 1.0
        elif current_filter in ["Mean Filter", "Median Filter"]:
            self.kernel_scale.set(3)
            self.filter_params["kernel_size"] = 3

        self._apply_filter()

    def _update_split_view(self, event):
        if self.current_image is not None and hasattr(self, 'tk_image'):
            x = event.x
            img_width = self.tk_image.width()
            canvas_width = self.canvas.winfo_width()
            x = max(0, min(x, img_width if img_width <
                           canvas_width else canvas_width))
            self.canvas.coords(self.split_line, x, 0, x,
                               self.canvas.winfo_height())

    def _undo(self):
        if len(self.undo_stack) > 0:
            self.redo_stack.append(self.current_image)
            self.current_image = self.undo_stack.pop()
            self._update_canvas()

    def _redo(self):
        if len(self.redo_stack) > 0:
            self.undo_stack.append(self.current_image)
            self.current_image = self.redo_stack.pop()
            self._update_canvas()


if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoshopClone(root)
    root.mainloop()
