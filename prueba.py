import sys
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear el widget de la gráfica
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        # Agregar la gráfica al layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)

        # Crear el widget principal y establecer el layout
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        # Crear la gráfica
        ax = self.figure.add_subplot(111)
        ax.plot([0, 1, 2, 3, 4, 5], [0, 1, 4, 9, 16, 25], 'ro-')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_title('Title')

        # Actualizar la gráfica
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


