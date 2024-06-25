import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PIL import Image

class ImageConverter(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.btnBrowse.clicked.connect(self.browse)
        self.btnConvert.clicked.connect(self.convert_image)

        # Load custom style
        with open('style.qss', 'r') as f:
            self.setStyleSheet(f.read())

    def browse(self):
        file_dialog = QFileDialog()
        filename, _ = file_dialog.getOpenFileName(self, 'Open File', '', 'Image Files (*.png *.jpg *.jpeg)')
        if filename:
            self.filePath.setText(filename)

    def convert_image(self):
        file_path = self.filePath.text()
        if file_path:
            try:
                image = Image.open(file_path)
                output_format = self.formatCombo.currentText().lower()
                base_name = os.path.basename(file_path)
                output_file = os.path.splitext(base_name)[0] + '.' + output_format

                if image.mode == 'RGBA' and output_format in ['jpeg', 'jpg']:
                    image = image.convert('RGB')

                image.save(output_file)
                QMessageBox.information(self, 'Conversion Successful', f'Image converted and saved as {output_file}')
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'Error converting image: {str(e)}')
        else:
            QMessageBox.warning(self, 'Error', 'Please select an image file.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = ImageConverter()
    converter.show()
    sys.exit(app.exec())
