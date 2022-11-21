import sys

from PyQt5.QtCore import (
    QRect,
    QSize,
    Qt
    )



import beam

from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QLineEdit,
    QStackedLayout,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
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
        self.page2Layout = QVBoxLayout()
        self.page2Layout.setSizeConstraint()
        
        self.decBox = QWidget()
        self.page2Layout.addWidget(self.decBox, 1,3)
        
        
        #Title decleration, insertion and styling
        self.title = QLabel("Please List All External Forces on Member")
        self.title.setFixedSize(400,20)
        self.page2Layout.setVerticalSpacing(5)
        self.page2Layout.addWidget(self.title, alignment=Qt.AlignCenter)
        self.title.setStyleSheet("padding: 0px;" 
                                "font-family: Times-New-Roman;"
                                "font-size: 20px;"
                                "font-weight: vold;")
       
       #Textbox for force 
        self.forceInput = QLineEdit()
        self.forceInput.setFixedSize(QSize(100,20))

        #Textbox for position
        self.positionInput = QLineEdit()
        self.positionInput.setFixedSize(QSize(100,20))

        #box styling

        self.setStyleSheet("QLineEdit: {border-radius: 5px; } ")

        self.fLabel = QLabel("Force: ")
        self.fLabel.setStyleSheet("font-size: 16px;"
                                "font-family: Times-new-roman;")

        self.pLabel = QLabel("Position: ")
        self.pLabel.setStyleSheet("font-size: 16px;"
                                "font-family: Times-new-roman;")
        self.forceRow = QWidget()
        self.forceRow.setLayout(QHBoxLayout())
        self.forceRow.layout().addWidget(self.fLabel)
        self.forceRow.layout().addWidget(self.forceInput)

        
        
        
        self.positionRow = QWidget()
        self.positionRow.setLayout(QHBoxLayout())
        self.page2Layout.addWidget(self.fLabel, 1,0,alignment=Qt.AlignLeft)
        self.page2Layout.addWidget(self.forceInput,1,0,alignment=Qt.AlignHCenter)
        self.page2Layout.addWidget(self.pLabel,2,0, alignment=Qt.AlignLeft)
        self.page2Layout.addWidget(self.positionInput, 2,0,alignment=Qt.AlignHCenter)
        self.addButton = QPushButton("Add")
        self.addButton.setFixedSize(150,30)
        self.addButton.clicked.connect(self.appendInputText)
        self.page2Layout.addWidget(self.addButton, 3,0, alignment=Qt.AlignRight)

        self.inputsLayout = QVBoxLayout()
        self.page2Layout.addLayout(self.inputsLayout,0,3)


        self.page2.setLayout(self.page2Layout)
        self.stackedLayout.addWidget(self.page2)
        # Add the combo box and the stacked layout to the top-level layout
        self.layout.addLayout(self.stackedLayout)

    def switchPage(self):
        self.stackedLayout.setCurrentWidget(self.page2)

    def appendInputText(self):
        #Store and add input values to chart
        forceInput =QLabel(self.forceInput.text())
        positionInput = QLabel(self.positionInput.text())
        forceInput.setAlignment(Qt.AlignLeft)
        positionInput.setAlignment(Qt.AlignRight) 
        self.inputsLayout.addWidget(forceInput)
        self.inputsLayout.addWidget(positionInput)

        #Delete values in the textbox's

        self.forceInput.setText("") 
        self.positionInput.setText("")       


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())