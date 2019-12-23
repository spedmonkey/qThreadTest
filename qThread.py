from PyQt4 import QtCore, QtGui
import sys, time
import subprocess

class mythread(QtCore.QThread):

    total = QtCore.pyqtSignal(object)
    update = QtCore.pyqtSignal()

    def __init__(self, parent, n):
        super(mythread, self).__init__(parent)
        self.n = n

    def run(self):
        #self.total.emit(self.n)
        #process = subprocess.Popen(['python','C:\\Users\\gime9\\PycharmProjects\\threadingTest\\externalProcess.py'],
        #                         stdout=subprocess.PIPE)
        process = subprocess.Popen('ping www.google.com -t', stdout=subprocess.PIPE)
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:

                self.update.emit()
                print output.strip()

# create the dialog for zoom to point
class progress(QtGui.QProgressBar):

    def __init__(self, parent=None):
        super(progress, self).__init__(parent)
        # Set up the user interface from Designer.
        self.setValue(0)
        self.thread = mythread(self, 3)
        self.thread.total.connect(self.setMaximum)
        self.thread.update.connect(self.update)
        self.thread.finished.connect(self.close)

        self.n = 0
        self.thread.start()

    def update(self):
        self.n += 1
        self.setValue(self.n)

if __name__=="__main__":
    app = QtGui.QApplication([])
    progressWidget = progress()
    progressWidget.move(300, 300)
    progressWidget.show()
    sys.exit(app.exec_())
