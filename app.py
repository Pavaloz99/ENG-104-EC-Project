import sys

from PyQt5.QtCore import (
    QRect,
    QSize,
    Qt,
    QPoint,
    QAbstractItemModel,
    QStringListModel
    
    
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
    QListView,
    QListWidget,
    QListWidgetItem,
    
    
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
        self.tButton = QPushButton("Torsion")
        self.tButton.clicked.connect(self.switchTor)
        self.page1Layout.addRow(self.tButton)
        self.page1Layout.addRow(QPushButton("Bending"))
        self.page1.setLayout(self.page1Layout)
        self.stackedLayout.addWidget(self.page1)
        # Create the second page
        self.page2 = QWidget()
        self.page2Layout = QVBoxLayout()
        
        
        
        #Title decleration, insertion and styling
        self.zeroRow = QWidget()
        self.zeroRow.setLayout(QHBoxLayout())
        self.zeroRow.layout().setAlignment(Qt.AlignHCenter)
        self.zeroRow.setFixedHeight(50)
        self.title = QLabel("List All Axial Loads On Beam")
        

        # self.title2 = QLabel("List All Supports Acting on the Member")
        # self.title2.setStyleSheet("padding: 0px;" 
        #                         "font-family: Times-New-Roman;"
        #                         "font-size: 20px;"
        #                         "font-weight: Bold;")
        # self.title2.setFixedSize(400,25)
    
        self.zeroRow.layout().addWidget(self.title)
        self.title.setStyleSheet(
                                "font-family: Times-New-Roman;"
                                "font-size: 20px;"
                                "font-weight: Bold;")
        
        # self.zeroRow.layout().addWidget(self.title2, alignment = Qt.AlignRight and Qt.AlignVCenter)
        self.page2Layout.addWidget(self.zeroRow)
       
       #Textbox for force 
        self.forceInput = QLineEdit()
        self.forceInput.setFixedSize(QSize(70,20))
        

        #Textbox for position
        self.positionInput = QLineEdit()
        self.positionInput.setFixedSize(QSize(70,20))

        #box styling
        self.setStyleSheet("QLineEdit: {border-radius: 30px; } ")

        self.fLabel = QLabel("Force:")
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
        # self.rowOneSecondHalf = QWidget()
        # self.rowOneSecondHalf.setLayout(QHBoxLayout())
        self.rowOne.layout().addWidget(self.rowOneFirstHalf)
        # self.rowOne.layout().addWidget(self.rowOneSecondHalf)
        self.rowOne.layout().setAlignment(Qt.AlignTop)

        

        self.rowOne.setFixedHeight(70)
        self.rowOne.layout().setAlignment(Qt.AlignHCenter)
  
        self.rowOneFirstHalf.setFixedWidth(450)

        # self.rowOneSecondHalf.layout().setSpacing(3)
        
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

        # self.addButtonPos = QPushButton("Add")
        # self.addButtonPos.clicked.connect(self.appendSupportText)
        # self.addButtonPos.setFixedSize(50,30)

        # self.supportType = QComboBox()
        # self.supportType.addItems(["-Select-","Pin Support", "Roller Support", "Fixed End"])
        # self.supportType.setFixedSize(100, 30)
        
        
        # self.pLabel2 = QLabel("Position:")
        # self.pLabel2.setFixedWidth(70)
        # self.pLabel2.setStyleSheet("font-size: 16px;"
        #                         "font-family: Times-new-roman;")

        # self.positionInput2 = QLineEdit()
        # self.positionInput2.setFixedSize(QSize(50,20))

        self.rowOneFirstHalf.layout().addWidget(self.addButton)

        
        # self.rowOneSecondHalf.layout().addWidget(self.pLabel2)
        # self.rowOneSecondHalf.layout().addWidget(self.positionInput2)
        # self.rowOneSecondHalf.layout().addWidget(self.supportType)
        # self.rowOneSecondHalf.layout().addWidget(self.addButtonPos)



    
        
        
        self.page2Layout.addWidget(self.rowOne)



        
        
        
        self.secondRow = QWidget()


        #Defining each column for the fourth row
        self.secondRow1 = QWidget()
        self.secondRow2 = QWidget()
        # self.secondRow3 = QWidget()
        # self.secondRow4 = QWidget()


   
        




        self.secondRowContainer1 = QWidget()
        self.secondRowContainer1.setLayout(QHBoxLayout())
      

        # self.secondRowContainer2 = QWidget()
        # self.secondRowContainer2.setLayout(QHBoxLayout())
    




        self.secondRow1.setLayout(QVBoxLayout())
        self.secondRow2.setLayout(QVBoxLayout())
        # self.secondRow3.setLayout(QVBoxLayout())
        # self.secondRow4.setLayout(QVBoxLayout())
        


        self.secondRowfLabel = QLabel("Force")
        self.secondRowpLabel = QLabel("Position")
        self.secondRowdLabel = QLabel("Distance")
        self.secondRowpLabel2 = QLabel("Position")
        self.secondRowsLabel = QLabel("Support-Type")

        self.secondRow1.layout().addWidget(self.secondRowfLabel)
        self.secondRow2.layout().addWidget(self.secondRowpLabel)
        # self.secondRow3.layout().addWidget(self.secondRowpLabel2)
        # self.secondRow4.layout().addWidget(self.secondRowsLabel)



        self.secondRowContainer1.layout().addWidget(self.secondRow1)
        self.secondRowContainer1.layout().addWidget(self.secondRow2)
        self.secondRowContainer1.layout().setSpacing(120)
        
        

        # self.secondRowContainer2.layout().addWidget(self.secondRow3)
        # self.secondRowContainer2.layout().addWidget(self.secondRow4)
        # self.secondRowContainer2.layout().setSpacing(120)

        
        
     

        self.secondRow.setLayout(QHBoxLayout())
        self.secondRow.layout().setAlignment(Qt.AlignTop)
        self.secondRow.setFixedSize(900,140)


        self.scrollArea1 = QScrollArea(self.secondRow)
        self.scrollArea1.setWidget(self.secondRowContainer1)
        self.scrollArea1.setVisible(True)
        self.scrollArea1.setWidgetResizable(True)
        self.scrollArea1.setAlignment(Qt.AlignHCenter)
        self.scrollArea1.setFixedSize(400,140)
       
        
        #self.secondRowContainer1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
      
        


        
  
     
        
        # self.scrollArea2 = QScrollArea(self.secondRow)
        # self.scrollArea2.setWidget(self.secondRowContainer2)
        # self.scrollArea2.setWidgetResizable(True)
        # self.scrollArea2.setAlignment(Qt.AlignHCenter)
        # self.scrollArea2.setFixedSize(320,140)
        # self.scrollArea2.setVisible(True)

        # self.scrollArea2.setStyleSheet("background-color: red;")
        

        self.secondRow.layout().addWidget(self.scrollArea1)
        # self.secondRow.layout().addWidget(self.scrollArea2)
        # self.secondRow.layout().setSpacing(140)
        self.secondRow.layout().setContentsMargins(50,0,0,0)
        
        self.secondRow.layout().setAlignment(Qt.AlignHCenter)
        self.secondRowContainer1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        # self.secondRowContainer2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.secondRowContainer1.layout().setAlignment(Qt.AlignTop)
        # self.secondRowContainer2.layout().setAlignment(Qt.AlignTop)   
        
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
        self.calcOption.addItems(["Elongation", "Normal Stress", "Reaction Forces (indeterminate)"])


        self.calcOption.currentIndexChanged.connect(self.changeInputOption)


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



        
   
        
        self.compatibilityL = QLabel("Compatibility:")
        self.compatibilityL.setFixedWidth(70)
        self.compatibilityL.hide()

        self.compatibilityCombo = QComboBox()
        self.compatibilityCombo.addItems(["Elongation = 0", "Elongation <= x"])
        self.compatibilityCombo.setFixedSize(140,30)
        self.compatibilityCombo.hide()
        self.compatibilityCombo.currentIndexChanged.connect(self.addXInputs)

        self.xLabel = QLabel("x[m]:")
        self.xLabel.setFixedWidth(22)
        self.xLabel.hide()
        self.xInput = QLineEdit()
        self.xInput.setFixedWidth(80)
        self.xInput.hide()
        

        self.row4 = QWidget()
        self.row4.setLayout(QHBoxLayout())
        self.row4.layout().setAlignment(Qt.AlignLeft)
        self.row4.layout().setSpacing(10)
        self.row4.layout().addWidget(self.compatibilityL)
        self.row4.layout().addWidget(self.compatibilityCombo)
        self.row4.layout().addWidget(self.xLabel)
        self.row4.layout().addWidget(self.xInput)

        self.answerL = QLabel("Answer:")
        self.answerL.hide()
        self.answer = QLabel("")
        self.answer.hide()

        self.row4.layout().addWidget(self.answerL)
        self.row4.layout().addWidget(self.answer)

        

        # self.row5 = QWidget()
        # self.row5.setLayout(QHBoxLayout())
        # self.row5.layout().setAlignment(Qt.AlignLeft)
        # self.row5.setFixedWidth(900)
        # self.moreSections = QPushButton("Add a section")
        # self.moreSections.clicked.connect(self.addSectionInputs)
        # self.moreSectionsBox = QWidget()
        # self.moreSectionsBox.setLayout(QVBoxLayout())
        # self.moreSectionsBox.setFixedSize(600,100)
        # self.moreSectionsBox.layout().setAlignment(Qt.AlignCenter)
        # self.scrollContainer = QWidget()
        # self.scrollContainer.setLayout(QVBoxLayout())
        
     
        # self.moreSectionScroll = QScrollArea(self.moreSectionsBox)
        # self.moreSectionScroll.setAlignment(Qt.AlignCenter)
        # self.moreSectionScroll.setWidgetResizable(True)
        # self.moreSectionScroll.setVisible(True)
        # self.moreSectionScroll.setFixedSize(600, 100)
        
        # self.moreSectionScroll.setWidget(self.scrollContainer)
    
        
        # self.row5.layout().addWidget(self.moreSections)
        # self.row5.layout().addWidget(self.moreSectionsBox)

        



        self.row3.layout().addWidget(self.elonKnowns)


        self.row3.layout().addWidget(self.nextPBttn)
        self.page2Layout.addWidget(self.row3)
        self.page2Layout.addWidget(self.row4)
        #self.page2Layout.addWidget(self.row5)

        self.page2.setLayout(self.page2Layout)

        self.page3 = QWidget()

        self.page3.setLayout(QVBoxLayout())

        self.p3R1 = QWidget()
        self.p3R1.setLayout(QHBoxLayout())
        self.p3R1.layout().addWidget(QLabel("List Forces, distance and position on Bar"))

        self.p3r2 = QWidget()
        self.p3r2.setLayout(QHBoxLayout())

        
        self.p3r3 = QWidget()
        self.p3r3.setLayout(QHBoxLayout())
        self.p3r3gridW = QWidget()
        self.p3r3gridW.setLayout(QGridLayout())
        self.p3r3gridW.setFixedSize(800,100)
        self.p3r3gridW.layout().setAlignment(Qt.AlignHCenter)
        self.p3r3.layout().addWidget(self.p3r3gridW)
        self.p3r3.layout().setAlignment(Qt.AlignCenter)
        self.p3r3Scroll = QScrollArea(self.p3r3)
        self.p3r3Scroll.setWidget(self.p3r3gridW)
        self.p3r3Scroll.setFixedSize(900,180)
        self.p3r3Scroll.setAlignment(Qt.AlignCenter)
        self.p3r3Scroll.setVisible(True)
        

    
       
       

        self.tfLabel = QLabel("Force")
        self.tdLabel = QLabel("Distance")
        self.tpLabel = QLabel("Position")


        self.tfInput = QLineEdit()
        self.tdInput = QLineEdit()
        self.tpInput = QLineEdit()

        self.torAddBttn = QPushButton("Add")
        self.torAddBttn.clicked.connect(self.appendTorInputs)


        


        
        
        
        
        
        



        self.p3r2.layout().addWidget(self.tfLabel)
        self.p3r2.layout().addWidget(self.tfInput)
        self.p3r2.layout().addWidget(self.tdLabel)
        self.p3r2.layout().addWidget(self.tdInput)
        self.p3r2.layout().addWidget(self.tpLabel)
        self.p3r2.layout().addWidget(self.tpInput)
        self.p3r2.layout().addWidget(self.torAddBttn)


        


        self.page3.layout().addWidget(self.p3R1)
        self.page3.layout().addWidget(self.p3r2)
        self.page3.layout().addWidget(self.p3r3)
        self.stackedLayout.addWidget(self.page2)
        self.stackedLayout.addWidget(self.page3)
        # Add the combo box and the stacked layout to the top-level layout
        self.layout.addLayout(self.stackedLayout)

    


    # def addSectionInputs(self):
    #     areaLabel = QLabel("Cross-Sectional Area [m^2]")
    #     areaInput = QLineEdit()
    #     areaInput.setObjectName("aInput")
    #     endSection = QLabel("End Position")
    #     endSectionInput = QLineEdit()
    #     endSectionInput.setObjectName("endSection")
    #     areaModLabel = QLabel("Modulus")
    #     areaModInput = QLineEdit()
    #     areaModInput.setObjectName("modInput")

    #     newline = QWidget()
    #     newline.setLayout(QHBoxLayout())

       
    #     newline.layout().addWidget(areaLabel)
    #     newline.layout().addWidget(areaInput)
    #     newline.layout().addWidget(endSection)
    #     newline.layout().addWidget(endSectionInput)
    #     newline.layout().addWidget(areaModLabel)
    #     newline.layout().addWidget(areaModInput)

    #     self.scrollContainer.layout().addWidget(newline)

    #     return
    def addXInputs(self):
        if self.compatibilityCombo.currentText() == "Elongation <= x":
            self.xLabel.show()
            self.xInput.show()
        else: 
            self.xInput.hide()
            self.xLabel.hide()
    

    def appendTorInputs(self):
        position = self.p3r3gridW.layout().rowCount()
        self.p3r3gridW.layout().addWidget(QLabel(self.tfInput.text()),position,0)
        self.p3r3gridW.layout().addWidget(QLabel(self.tdInput.text()),position,1)
        self.p3r3gridW.layout().addWidget(QLabel(self.tpInput.text()),position,2)

        self.tfInput.setText("")
        self.tdInput.setText("")
        self.tpInput.setText("")
        
    

    def switchPage(self):
        self.stackedLayout.setCurrentWidget(self.page2)

    def switchTor(self):
        self.stackedLayout.setCurrentWidget(self.page3)


    def appendExForceText(self):
        #Store and add input values to chart
        self.secondRow1.layout().addWidget(QLabel(self.forceInput.text()))
        self.secondRow2.layout().addWidget(QLabel(self.positionInput.text()))
        self.myBeam.addEForce(float(self.forceInput.text()))
        self.myBeam.addposition(float(self.positionInput.text()))
        self.myBeam.addtForce(float(self.forceInput.text()), float(self.positionInput.text()))

        #Delete values in the textbox's
        self.forceInput.setText("") 
        self.positionInput.setText("")  

    # def appendSupportText(self):
    #     self.secondRow3.layout().addWidget(QLabel(self.positionInput2.text()))
    #     self.secondRow4.layout().addWidget(QLabel(self.supportType.currentText()))

    #     self.positionInput2.setText("")
    #     self.supportType.setCurrentIndex(0)
    
    def calc(self):
        
        #Check for multiple Sections

        self.myBeam.length = float(self.lengthInput.text())
        if self.calcOption.currentText() == "Elongation":
            self.myBeam.cArea = float(self.areaInput.text())
            self.myBeam.modulusOfE = float(self.modEInput.text())
            self.answer.setText(str(self.myBeam.calculateElongation()))
            self.answerL.show()
            self.answer.show()
            print(self.myBeam.calculateElongation())
        elif self.calcOption.currentText() == "Normal Stress":
            print("Meme")
        elif self.calcOption.currentText() == "Reaction Forces (indeterminate)":
            if self.compatibilityCombo.currentText() == "Elongation = 0":
                self.myBeam.compatibility = 0
                ans = self.myBeam.axLoadIndRxnForces()
                self.row4.layout().addWidget(QLabel("Answer -  F_a:"))
                self.row4.layout().addWidget(QLabel(str(ans[0])))
                self.row4.layout().addWidget(QLabel(" F_b:"))
                self.row4.layout().addWidget(QLabel(str(ans[1])))

    def changeInputOption(self):
        if(self.calcOption.currentText() == "Reaction Forces (indeterminate)"):
            self.compatibilityL.show()
            self.compatibilityCombo.show()
        else: 
            self.compatibilityCombo.hide()
            self.compatibilityL.hide()

    def axCalc(self):
        return
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())