import sys
from PyQt5.QtWidgets import QApplication
from converter_window import ConverterWindow

def main():
    app = QApplication(sys.argv)
    
    # Apply basic styling at app level
    app.setStyle("Fusion")  # Use Fusion style for modern look
    
    window = ConverterWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()