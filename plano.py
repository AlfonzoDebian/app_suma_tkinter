import tkinter as tk

class PlanoConCubo:
    def __init__(self, root):
        self.root = root
        self.root.title("Ubicar Cubo en el Plano Cartesiano")

        # Tamaño del canvas
        self.width = 600
        self.height = 600
        self.center_x = self.width // 2
        self.center_y = self.height // 2

        # Canvas
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="white")
        self.canvas.pack()

        # Ejes
        self.canvas.create_line(0, self.center_y, self.width, self.center_y, fill="black", width=2)  # X
        self.canvas.create_line(self.center_x, 0, self.center_x, self.height, fill="black", width=2)  # Y

        # Entradas para tamaño del cubo
        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Label(frame, text="Ancho:").grid(row=0, column=0)
        self.entry_ancho = tk.Entry(frame, width=5)
        self.entry_ancho.insert(0, "50")
        self.entry_ancho.grid(row=0, column=1)

        tk.Label(frame, text="Alto:").grid(row=0, column=2)
        self.entry_alto = tk.Entry(frame, width=5)
        self.entry_alto.insert(0, "50")
        self.entry_alto.grid(row=0, column=3)

        # Etiqueta de coordenadas
        self.label_info = tk.Label(root, text="Haz clic para ubicar el cubo", font=("Arial", 12))
        self.label_info.pack()

        # Evento de clic
        self.canvas.bind("<Button-1>", self.dibujar_cubo)

    def dibujar_cubo(self, event):
        try:
            ancho = int(self.entry_ancho.get())
            alto = int(self.entry_alto.get())
        except ValueError:
            self.label_info.config(text="⚠️ Ingresa valores numéricos válidos.")
            return

        # Coordenadas cartesianas
        x_cart = event.x - self.center_x
        y_cart = self.center_y - event.y

        # Dibujar cubo (rectángulo)
        x1 = event.x
        y1 = event.y
        x2 = x1 + ancho
        y2 = y1 + alto

        self.canvas.create_rectangle(x1, y1, x2, y2, outline="green", width=2)

        # Mostrar info
        self.label_info.config(
            text=f"Cubo en ({x_cart}, {y_cart}) | Ancho: {ancho} | Alto: {alto}"
        )

        # Etiqueta en el cubo
        self.canvas.create_text(x1 + ancho / 2, y1 + alto / 2, text=f"{ancho}x{alto}", fill="purple")

# Ejecutar app
if __name__ == "__main__":
    root = tk.Tk()
    app = PlanoConCubo(root)
    root.mainloop()
