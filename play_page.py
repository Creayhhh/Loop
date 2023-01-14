import cv2 as cv
import numpy as np
import datetime
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QMainWindow
from mediapipe.python.solutions import drawing_utils as mp_drawing
from mediapipe.python.solutions import pose as mp_pose

import messagebox
import pose_detection.counter as counter  # 动作计数器
import pose_detection.poseclassifier as pc  # 姿态分类器
import pose_detection.poseembedding as pe  # 姿态关键点编码模块
import pose_detection.resultsmooth as rs  # 分类结果平滑

from window.play_window import Ui_Play_Window, Ui_finishWidget, Ui_pauseWidget, Ui_startWidget

import request


class PlayWindow(QMainWindow, Ui_Play_Window):
    def __init__(self, parent_object, sport="chinning", time=10, parent=None):
        super(PlayWindow, self).__init__(parent)
        self.setupUi(self)
        self.parent_object = parent_object
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.sport = sport
        self.sport_dict = {"chinning": "引体向上", "jumpingJacks": "开合跳", "push": "俯卧撑",
                           "squat": "深蹲", "dumbbell": "哑铃"}

        self.time = int(time)
        self.time_remainder = int(time)
        self.start_time = None

        self.window_width = 0
        self.window_height = 0

        self.init_poseDetection()

        self.cap = cv.VideoCapture(0, cv.CAP_DSHOW)  # 初始化摄像头

        self.init_timer()
        self.init_widget()

    def init_timer(self):
        # 初始化主功能定时器
        self.pose_detection_timer = QTimer()
        self.pose_detection_timer.timeout.connect(self.pose_detection)

        # 初始化一个用于倒计时的定时器
        self.timing_timer = QTimer()
        self.timing_timer.timeout.connect(self.timing)

    def init_widget(self):
        self.startWidget = Ui_startWidget(self)
        self.startWidget.setupUi(self.startWidget)
        self.startWidget.itemLabel.setText(self.sport_dict[self.sport])
        self.startWidget.timeLabel.setText(str(self.time) + ' s')

        self.finishWidget = Ui_finishWidget(self)
        self.finishWidget.setupUi(self.finishWidget)
        self.pauseWidget = Ui_pauseWidget(self)
        self.pauseWidget.setupUi(self.pauseWidget)

        self.finishWidget.hide()
        self.pauseWidget.hide()

        self.pauseWidget.exitButton.clicked.connect(self.exit)
        self.pauseWidget.continueButton.clicked.connect(self.pause)
        self.finishWidget.exitButton.clicked.connect(self.exit)
        self.startWidget.exitButton.clicked.connect(self.exit)
        self.startWidget.startButton.clicked.connect(self.start)

    # 初始化finishWidget和pauseWidget
    def change_widget_position(self):
        self.camLabel.resize(1920, 1080)
        self.countLabel.move(self.window_width - 30 - 250, 30)

        self.startWidget.move(int((self.window_width / 2) - (self.startWidget.width() / 2)),
                              int((self.window_height / 2) - (self.startWidget.height() / 2)))

        self.finishWidget.move(int((self.window_width / 2) - (self.finishWidget.width() / 2)),
                               int((self.window_height / 2) - (self.finishWidget.height() / 2)))

        self.pauseWidget.move(int((self.window_width / 2) - (self.pauseWidget.width() / 2)),
                              int((self.window_height / 2) - (self.pauseWidget.height() / 2)))

    def init_poseDetection(self):
        class_name = ""

        if self.sport == "push":
            class_name = 'push_down'
        elif self.sport == "squat":
            class_name = 'squat_down'
        elif self.sport == "chinning":
            class_name = 'chinning_up'
        elif self.sport == "jumpingJacks":
            class_name = 'jumpingJacks_open'

        self.pose_tracker = mp_pose.Pose()

        self.pose_classifier = pc.PoseClassifier(
            pose_samples_folder="poses_csvs",
            pose_embedder=pe.FullBodyPoseEmbedder(),
            top_n_by_max_distance=30,
            top_n_by_mean_distance=10)

        self.pose_classification_filter = rs.EMADictSmoothing(
            window_size=10,
            alpha=0.2)

        self.repetition_counter = counter.RepetitionCounter(
            class_name=class_name,
            enter_threshold=5,
            exit_threshold=4)

    def timing(self):
        if self.time_remainder >= 0:
            self.timeLabel.setText(str(self.time_remainder))
            self.time_remainder -= 1
        else:
            self.pose_detection_timer.stop()
            self.timing_timer.stop()
            self.finish()

    def pose_detection(self):
        flag, input_frame = self.cap.read()
        input_frame = cv.cvtColor(input_frame, cv.COLOR_BGR2RGB)
        result = self.pose_tracker.process(image=input_frame)
        pose_landmarks = result.pose_landmarks

        output_frame = input_frame.copy()

        if pose_landmarks is not None:
            # 绘制人体关键点
            mp_drawing.draw_landmarks(
                image=output_frame,
                landmark_list=pose_landmarks,
                connections=mp_pose.POSE_CONNECTIONS)

            # Get landmarks.
            frame_height, frame_width = output_frame.shape[0], output_frame.shape[1]
            pose_landmarks = np.array([[lmk.x * frame_width, lmk.y * frame_height, lmk.z * frame_width]
                                       for lmk in pose_landmarks.landmark], dtype=np.float32)
            assert pose_landmarks.shape == (33, 3), 'Unexpected landmarks shape: {}'.format(pose_landmarks.shape)

            # Classify the pose on the current frame.
            pose_classification = self.pose_classifier(pose_landmarks)

            # Smooth classification using EMA.
            pose_classification_filtered = self.pose_classification_filter(pose_classification)

            # Count repetitions.
            repetitions_count = self.repetition_counter(pose_classification_filtered)
            print(repetitions_count)
            self.countLabel.setText(str(repetitions_count))

        showImage = QImage(output_frame.data, output_frame.shape[1], output_frame.shape[0], QImage.Format.Format_RGB888)
        self.camLabel.setPixmap(QPixmap.fromImage(showImage))
        self.camLabel.setScaledContents(True)

    def start(self):
        self.startWidget.hide()
        self.pose_detection_timer.start(30)
        self.timing_timer.start(1000)
        self.start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def pause(self):
        if self.pauseWidget.isHidden() and self.time_remainder > 0:
            self.timing_timer.stop()
            self.pose_detection_timer.stop()
            self.pauseWidget.show()
        else:
            self.pauseWidget.hide()
            self.pose_detection_timer.start(30)
            self.timing_timer.start(1000)

    def finish(self):
        self.finishWidget.countLabel.setText(self.countLabel.text())
        self.finishWidget.timeLabel.setText(str(self.time) + " s")
        self.finishWidget.show()
        record = {
            "username": self.parent_object.userinfo["username"],
            "sport_name": self.sport_dict[self.sport],
            "count": int(self.countLabel.text()),
            "sport_time": int(self.time),
            "start_time": self.start_time
        }

        if not request.submit_sport_record(self.parent_object.token, record):
            messagebox.messagebox_error(self, "My God，记录上传失败了！")

    def exit(self):
        self.cap.release()
        self.close()
        self.parent_object.show()

    # 重写键盘响应事件
    def keyPressEvent(self, event):
        # 如果按下了Esc
        if event.key() == 0x01000000:
            self.pause()

    # 当启用了全屏后，调整camLabel的大小和countLabel的位置，并初始化finishWidget和pauseWidget（改变了尺寸才懂居中的位置）
    def resizeEvent(self, event):
        self.window_width = event.size().width()
        self.window_height = event.size().height()
        if not self.cap.isOpened():
            messagebox.messagebox_error(self, "摄像头打不开 (╯°Д°)╯︵ ┻━┻")
        self.change_widget_position()
