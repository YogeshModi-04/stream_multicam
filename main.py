import cv2
import threading
import queue
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class ThreadedCamera(threading.Thread):
    def __init__(self, camID, frame_queue):
        threading.Thread.__init__(self)
        self.camID = camID
        self.frame_queue = frame_queue

    def run(self):
        cam = cv2.VideoCapture(self.camID)
        while True:
            ret, frame = cam.read()
            if not ret:
                break
            if not self.frame_queue.full():
                self.frame_queue.put(frame)
        cam.release()

class App(QtWidgets.QWidget):
    def __init__(self, frame_queue1, frame_queue2):
        super().__init__()
        self.frame_queue1 = frame_queue1
        self.frame_queue2 = frame_queue2
        self.init_ui()

    def init_ui(self):
        self.image_label1 = QtWidgets.QLabel(self)
        self.image_label2 = QtWidgets.QLabel(self)
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.image_label1)
        layout.addWidget(self.image_label2)
        self.setLayout(layout)
        self.setWindowTitle('Camera View')

        self.timer1 = QtCore.QTimer()
        self.timer1.timeout.connect(self.update_image1)
        self.timer1.start(20)

        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.update_image2)
        self.timer2.start(20)

    def update_image1(self):
        if not self.frame_queue1.empty():
            frame = self.frame_queue1.get()
            self.display_image(frame, self.image_label1)

    def update_image2(self):
        if not self.frame_queue2.empty():
            frame = self.frame_queue2.get()
            self.display_image(frame, self.image_label2)

    def display_image(self, frame, label):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(QtGui.QPixmap.fromImage(p))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Q:
            self.close()  # Close the application

if __name__ == '__main__':
    frame_queue1 = queue.Queue(10)
    frame_queue2 = queue.Queue(10)
    app = QtWidgets.QApplication(sys.argv)
    ex = App(frame_queue1, frame_queue2)
    ex.show()

    thread1 = ThreadedCamera("rstp/video", frame_queue1)
    thread2 = ThreadedCamera("rstp/video", frame_queue2)
    thread1.start()
    thread2.start()

    try:
        sys.exit(app.exec_())
    except SystemExit as e:
        print("Exiting application:", e)
