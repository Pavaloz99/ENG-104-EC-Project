import sys

from PyQt5.QtCore import (
    QRect,
    QSize,
    Qt,
    QPoint,
    
    )



from PyQt5.QtGui import (QPalette,
                        QColor,
)

from beam import beam

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
    QScrollArea,
    QSizePolicy,
    
    )




class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.myBeam = beam()
        self.setWindowTitle("ENG 104 Extra Credit App")
        # Create a top-level layout
        self.layout = QVBoxLayout()
        self.setFixedHeight(500)
        self.setFixedWidth(1000)
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
        self.page1Layout.addRow(QPushButton("Torsion"))
        self.page1.setLayout(self.page1Layout)
        self.stackedLayout.addWidget(self.page1)
        # Create the second page
        self.page2 = QWidget()
        self.page2Layout = QVBoxLayout()
        
        
        
        #Title decleration, insertion and styling
        self.zeroRow = QWidget()
        self.zeroRow.setLayout(QHBoxLayout())
        self.zeroRow.setFixedHeight(50)
        self.title = QLabel("List All External Forces on Member")
        self.title.setFixedSize(400,25)

        self.title2 = QLabel("List All Supports Acting on the Member")
        self.title2.setStyleSheet("padding: 0px;" 
                                "font-family: Times-New-Roman;"
                                "font-size: 20px;"
                                "font-weight: Bold;")
        self.title2.setFixedSize(400,25)
    
        self.zeroRow.layout().addWidget(self.title, alignment=Qt.AlignLeft and Qt.AlignVCenter)
        self.title.setStyleSheet("padding: 0px;" 
                                "font-family: Times-New-Roman;"
                                "font-size: 20px;"
                                "font-weight: Bold;")
        
        self.zeroRow.layout().addWidget(self.title2, alignment = Qt.AlignRight and Qt.AlignVCenter)
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
        self.fLabel.setFixedWidth(70)
        self.fLabel.setStyleSheet("font-size: 16px;"
                                "font-family: Times-new-roman;")

        self.pLabel = QLabel("Position:")
        self.pLabel.setFixedWidth(70)
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
        self.rowOne.layout().setAlignment(Qt.AlignTop)

        

        self.rowOne.setFixedHeight(70)
        
  
        self.rowOneFirstHalf.layout().setSpacing(3)

        self.rowOneSecondHalf.layout().setSpacing(3)
        
        #Force Label and Textbox
        self.rowOneFirstHalf.layout().addWidget(self.fLabel)
        self.rowOneFirstHalf.layout().addWidget(self.forceInput)
        
        #Position label and textbox
        self.rowOneFirstHalf.layout().addWidget(self.pLabel)
        self.rowOneFirstHalf.layout().addWidget(self.positionInput)
        #Button
        self.addButton = QPushButton("Add")
        self.addButton.clicked.connect(self.appendExForceText)
        self.addButton.setFixedSize(50,30)

        self.addButtonPos = QPushButton("Add")
        self.addButtonPos.clicked.connect(self.appendSupportText)
        self.addButtonPos.setFixedSize(50,30)

        self.supportType = QComboBox()
        self.supportType.addItems(["-Select-","Pin Support", "Roller Support", "Fixed End"])
        self.supportType.setFixedSize(100, 30)
        
        
        self.pLabel2 = QLabel("Position:")
        self.pLabel2.setFixedWidth(70)
        self.pLabel2.setStyleSheet("font-size: 16px;"
                                "font-family: Times-new-roman;")

        self.positionInput2 = QLineEdit()
        self.positionInput2.setFixedSize(QSize(50,20))

        self.rowOneFirstHalf.layout().addWidget(self.addButton)

        
        self.rowOneSecondHalf.layout().addWidget(self.pLabel2)
        self.rowOneSecondHalf.layout().addWidget(self.positionInput2)
        self.rowOneSecondHalf.layout().addWidget(self.supportType)
        self.rowOneSecondHalf.layout().addWidget(self.addButtonPos)



    
        
        
        self.page2Layout.addWidget(self.rowOne)



        
        
        
        self.secondRow = QWidget()


        #Defining each column for the fourth row
        self.secondRow1 = QWidget()
        self.secondRow2 = QWidget()
        self.secondRow3 = QWidget()
        self.secondRow4 = QWidget()


   
        




        self.secondRowContainer1 = QWidget()
        self.secondRowContainer1.setLayout(QHBoxLayout())
      

        self.secondRowContainer2 = QWidget()
        self.secondRowContainer2.setLayout(QHBoxLayout())
    




        self.secondRow1.setLayout(QVBoxLayout())
        self.secondRow2.setLayout(QVBoxLayout())
        self.secondRow3.setLayout(QVBoxLayout())
        self.secondRow4.setLayout(QVBoxLayout())
        


        self.secondRowfLabel = QLabel("Force")
        self.secondRowpLabel = QLabel("Position")
        self.secondRowpLabel2 = QLabel("Position")
        self.secondRowsLabel = QLabel("Support-Type")

        self.secondRow1.layout().addWidget(self.secondRowfLabel)
        self.secondRow2.layout().addWidget(self.secondRowpLabel)
        self.secondRow3.layout().addWidget(self.secondRowpLabel2)
        self.secondRow4.layout().addWidget(self.secondRowsLabel)



        self.secondRowContainer1.layout().addWidget(self.secondRow1)
        self.secondRowContainer1.layout().addWidget(self.secondRow2)
        self.secondRowContainer1.layout().setSpacing(120)
        
        

        self.secondRowContainer2.layout().addWidget(self.secondRow3)
        self.secondRowContainer2.layout().addWidget(self.secondRow4)
        self.secondRowContainer2.layout().setSpacing(120)

        
        
     

        self.secondRow.setLayout(QHBoxLayout())
        self.secondRow.layout().setAlignment(Qt.AlignTop)
        self.secondRow.setFixedSize(900,140)


        self.scrollArea1 = QScrollArea(self.secondRow)
        self.scrollArea1.setWidget(self.secondRowContainer1)
        self.scrollArea1.setVisible(True)
        self.scrollArea1.setWidgetResizable(True)
        self.scrollArea1.setAlignment(Qt.AlignHCenter)
        self.scrollArea1.setFixedSize(320,140)
       
        
        #self.secondRowContainer1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
      
        


        
  
     
        
        self.scrollArea2 = QScrollArea(self.secondRow)
        self.scrollArea2.setWidget(self.secondRowContainer2)
        self.scrollArea2.setWidgetResizable(True)
        self.scrollArea2.setAlignment(Qt.AlignHCenter)
        self.scrollArea2.setFixedSize(320,140)
        self.scrollArea2.setVisible(True)

        # self.scrollArea2.setStyleSheet("background-color: red;")
        

        self.secondRow.layout().addWidget(self.scrollArea1)
        self.secondRow.layout().addWidget(self.scrollArea2)
        self.secondRow.layout().setSpacing(140)
        self.secondRow.layout().setContentsMargins(50,0,0,0)
        
        print(self.secondRow.sizePolicy().Policy.Fixed)
        self.secondRowContainer1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.secondRowContainer2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.secondRowContainer1.layout().setAlignment(Qt.AlignTop)
        self.secondRowContainer2.layout().setAlignment(Qt.AlignTop)   
        
        self.page2Layout.addWidget(self.secondRow)

        #Page2 row 3
        self.row3 = QWidget()
        self.row3.setLayout(QHBoxLayout())
        self.row3.layout().setAlignment(Qt.AlignLeft)
        self.optionsLabel = QLabel("Find:")
        self.optionsLabel.setFixedWidth(40)
        self.optionsLabel.setStyleSheet("font-family: times-new-roman;"
                                        "font-size: 14px;"
                                        "font-weight: bold;")
        self.calcOption = QComboBox()
        self.calcOption.addItems(["Elongation", "Normal Stress", "Reaction Forces (determinate)", "Reaction Forces (indeterminate)"])


        self.calcOption.objectNameChanged.connect(self.changeInputOption)


        self.calcOption.setFixedWidth(180)
        self.row3.layout().addWidget(self.optionsLabel)
        self.row3.layout().addWidget(self.calcOption)

        self.nextPBttn = QPushButton("Calculate")
        self.nextPBttn.setFixedWidth(60)
        self.nextPBttn.clicked.connect(self.calc)


        self.elonKnowns = QWidget()
        self.elonKnowns.setLayout(QHBoxLayout())



        self.lengthAsk = QLabel("Beam Length[m]:")
        self.lengthInput = QLineEdit()
        self.areaAsk = QLabel("Cross-Sectional Area[mm^2]: ")
        self.areaInput = QLineEdit()

        self.modEInputLabel = QLabel("Young's Modulus")
        self.modEInput = QLineEdit()
        self.elonKnowns.layout().addWidget(self.lengthAsk)
        self.elonKnowns.layout().addWidget(self.lengthInput)
        self.elonKnowns.layout().addWidget(self.areaAsk)
        self.elonKnowns.layout().addWidget(self.areaInput)
        self.elonKnowns.layout().addWidget(self.modEInputLabel)
        self.elonKnowns.layout().addWidget(self.modEInput)

        self.row3.layout().addWidget(self.elonKnowns)


        self.row3.layout().addWidget(self.nextPBttn)
        self.page2Layout.addWidget(self.row3)

        self.page2.setLayout(self.page2Layout)
        self.stackedLayout.addWidget(self.page2)
        # Add the combo box and the stacked layout to the top-level layout
        self.layout.addLayout(self.stackedLayout)


    

    def switchPage(self):
        self.stackedLayout.setCurrentWidget(self.page2)

    def appendExForceText(self):
        #Store and add input values to chart
        self.secondRow1.layout().addWidget(QLabel(self.forceInput.text()))
        self.secondRow2.layout().addWidget(QLabel(self.positionInput.text()))
        self.myBeam.addEForce(int(self.forceInput.text()))
        self.myBeam.addtForce(int(self.forceInput.text()), int(self.positionInput.text()))

        #Delete values in the textbox's
        self.forceInput.setText("") 
        self.positionInput.setText("")  

    def appendSupportText(self):
        self.secondRow3.layout().addWidget(QLabel(self.positionInput2.text()))
        self.secondRow4.layout().addWidget(QLabel(self.supportType.currentText()))

        self.positionInput2.setText("")
        self.supportType.setCurrentIndex(0)
    
    def calc(self):
        force = 0
        for i in range(len(self.myBeam.forces)):
            force += self.myBeam.forces[i]
        
        
        
        self.myBeam.changelength(float(self.lengthInput.text()))
        self.myBeam.changecArea(float(self.areaInput.text()))
        self.myBeam.changeMod(float(self.modEInput.text()))

        return print(self.myBeam.calculateElongation(), self.myBeam.torsionCalc())

    def changeInputOption(self):
        if(self.calcOption.currentText == "Elongation"):
            self.elonKnowns.show()
        else:
            self.elonKnowns.hide()

    def axCalc(self):
        return
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())