import sys

from PyQt5.QtCore import (
    QRect,
    QSize,
    )

import beam

from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QLineEdit,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
    
    )

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ENG 104 Extra Credit App")
        # Create a top-level layout
        self.layout = QVBoxLayout()
        self.setFixedHeight(400)
        self.setFixedWidth(900)
        self.setLayout(self.layout)
        
        # Create the stacked layout
        self.stackedLayout = QStackedLayout()
        # Create the first page
        self.page1 = QWidget()
        self.page1Layout = QFormLayout()
        self.page1Layout.addRow(QLabel("What Type of problem would you like solved?"))
        self.axButton = QPushButton("Axial Load")
        self.axButton.clicked.connect(self.switchPage)
        self.page1Layout.addRow(self.axButton)
        self.page1Layout.addRow(QPushButton("Other Stuff"))
        self.page1.setLayout(self.page1Layout)
        self.stackedLayout.addWidget(self.page1)
        # Create the second page
        self.page2 = QWidget()
        self.page2Layout = QFormLayout()
        self.page2Layout.addRow(QLabel("Please list all external forces on member: "))
        self.forceInput = QLineEdit()
        self.forceInput.setFixedSize(QSize(100,20))
        self.positionInput = QLineEdit()
        self.positionInput.setFixedSize(QSize(100,20))
        self.page2Layout.addRow("Force: ", self.forceInput)
        self.page2Layout.addRow("position: ", self.positionInput)
        self.addButton = QPushButton("Add")
        self.addButton.setFixedSize(150,30)
        self.page2Layout.addRow(self.addButton)
        self.page2.setLayout(self.page2Layout)
        self.stackedLayout.addWidget(self.page2)
        # Add the combo box and the stacked layout to the top-level layout
        self.layout.addLayout(self.stackedLayout)

    def switchPage(self):
        self.stackedLayout.setCurrentWidget(self.page2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())