# deeptube :: Unofficial Youtube Downloader

<img width="500" src="https://github.com/59rice/Deeptube/assets/101755125/0699285f-b01b-45da-9e13-a57f54381e3f">

### Simple Video/Audio file downloader for Youtube

![GitHub](https://img.shields.io/github/license/sioaeko/DeepTube-Youtube-Downloader)
![GitHub stars](https://img.shields.io/github/stars/sioaeko/DeepTube-Youtube-Downloader)
![GitHub forks](https://img.shields.io/github/forks/sioaeko/DeepTube-Youtube-Downloader)


----------------------------------------------

## Features

- Download videos in multiple qualities (360p, 480p, 720p, 1080p, 1440p, 2160p, best, worst).
- Download audio in various formats (aac, flac, mp3, m4a, opus, vorbis, wav).
- Support for multiple video formats (mp4, mkv, webm).
- Simple and intuitive user interface.
- Progress bar to track download status.

-------------------------------------------------

## ⚠ Notice!

- Please note that using these libraries to download videos from YouTube may violate YouTube's Terms of Service, so use them responsibly.

## Requirements

- Python 3.6+
- PyQt6
- yt-dlp
- ffmpeg

---------------------------------------------------


# 1. Intuitive user interface

<img width="516" alt="Screenshot 2023-11-22 at 11 41 59 PM" src="https://github.com/59rice/Deeptube/assets/101755125/15ee5ff7-5103-4e44-9893-fdae785f1b46">

> We designed the GUI in PyQt6 for a clean design and used the
We've implemented all the features we think you'll need, without any of the features that would be labeled as concise.

|Functions|verification
|------|---
|Video Download| ✓
|Only Audio Download| ✓
|Video Format(mp4,mkv,webm)| ✓
|Audio Format(aac,flac,mp3,m4a,opus,vorbis,wav)| ✓
|4K Resolution Support | ✓
|Youtube age restriction bypass | X



# 2. Fast Download Speed

<img width="451" alt="Screenshot 2023-11-23 at 3 01 35 AM" src="https://github.com/59rice/Deeptube/assets/101755125/e9435a5a-9fb5-4c09-b440-34a8a006b302">


> We use a split download method to download videos faster.
With ffmpeg, we can quickly combine the videos and serve them to you, so you don't have to wait long to get them.


# 3. Unlimited Download Video 

<img width="447" alt="Screenshot 2023-11-23 at 3 14 40 AM" src="https://github.com/59rice/Deeptube/assets/101755125/dddd1207-6999-4719-a8b2-40470db393fd">

> Since we're an open-source program, we use the
There is no limit to the number of downloads, you can get as many as you want.


# 4. Supports multiple platforms

<img width="200" src="https://github.com/59rice/Deeptube/assets/101755125/88c98b87-bb87-4a3a-9f93-15b414716918">

> Enable broad compatibility by adding support for AMD64 processors, the majority of which are currently used on desktops, starting with Apple's ARM processors.

# 5. Cool program icon

<img width="150" src="https://github.com/59rice/Deeptube/assets/101755125/25909530-073d-435b-ab41-69781298e77f">


-------------------------------------------


## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/DeepTube.git
    cd DeepTube
    ```

2. **Install the required Python packages:**
    ```bash
    pip3 install -r requirements.txt
    ```

3. **Ensure ffmpeg is installed and available in your PATH:**
    - On Ubuntu:
        ```bash
        sudo apt update
        sudo apt install ffmpeg
        ```
    - On Windows:
        - Download `ffmpeg` from [FFmpeg](https://ffmpeg.org/download.html) and add it to your system PATH.

## Usage

1. **Run the application:**
    ```bash
    python3 deeptube_latest.py
    ```

2. **Use the UI to enter the YouTube URL, select the desired quality and format, and specify the download location.**

## Building Executable

To build a standalone executable of DeepTube, follow these steps:

1. **Install PyInstaller:**
    ```bash
    pip3 install pyinstaller
    ```

2. **Generate the spec file and modify it to include additional files:**
    ```bash
    pyinstaller --name=DeepTube --onefile --windowed deeptube_latest.py
    ```

3. **Modify the generated `DeepTube.spec` file to include your resource files (logo, ffmpeg, etc.).**

4. **Build the executable:**
    ```bash
    pyinstaller DeepTube.spec
    ```

5. **Find the executable in the `dist` directory.**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Acknowledgements

- [PyQt6](https://riverbankcomputing.com/software/pyqt/intro)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://ffmpeg.org/)

## Contact

If you have any questions or suggestions, please open an issue or reach out to me at [asanaridev@proton.me].

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=sioaeko/Deeptube-Youtube-Downloader&type=Timeline)](https://star-history.com/#sioaeko/Deeptube-Youtube-Downloader&Timeline)




