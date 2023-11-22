import os
import sys
import webbrowser
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QComboBox,
    QFileDialog,
    QMessageBox,
    QLabel,
    QRadioButton,
)
from PyQt6.QtGui import QPixmap, QIcon

from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from PyQt6.QtCore import Qt

class YoutubeDownloader(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize UI components
        self.init_ui()

                # Set the path to ffmpeg
        self.set_ffmpeg_path()

    def set_ffmpeg_path(self):
        ffmpeg_path = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")
        os.environ["PATH"] += os.pathsep + ffmpeg_path

    def init_ui(self):
        self.setWindowTitle("DeepTube :: Unofficial YouTube Downloader")
        self.setGeometry(300, 300, 400, 280)  # Adjusted height

        # Main widget and layout setup
        self.main_widget = QWidget(self)
        self.main_layout = QVBoxLayout(self.main_widget)
        self.setCentralWidget(self.main_widget)

        # Logo image
        self.logo_label = QLabel(self)
        logo_path = self.img_resouce_path("logo.png")
        self.logo_pixmap = QPixmap(logo_path)
        self.logo_label.setPixmap(self.logo_pixmap)
        self.logo_label.setScaledContents(True)
        self.logo_label.setFixedSize(380, 100)  # Adjust size as needed
        self.main_layout.addWidget(self.logo_label)

        # Add a small space after the logo
        self.main_layout.addSpacing(10)

        # YouTube link input field
        url_label = QLabel("YouTube URL:", self)
        self.main_layout.addWidget(url_label)
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Insert the URL of your YouTube video.")
        self.url_input.setFixedWidth(380)  # Set a fixed width
        self.main_layout.addWidget(self.url_input)

        # Video quality selection
        quality_label = QLabel("Video Quality:", self)
        self.main_layout.addWidget(quality_label)
        self.quality_input = QComboBox(self)
        self.quality_input.addItems(
            ["360p", "480p", "720p", "1080p", "1440p", "2160p", "best", "worst"]
        )
        self.quality_input.setFixedWidth(380)  # Set a fixed width
        self.main_layout.addWidget(self.quality_input)

        # Audio format selection
        audio_label = QLabel("Audio Format:", self)
        self.main_layout.addWidget(audio_label)
        self.audio_format_input = QComboBox(self)
        self.audio_format_input.addItems(
            ["best", "aac", "flac", "mp3", "m4a", "opus", "vorbis", "wav"]
        )
        self.audio_format_input.setFixedWidth(380)  # Set a fixed width
        self.main_layout.addWidget(self.audio_format_input)

        # Video format selection
        video_format_label = QLabel("Video Format:", self)
        self.main_layout.addWidget(video_format_label)
        self.video_format_input = QComboBox(self)
        self.video_format_input.addItems(["mp4", "mkv", "webm"])
        self.video_format_input.setFixedWidth(380)  # Set a fixed width
        self.main_layout.addWidget(self.video_format_input)

        # Video download radio button
        self.video_radio = QRadioButton("Video Download", self)
        self.video_radio.setChecked(True)
        self.video_radio.toggled.connect(self.handle_video_radio)
        self.main_layout.addWidget(self.video_radio)

        # Audio download radio button
        self.audio_radio = QRadioButton("Audio only", self)
        self.audio_radio.setChecked(False)
        self.audio_radio.toggled.connect(self.handle_audio_radio)
        self.main_layout.addWidget(self.audio_radio)

        # Download button
        self.download_button = QPushButton("Download", self)
        self.download_button.clicked.connect(self.start_download)
        self.download_button.setFixedWidth(380)  # Set a fixed width
        self.main_layout.addWidget(self.download_button)

        self.icon_button = QPushButton("", self)
        github_icon_path = self.img_resouce_path("github-mark.png")
        self.icon_button.setIcon(QIcon(github_icon_path))  # Replace 'icon.png' with your icon file
        self.icon_button.clicked.connect(self.handle_icon_button)
        self.icon_button.setFixedWidth(30)  # Set a fixed width
        self.icon_button.setStyleSheet(
            "QPushButton {background-color: transparent; border: none;}"
        )
        self.main_layout.addWidget(self.icon_button)

        # Add some spacing between components
        self.main_layout.addSpacing(10)

        self.show()
        
    def img_resouce_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.dirname(__file__)
        return os.path.join(base_path, relative_path)

    def handle_audio_radio(self, state):
        if state == Qt.CheckState.Checked:
            self.quality_input.setEnabled(True)
            self.video_format_input.setEnabled(True)
        else:
            self.quality_input.setEnabled(False)
            self.video_format_input.setEnabled(False)

    def handle_video_radio(self, state):
        if state == Qt.CheckState.Checked:
            self.quality_input.setEnabled(False)
            self.video_format_input.setEnabled(False)
        else:
            self.quality_input.setEnabled(True)
            self.video_format_input.setEnabled(True)

    def start_download(self):
        video_url = self.url_input.text().strip()
        if not video_url:
            QMessageBox.warning(self, "Warning", "Please enter a YouTube link.")
            return

        video_quality = self.quality_input.currentText()
        audio_format = self.audio_format_input.currentText()

        # 파일 저장 경로 대화상자 표시
        save_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Video",
            "/",
            "Video Files (*." + self.video_format_input.currentText() + ")",
        )

        if save_path:
            if self.audio_radio.isChecked():
                save_path = save_path.replace(
                    "." + self.video_format_input.currentText(), f".{audio_format}"
                )  # Change the file extension to audio format

            if self.video_radio.isChecked():
                self.download_video(video_url, video_quality, save_path)

            if self.audio_radio.isChecked():
                self.download_audio(video_url, audio_format, save_path)
        else:
            QMessageBox.warning(
                self, "Warning", "The path to save the file is not specified."
            )

    def download_video(self, video_url, video_quality, save_path):
        # ‘best’로 선택되었을 경우에 적절한 처리
        quality = (
            f"{video_quality}p"
            if video_quality != "best" and not video_quality.endswith("p")
            else video_quality
        )

        video_format = (
            self.video_format_input.currentText()
        )  # Get the selected video format

        ydl_opts = {
            "format": f"bestvideo[height<={quality}]+bestaudio/best[ext={video_format}]",
            "outtmpl": save_path,
            "merge_output_format": video_format,  # Set the merge output format
            "postprocessors": [
                {
                    "key": "FFmpegVideoConvertor",
                    "preferedformat": video_format,
                }
            ],
            "ffmpeg_location": os.path.join(os.path.dirname(sys.executable), "ffmpeg"),
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            QMessageBox.information(self, "Success", "The video download is complete.")
        except DownloadError as e:
            QMessageBox.critical(
                self, "Error", "There was an error downloading the video.\n" + str(e)
            )
        except Exception as e:
            QMessageBox.critical(
                self, "Error", "An unexpected error occurred.\n" + str(e)
            )

    def download_audio(self, video_url, audio_format, save_path):
        if audio_format == "audio":
            save_path = save_path.replace(
                "." + self.video_format_input.currentText(), ".mp3"
            )  # Change the file extension to .mp3
            ydl_opts = {
                "format": "bestaudio/best",
                "outtmpl": save_path,
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ],
                "ffmpeg_location": os.path.join(os.path.dirname(sys.executable), "ffmpeg"),
            }
        else:
            ydl_opts = {
                "format": f"bestaudio/best[ext={audio_format}]",
                "outtmpl": save_path,
                "ffmpeg_location": os.path.join(os.path.dirname(sys.executable), "ffmpeg"),
            }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            QMessageBox.information(self, "Success", "The audio download is complete.")
        except DownloadError as e:
            QMessageBox.critical(
                self, "Error", "There was an error downloading audio.\n" + str(e)
            )
        except Exception as e:
            QMessageBox.critical(
                self, "Error", "An unexpected error occurred.\n" + str(e)
            )

    def handle_icon_button(self):
        webbrowser.open("https://github.com/59rice/Deeptube")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = YoutubeDownloader()
    sys.exit(app.exec())
