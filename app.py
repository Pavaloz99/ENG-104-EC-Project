import sys

from PyQt5.QtCore import (
    QRect,
    QSize,
    Qt,
    QPoint
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
        
        
        
        #Title decleration, insertion and styling
        self.zeroRow = QWidget()
        self.zeroRow.setLayout(QHBoxLayout())
        self.title = QLabel("List All External Forces on Member")
        self.title.setFixedSize(400,25)

        self.title2 = QLabel("List All Supports Acting on the Member")
        self.title2.setStyleSheet("padding: 0px;" 
                                "font-family: Times-New-Roman;"
                                "font-size: 20px;"
                                "font-weight: Bold;")
        self.title2.setFixedSize(400,20)
    
        self.zeroRow.layout().addWidget(self.title, alignment=Qt.AlignLeft)
        self.title.setStyleSheet("padding: 0px;" 
                                "font-family: Times-New-Roman;"
                                "font-size: 20px;"
                                "font-weight: Bold;")
        
        self.zeroRow.layout().addWidget(self.title2, alignment = Qt.AlignRight)
        self.page2Layout.addWidget(self.zeroRow)
       
       #Textbox for force 
        self.forceInput = QLineEdit()
        self.forceInput.setFixedSize(QSize(70,20))
        

        #Textbox for position
        self.positionInput = QLineEdit()
        self.positionInput.setFixedSize(QSize(70,20))

        #box styling
        self.setStyleSheet("QLineEdit: {border-radius: 30px; } ")

        self.fLabel = QLabel("Force: ")
        self.fLabel.setStyleSheet("font-size: 16px;"
                                "font-family: Times-new-roman;")

        self.pLabel = QLabel("Position: ")
        self.pLabel.setStyleSheet("font-size: 16px;"
                                "font-family: Times-new-roman;")
        self.rowOne = QWidget()
        self.rowOne.setLayout(QHBoxLayout())
        self.rowOneFirstHalf = QWidget()
        self.rowOneFirstHalf.setLayout(QHBoxLayout())
        self.rowOneSecondHalf = QWidget()
        self.rowOneSecondHalf.setLayout(QHBoxLayout())
        self.rowOne.layout().addWidget(self.rowOneFirstHalf)
        self.rowOne.layout().addWidget(self.rowOneSecondHalf)
        
        
        self.rowOneFirstHalf.setContentsMargins(0,10,120,200)
        self.rowOneFirstHalf.layout().setSpacing(20)
        self.rowOneSecondHalf.setContentsMargins(0,0, 50, 200)
        self.rowOneSecondHalf.layout().setSpacing(20)
        
        #Force Label and Textbox
        self.rowOneFirstHalf.layout().addWidget(self.fLabel)
        self.rowOneFirstHalf.layout().addWidget(self.forceInput)
        
        #Position label and textbox
        self.rowOneFirstHalf.layout().addWidget(self.pLabel)
        self.rowOneFirstHalf.layout().addWidget(self.positionInput)
        #Button
        self.addButton = QPushButton("Add")
        self.addButton.clicked.connect(self.appendInputText)
        self.addButton.setFixedSize(50,30)

        self.supportType = QComboBox()
        self.supportType.addItems(["-Select-","Pin Support", "Roller Support", "Fixed End"])
        self.supportType.setFixedSize(100, 30)
        
        
        self.pLabel2 = QLabel("Position: ")
        self.pLabel2.setStyleSheet("font-size: 16px;"
                                "font-family: Times-new-roman;")

        self.positionInput2 = QLineEdit()
        self.positionInput2.setFixedSize(QSize(70,20))

        self.rowOneFirstHalf.layout().addWidget(self.addButton)

        
        self.rowOneSecondHalf.layout().addWidget(self.pLabel2)
        self.rowOneSecondHalf.layout().addWidget(self.positionInput2)
        self.rowOneSecondHalf.layout().addWidget(self.supportType)

   
        
        
        self.page2Layout.addWidget(self.rowOne)



        
        
        
        self.secondRow = QWidget()

        
        # self.page2Layout.addLayout(self.inputsLayout,0,3)


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