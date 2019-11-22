import sys
import math
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

global client
global count
global feecalc
global totalamount
global fees
global inv
global depo
global mediation
global efiling
global citation
global other
global feecal
global client
global providernum
global providerint
global refint
global totalfees
global totalbill
global N
global B
global F

N = list()
B = list()
F = list()
providernum = "0"



class disbursement(QDialog):
    def __init__(self):
        super(disbursement, self).__init__()
        loadUi("gui/disbursement.ui", self)
        self.pushButton.clicked.connect(self.calcclient)
        self.pushButton_2.clicked.connect(self.calcprovider)
        self.pushButton_3.clicked.connect(self.createfiles)

        self.textEdit.setTabChangesFocus(True)
        self.textEdit_2.setTabChangesFocus(True)


    def calcclient(self):

        global totalamount
        global totalfees
        global totalbill

        clientnum = self.textEdit.toPlainText()

        if not clientnum == "":

            clientfloat = float(clientnum)
            toproviders = totalamount - totalfees - clientfloat
            toproviders = toproviders/totalbill
            toproviders = toproviders*100

            self.textEdit_2.setText(str(toproviders))

    def calcprovider(self):
        global totalamount
        global totalfees
        global totalbill
        toproviders = self.textEdit_2.toPlainText()

        if not toproviders == "":
            toproviders = float(toproviders)
            providerpercentage = toproviders/100
            totalpaidtoproviders = providerpercentage * totalbill
            toclient = totalamount - totalfees - totalpaidtoproviders

            self.textEdit.setText(str(toclient))

    def createfiles(self):
        print("WIP")

class providers(QDialog):
    def __init__(self):
        super(providers, self).__init__()
        loadUi("gui/settlement_providers.ui", self)
        self.disbursement = disbursement()
        self.label_6.setText("1")
        global refint
        refint = 1
        self.pushButton.clicked.connect(self.calculate)

        self.textEdit.setTabChangesFocus(True)
        self.textEdit_2.setTabChangesFocus(True)
        self.textEdit_3.setTabChangesFocus(True)


    def calculate(self):
        global refint


        if providerint > refint:
            if refint == False:
                refint = 1

            n = self.textEdit.toPlainText()
            b = self.textEdit_2.toPlainText()
            f = self.textEdit_3.toPlainText()
            b = float(b)
            N.append(n)
            B.append(b)
            F.append(f)
            refint += 1
            refnum = str(refint)
            self.label_6.setText(refnum)
            self.textEdit.clear()
            self.textEdit_2.clear()


        else:
            n = self.textEdit.toPlainText()
            b = self.textEdit_2.toPlainText()
            f = self.textEdit_3.toPlainText()
            b = float(b)
            N.append(n)
            B.append(b)
            F.append(f)
            global totalbill
            totalbill = sum(i for i in B)
            totalbill = float(totalbill)
            self.hide()
            self.disbursement.show()


class mainpage(QDialog):
    def __init__(self):
        super(mainpage, self).__init__()
        loadUi("gui/settlement.ui", self)
        self.providers = providers()
        self.pushButton.clicked.connect(self.movepage)

        self.textEdit.setTabChangesFocus(True)
        self.textEdit_2.setTabChangesFocus(True)
        self.textEdit_3.setTabChangesFocus(True)
        self.textEdit_4.setTabChangesFocus(True)
        self.textEdit_5.setTabChangesFocus(True)
        self.textEdit_6.setTabChangesFocus(True)
        self.textEdit_7.setTabChangesFocus(True)
        self.textEdit_8.setTabChangesFocus(True)
        self.textEdit_9.setTabChangesFocus(True)
        self.textEdit_10.setTabChangesFocus(True)

    def movepage(self):
        self.providers.show()
        self.hide()

        global fees
        global totalamount

        feetype = self.comboBox.currentText()
        totalamount = self.textEdit.toPlainText()
        fees = self.textEdit_2.toPlainText()
        inv = self.textEdit_3.toPlainText()
        depo = self.textEdit_4.toPlainText()
        mediation = self.textEdit_5.toPlainText()
        efiling = self.textEdit_6.toPlainText()
        citation = self.textEdit_7.toPlainText()
        other = self.textEdit_8.toPlainText()
        client = self.textEdit_9.toPlainText()
        providernum = self.spinBox.value()

        if not totalamount:
            totalamount = 0

        if not fees:
            fees = 0

        if not inv:
            inv = 0

        if not depo:
            depo = 0

        if not mediation:
            mediation = 0

        if not efiling:
            efiling = 0

        if not citation:
            citation = 0

        if not other:
            other = 0

        if not client:
            client = ("Client")


        totalamount = float(totalamount)
        fees = float(fees)
        inv = float(inv)
        depo = float(depo)
        mediation = float(mediation)
        efiling = float(efiling)
        citation = float(citation)
        other = float(other)

        global providerint
        providerint = int(providernum)

        if feetype == "%":

            fees = (fees/100*totalamount)

        global totalfees
        totalfees = fees + inv + depo + mediation + efiling + citation + other

app = QApplication(sys.argv)
global widget
widget = mainpage()
widget.show()
sys.exit(app.exec_())
