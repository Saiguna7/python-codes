import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
import numpy as np

from fotf import *

#gui
from pyGui import fotfviewergui, createnewfotfgui
STATUSBAR_TIME = 5000

#__all__ = ['loadsets','gg1','gg2','gg3']

class FotfViewForm(QMainWindow, fotfviewergui.Ui_MainWindow_fotfviewer):
    def __init__(self):
        QMainWindow.__init__(self)
        fotfviewergui.Ui_MainWindow_fotfviewer.__init__(self)
        self.setWindowIcon(QIcon('index.png'))
        self.setupUi(self)

        # Checks for frequency domain
        self.lowerFreq = self.higherFreq = self.freqDataPoints = True

        # Checks for time Domain
        self._input = self._STOPTIME = self._STARTTIME = self._greaterthan = self._stepok = True

        #Personal Edits and Method calls/Subscribed Events
        self.foregroundRole()
        self.reloadAllFOTransFunc()
        self.pushButton_AddFotf.clicked.connect(self.addnewFotf)
        self.pushButton_EditFOTF.clicked.connect(self.editFOTF)
        self.pushButton_DeleteFOTF.clicked.connect(self.deleteFOTF)
        self.pushButtonViewInConsole.clicked.connect(self.ViewInConsole)
        self.pushButtonGetOustaloop.clicked.connect(self.OustaloopModel)
        self.pushButton_StabilityTest.clicked.connect(self.StabilityTest)
        self.pushButton_BodePlot.clicked.connect(self.BodePlot)
        self.pushButtonSimulate.clicked.connect(self.Step)
        self.comboBoxFOTF.currentIndexChanged.connect(self.ComboBoxFOTFempty)
        self.lineEdit_LowerFreq.editingFinished.connect(self._LowerFreq)
        self.lineEdit_HigherFreq.editingFinished.connect(self._HigherFreq)
        self.lineEdit_FreqDataPoints.editingFinished.connect(self._FreqDataPoints)
        self.lineEdit_inputTime.editingFinished.connect(self._isinputok)
        self.lineEdit_StartTime.editingFinished.connect(self._isstarttimeok)
        self.lineEdit_StepTime.editingFinished.connect(self._issteptimeok)
        self.lineEdit_StopTime.editingFinished.connect(self._isstoptimeok)
        self.isDialogActive =False
        self.show()

    def Exit(self):
        reply = QMessageBox.question(self, "Exit?", "Would you like to exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit()

    def reloadAllFOTransFunc(self):
        g1, g2, g3,g4 = loadsets()
        xvalues = list(locals().items())
        self.comboBoxFOTF.clear()
        for i, j in xvalues:
            if isinstance(j, FOTransFunc):
                self.comboBoxFOTF.addItem(i, j)

        #self.comboBoxTimeDomainType.addItems(["Step","Impulse"])
        self.comboBoxTimeDomainType.addItems(["Step"])

    def addnewFotf(self):
        createnew = newfotfgui()
        createnew.exec_()
        try:
            sysname, zero, pole, dt = createnew.lineEditSysName.text(), createnew.lineEdit_ZeroPoly.text(),\
                                      createnew.lineEdit_PolePoly.text(), createnew.lineEdit_DelayText.text()

            if (sysname or zero or pole or dt) != "":
                self.comboBoxFOTF.addItem(createnew.lineEditSysName.text(),
                                          newfotf(createnew.lineEdit_ZeroPoly.text(),
                                                  createnew.lineEdit_PolePoly.text(),
                                                  createnew.lineEdit_DelayText.text()))
                self.comboBoxFOTF.setCurrentIndex(self.comboBoxFOTF.count()-1)
        except:
            self.statusbar.showMessage('pyfomcon.addnewFotf: FOTF Addition Failed', STATUSBAR_TIME)
            print('\nfofopdtguiclass._addData: FOFOPDT Addition Failed\n')

    def editFOTF(self):
        createnew = newfotfgui()
        createnew.foregroundRole()
        createnew.lineEditSysName.setText(self.comboBoxFOTF.currentText())
        currentindex = self.comboBoxFOTF.currentIndex()
        x = self.comboBoxFOTF.currentData()
        num, nnum,den,nden, dt = fotfparam(x)
        if num.size > 1 and 1 < nnum.size == num.size:
            Zeros= poly2str(num,nnum)
        else:
            a = num**nnum
            Zeros = str(a[0])

        if den.size > 1 and 1 < nden.size == den.size:
            Poles = poly2str(den,nden)
        else:
            b = den**nden
            Poles = str(b[0])

        createnew.lineEdit_ZeroPoly.setText(Zeros),
        createnew.lineEdit_PolePoly.setText(Poles),
        createnew.lineEdit_DelayText.setText(str(dt))
        createnew.exec_()

        _sysname = createnew.lineEditSysName.text()
        _zero = createnew.lineEdit_ZeroPoly.text()
        _pole = createnew.lineEdit_PolePoly.text()
        _dt =   createnew.lineEdit_DelayText.text()
        self.comboBoxFOTF.setCurrentIndex(currentindex)
        if _sysname != "":
            self.comboBoxFOTF.setCurrentText(_sysname)
            if _zero != "" and _pole != "" and _dt != "":
                try:
                    self.comboBoxFOTF.setItemData(currentindex, newfotf(_zero,_pole,float(_dt)))
                except:
                    QMessageBox.question(self, 'Error',
                                         "Input values are not correct.\nEDIT ABORTED!",
                                         QMessageBox.StandardButtons(QMessageBox.Ok))
            else:
                QMessageBox.question(self, 'Error',
                                     "Input values are not correct.\nEDIT ABORTED!",
                                     QMessageBox.StandardButtons(QMessageBox.Ok))
        else:
            QMessageBox.question(self, 'Error',
                                 "System Name Empty!.\nEDIT ABORTED!",
                                 QMessageBox.StandardButtons(QMessageBox.Ok))

    def deleteFOTF(self):
        self.comboBoxFOTF.removeItem(self.comboBoxFOTF.currentIndex())

    def ViewInConsole(self):
        x = self.comboBoxFOTF.itemData(self.comboBoxFOTF.currentIndex())
        sysname = self.comboBoxFOTF.currentText()
        if x != None and isinstance(x,FOTransFunc):
            self.statusbar.showMessage('View Console for Transfer Function of {}'.format(sysname), STATUSBAR_TIME)
            print( sysname + ':')
            print(x)

    def OustaloopModel(self):
        x = self.comboBoxFOTF.itemData(self.comboBoxFOTF.currentIndex())
        if x != None and isinstance(x,FOTransFunc):
            print(self.comboBoxFOTF.currentText() + '.Oustaloop():')
            print(x.oustaloop())

    def StabilityTest(self):
        x = self.comboBoxFOTF.itemData(self.comboBoxFOTF.currentIndex())
        if x != None and isinstance(x, FOTransFunc):
            x.isstable(doPlot=True)

    def BodePlot(self):
        x = self.comboBoxFOTF.itemData(self.comboBoxFOTF.currentIndex())
        if isinstance(x,FOTransFunc):
            try:
                lowExp = int(self.lineEdit_LowerFreq.text())
                highExp = int(self.lineEdit_HigherFreq.text())
                dataPoints= int(self.lineEdit_FreqDataPoints.text())
                x.freqresp(lowExp,highExp,dataPoints)
            except:
                pass
        else:
            QMessageBox.question(self, 'Error',"There is no FOTF object in the Combo Box, Use the 'Add' button",
                                 QMessageBox.StandardButtons(QMessageBox.Ok))

    def Step(self):
        #TODO:check that stop is greater than start
        start = float(self.lineEdit_StartTime.text())
        stop = float(self.lineEdit_StopTime.text())
        step = float(self.lineEdit_StepTime.text())

        intnumofsteps = int((stop-start)/step)
        t = np.linspace(start,stop,intnumofsteps)
        u = np.ones_like(t) * float(self.lineEdit_inputTime.text())

        sys = self.comboBoxFOTF.itemData(self.comboBoxFOTF.currentIndex())

        if self.comboBoxTimeDomainType.currentText() == "Step":
            sys.step(t, u, output= False, plot=True)
        elif self.comboBoxTimeDomainType.currentText() == "Impulse":
            #TODO: Code for Impulse time domain
            pass

    def ComboBoxFOTFempty(self):
        if self.comboBoxFOTF.count() == 0:
            self.pushButtonSimulate.setDisabled(True)
            self.pushButtonGetOustaloop.setDisabled(True)
            self.pushButton_StabilityTest.setDisabled(True)
            self.pushButton_BodePlot.setDisabled(True)
            self.pushButtonViewInConsole.setDisabled(True)
            self.pushButton_DeleteFOTF.setDisabled(True)
            self.pushButton_EditFOTF.setDisabled(True)
        else:

            self.pushButtonGetOustaloop.setDisabled(False)
            self.pushButton_StabilityTest.setDisabled(False)
            self.pushButtonViewInConsole.setDisabled(False)
            self.pushButton_DeleteFOTF.setDisabled(False)
            self.pushButton_EditFOTF.setDisabled(False)
            self._FreqCheck()
            self._TimeCheck()

    def _ShowError(self, message, obj = None, obj2 = None):
        try:
            if self.isDialogActive == False:
                self.isDialogActive = True
                if obj != None:
                    obj.setCursorPosition(0)
                    obj.setSelection(0, len(obj.text()))

                self.statusbar.showMessage('Error: '+message, STATUSBAR_TIME)
                raise ValueError(QMessageBox.question(self, 'Error', message, QMessageBox.StandardButtons(QMessageBox.Ok)))
        except:
            self.isDialogActive = False

    # FREQUENCY DOMAIN VARIABLES CHECKS
    def _LowerFreq(self):
        if int(self.lineEdit_LowerFreq.text()) < 0:
            self.lowerFreq =True
        else:
            self.lowerFreq = False
            self._ShowError("'freq exponent (-int)' must be a -ve integer", self.lineEdit_LowerFreq)
        self._FreqCheck()

    def _HigherFreq(self):
        if int(self.lineEdit_HigherFreq.text()) > 0:
            self.higherFreq = True
        else:
            self.higherFreq = False
            self._ShowError("'freq exponent (int)' must be a +ve integer",self.lineEdit_HigherFreq)
        self._FreqCheck()

    def _FreqDataPoints(self):
        if int(self.lineEdit_FreqDataPoints.text()) >= 500:
            self.freqDataPoints = True
        else:
            self.freqDataPoints = False
            self._ShowError("'Data points (int)' must be a +ve integer >= 500", self.lineEdit_FreqDataPoints)
        self._FreqCheck()

    def _FreqCheck(self):
        if self.lowerFreq and self.higherFreq and self.freqDataPoints:
            self.pushButton_BodePlot.setEnabled(True)
        else:
            self.pushButton_BodePlot.setEnabled(False)

    #TIME DOMAIN VARIABLES CHECKS
    def _issteptimeok(self):
        if 0 < float(self.lineEdit_StepTime.text()) <= 0.087:
            self._stepok = True
        else:
            self._stepok = False
            self._ShowError('0 < "Step(s)" < 0.087', self.lineEdit_StepTime)
        self._TimeCheck()

    def _isinputok(self):
        if float(self.lineEdit_inputTime.text()) < 0:
            self._input = False
            self._ShowError('"input" must be > 0',self.lineEdit_inputTime)
        else:
            self._input = True
        self._TimeCheck()

    def _isstarttimeok(self):
        if float(self.lineEdit_StartTime.text()) < 0:
            self._STARTTIME =False
            self._ShowError('"Start(s)" must be > 0',self.lineEdit_StartTime)
        else:
            self._STARTTIME = True
        self._TimeCheck()

    def _isstoptimeok(self):
        if float(self.lineEdit_StopTime.text()) < 0:
            self._STOPTIME = False
            self._ShowError('"Stop)" must be > 0',self.lineEdit_StopTime)
        else:
            self._STOPTIME = True
        self._TimeCheck()

    def _TimeCheck(self):
        if float(self.lineEdit_StartTime.text()) < float(self.lineEdit_StopTime.text()):
            self._greaterthan =True
        else:
            self._greaterthan = False
            self._ShowError('"Stop(s)" must be > Start(s)')

        if self._input and self._STOPTIME and self._STARTTIME and self._greaterthan and self._stepok:
            self.pushButtonSimulate.setEnabled(True)
        else:
            self.pushButtonSimulate.setEnabled(False)

    def closeEvent(self,event):
        reply = QMessageBox.question(self, "Exit?", "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            sys.exit()
        else:
            event.ignore()

class newfotfgui(QDialog, createnewfotfgui.Ui_dialogCreateNewFOTF):
    def __init__(self):
        QDialog.__init__(self)
        createnewfotfgui.Ui_dialogCreateNewFOTF.__init__(self)
        self.setWindowIcon(QIcon('index.png'))
        self.setupUi(self)

        self.lineEditSysName.textChanged.connect(self._checkSysName)
        self.lineEdit_ZeroPoly.textChanged.connect(self._zeroPolyChanged)
        self.lineEdit_PolePoly.textChanged.connect(self._polePolyChanged)
        self.lineEdit_DelayText.textChanged.connect(self._delayChanged)

        self.pushButtonOK.clicked.connect(self.close)
        self.pushButtonCancel.clicked.connect(self.close)
        self.sysnamecheck = self.zeroCheck = self.poleCheck = False
        self.delayCheck = True  #in gui intitla delay is always 0
        self.show()

    #region Button OK Check
    def _checkOkButton(self):
        if self.sysnamecheck and self.zeroCheck and self.delayCheck and self.poleCheck:
            self.pushButtonOK.setEnabled(True)
        else:
            self.pushButtonOK.setEnabled(False)
    #endregion

    #region lineEdit Values Check
    def _checkSysName(self):
        try:
            self.sysnamecheck = len(self.lineEditSysName.text().strip(" ")) >= 1
            self._checkOkButton()
        except:
            self.sysnamecheck = False
            self._checkOkButton()

    def _zeroPolyChanged(self):
        try:
            self.zeroCheck = str2poly(self.lineEdit_ZeroPoly.text())
            self._checkOkButton()
        except:
            self.zeroCheck = False
            self._checkOkButton()

    def _delayChanged(self):
        try:
            self.delayCheck = float(self.lineEdit_DelayText.text()) >= 0
            self._checkOkButton()
        except:
            self.delayCheck = False
            self._checkOkButton()

    def _polePolyChanged(self):
        try:
            self.poleCheck = str2poly(self.lineEdit_ZeroPoly.text())
            self._checkOkButton()
        except:
            self.poleCheck = False
            self._checkOkButton()

    #endregion

    def closeEvent(self, event):
        sender = self.sender().text()

        close = QMessageBox.question(self, "{0}?".format(sender),
                                     "Are you sure you would like to '{0}' this form?".format(sender),
                                     QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            if sender == "OK":
                pass
            else:
                self.lineEditSysName.clear()
                self.lineEdit_ZeroPoly.clear()
                self.lineEdit_PolePoly.clear()
                self.lineEdit_DelayText.clear()
            event.accept()
        else:
            event.ignore()

def loadsets():
    return gg1(),gg2(), gg3(),gg4()

def gg1():
    return newfotf(1., '14994s^{1.31}+6009.5s^{0.97}+1.69', 0)

def gg2():
    return newfotf(1., '0.8s^{2.2}+0.5s^{0.9}+1', 0)

def gg3():
    return newfotf('-2s^{0.63}+4', '2s^{3.501}+3.8s^{2.42}+2.6s^{1.798}+2.5s^{1.31}+1.5', 0)

def gg4():
    return newfotf('s+1','s^2.5+0.5s^1.5+100',0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fomcon = FotfViewForm()
    app.exec_()