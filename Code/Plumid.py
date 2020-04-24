import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
import sys, pygame, pygame.midi
import pyautogui
pygame.init()
pygame.midi.init()
import os

class Plumid(QWidget):

    def __init__(self):
        """
        Function to initialize UI and display welcome messages
        """
        super().__init__()
        self.initUI()
        print("Welcome to Plumid!")
        self.textbox.setText("Welcome to Plumid!")

    def center(self):
        """
        Function to center application window on screen
        :return: N/A
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def tryer(self):
        """
        Function to execute main MIDI function when called by GUI
        :return: N/A
        """
        self.parsemidi()

    def quit(self):
        """
        Function to kill program
        :return: N/A
        """
        os.system(exit())

    def parsemidi(self):
        """
        Function to listen for, read and parse MIDI received from hardware.
        :return: 1 if device is not connected
        """
         # list all midi devices
        for x in range(0, pygame.midi.get_count()):
            print (pygame.midi.get_device_info(x))

        # open a specific midi device
        while True:
            try:
                inp = pygame.midi.Input(0)
                break
            except pygame.midi.MidiException:
                print("Device not connected. Please try again!")
                self.textbox.clear()
                self.textbox.setText("Device not connected. Please try again!")
                return 1
        # runs the event loop
        while True:
            if inp.poll():
                # no way to find number of messages in queue
                # so we just specify a high max value
                midin=inp.read(10)
                print (len(midin), midin[0][0][0])

                # parses MIDI input based on received message
                if len(midin)==1 and  midin[0][0][0]==176 and 1 <= midin[0][0][1] <= 10:
                    print ('cc:', midin[0][0][1])
                    cc=midin[0][0][1]
                    self.electricsunrise(cc)
                elif len(midin)==1 and  midin[0][0][0]==192 and 10 <= midin[0][0][1] <= 20:
                    print('cc:', midin[0][0][1])
                    cc = midin[0][0][1]
                    self.worship(cc)
        pygame.time.wait(10)

    def worship(self, midicc):
        """
        Function to interact with the Archetype software based on the received MIDI input
        within the worship patches bank.
        :return: 1 if input is invalid or out of range.
        """
        if type(midicc)!=int:
            print ("Invalid Input! Please try again.")
            self.textbox.setText("Invalid Input! Please try again.")
            return 1
        #If MIDI is out of range
        if midicc>=20:
            print("Plumid doesn't have any more patches in the worship set. Thank you!")
            self.textbox.setText("Plumid doesn't have any more patches in the worship set. Thank you!")
            return 1
        # If MIDI is from 10-19, pyautogui will be used to automate mouse clicks
        # and interacts with the Archetype software to change to the specified patch
        if midicc==10:
            self.textbox.setText("Worship - Reverb")
            pyautogui.click(x=530, y=145)
            pyautogui.moveTo(530, 265, duration=0.1)
            pyautogui.moveTo(720, 265, duration=0.2)
            pyautogui.click(x=720, y=265)
        if midicc==11:
            self.textbox.setText("Worship - Ambience")
            pyautogui.click(x=530, y=145)
            pyautogui.moveTo(530, 265, duration=0.1)
            pyautogui.moveTo(720, 370, duration=0.2)
            pyautogui.click(x=720, y=370)
        if midicc==12:
            self.textbox.setText("Worship - Quarter Note Delay")
            pyautogui.click(x=530, y=145)
            pyautogui.moveTo(530, 265, duration=0.1)
            pyautogui.moveTo(720, 290, duration=0.2)
            pyautogui.click(x=720, y=290)
        if midicc==13:
            self.textbox.setText("Worship - Dotted Eighth Delay")
            pyautogui.click(x=530, y=145)
            pyautogui.moveTo(530, 265, duration=0.1)
            pyautogui.moveTo(720, 390, duration=0.2)
            pyautogui.click(x=720, y=390)
        if midicc==14:
            self.textbox.setText("Worship - Rhythm Low Gain")
            pyautogui.click(x=530, y=145)
            pyautogui.moveTo(530, 265, duration=0.1)
            pyautogui.moveTo(720, 310, duration=0.2)
            pyautogui.click(x=720, y=310)
        if midicc == 15:
            self.textbox.setText("Worship - Rhythm Main")
            pyautogui.click(x=530, y=145)
            pyautogui.moveTo(530, 265, duration=0.1)
            pyautogui.moveTo(720, 350, duration=0.2)
            pyautogui.click(x=720, y=350)
        if midicc == 16:
            self.textbox.setText("Worship - Lead")
            pyautogui.click(x=530, y=145)
            pyautogui.moveTo(530, 265, duration=0.1)
            pyautogui.moveTo(720, 330, duration=0.2)
            pyautogui.click(x=720, y=330)
        if midicc == 17:
            self.textbox.setText("Worship - Delay ON/OFF")
            pyautogui.click(x=136, y=483)
        if midicc==18:
            self.textbox.setText("Worship - Reverb ON/OFF")
            pyautogui.click(x=630, y=491)
        if midicc==19:
            self.textbox.setText("Worship - Tap Tempo")
            pyautogui.click(x=360, y=480)


    def electricsunrise(self, midicc):
        """
        Function to interact with the Archetype software based on the received MIDI input
        within the electric sunrise bank.
        :return: 1 if input is invalid or out of range.
        """
        if type(midicc)!=int:
            print ("Invalid Input! Please try again.")
            self.textbox.setText("Invalid Input! Please try again.")
            return 1
        # If MIDI is out of range
        if midicc>=20:
            print("Plumid doesn't have any more patches in the electric sunrise set. Thank you!")
            self.textbox.setText("Plumid doesn't have any more patches in the electric sunrise set. Thank you!")
            return 1
        # If MIDI is from 10-19, pyautogui will be used to automate mouse clicks
        # and interacts with the Archetype software to change to the specified patch
        if midicc==1:
            self.textbox.setText("ES - Intro")
            pyautogui.click(x=530, y=145)
            pyautogui.moveTo(530, 235, duration=0.1)
            pyautogui.moveTo(720, 275, duration=0.2)
            pyautogui.click(x=720, y=275)
        if midicc==2:
            self.textbox.setText("ES - Lead")
            pyautogui.click(x=530, y=145)
            pyautogui.moveTo(530, 235, duration=0.1)
            pyautogui.moveTo(720, 320, duration=0.2)
            pyautogui.click(x=720, y=320)
        if midicc==3:
            self.textbox.setText("ES - Crunch")
            pyautogui.click(x=530, y=145)
            pyautogui.moveTo(530, 235, duration=0.1)
            pyautogui.moveTo(720, 235, duration=0.2)
            pyautogui.click(x=720, y=235)
        if midicc==4:
            self.textbox.setText("ES - Sparkle")
            pyautogui.click(x=530, y=145)
            pyautogui.moveTo(530, 235, duration=0.1)
            pyautogui.moveTo(720, 295, duration=0.2)
            pyautogui.click(x=720, y=295)
        if midicc==5:
            self.textbox.setText("ES - Solo")
            pyautogui.click(x=530, y=145)
            pyautogui.moveTo(530, 235, duration=0.1)
            pyautogui.moveTo(720, 255, duration=0.2)
            pyautogui.click(x=720, y=255)
        if midicc ==9:
            self.textbox.setText("ES - Delay ON/OFF")
            pyautogui.click(x=136, y=483)
        if midicc==10:
            self.textbox.setText("ES - Reverb ON/OFF")
            pyautogui.click(x=630, y=491)



    def initUI(self):
        """
        Function to create, design and implement the main GUI elements.
        :return: 1 if input is invalid or out of range.
        """
        #Creates GUI window and specifies
        self.label = QLabel()
        self.grid = QGridLayout()
        self.grid.addWidget(self.label, 0, 0)
        self.setLayout(self.grid)
        self.resize(500, 250)
        self.center()

        #Start button design
        button = QPushButton('Start Plumid', self)
        button.move(80, 485)
        button.resize(200,40)
        button.clicked.connect(self.tryer)

        #Exit button design
        button2 = QPushButton('Exit', self)
        button2.move(285, 485)
        button2.resize(170,40)
        button2.clicked.connect(self.quit)

        #Textbox Design
        self.textbox = QLineEdit(self)
        self.textbox.move(120, 420)
        self.textbox.resize(300,25)

        #Background graphic importing and design
        self.im = QtGui.QPixmap("./logo4.png")
        self.pixmap1 = self.im.scaled(500, 500, QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.label.setPixmap(self.pixmap1)
        self.setWindowTitle("Plumid")
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Plumid()
    sys.exit(app.exec_())