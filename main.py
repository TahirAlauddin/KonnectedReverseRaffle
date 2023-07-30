import sys, time, subprocess
from PyQt5.QtCore import QUrl, pyqtSlot, QThread, pyqtSignal, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QProgressBar,QAction, QVBoxLayout, QLabel, QWidget, QSizePolicy
from PyQt5.QtGui import QContextMenuEvent, QIcon, QFont
from PyQt5.QtWebEngineWidgets import QWebEnginePage
import urllib3
import ctypes

myappid = 'tahiralauddin.konnected-reverse-raffle.1.0.0' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

PORT = 8323

class CustomErrorPage(QWebEnginePage):
    def __init__(self, parent=None):
        super(CustomErrorPage, self).__init__(parent)
        self.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, ok):
        if not ok:
            # Custom error message
            error_html = """
            <html><body><h1>Internal Server Error</h1>
            <p>There was an error trying to connect with backend.</p>
            </body></html>
            """
            self.setHtml(error_html)
            # Alternatively, you could load a custom error page like so:
            # self.load(QUrl('path/to/your/error_page.html'))


class LoadingPage(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window size
        self.setMinimumWidth(1000)
        self.setMinimumHeight(650)

        # Set up loading label
        self.loading_label = QLabel('Loading page...')
        self.loading_label.setFont(QFont('Arial', 20))
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Set up progress bar (optional)
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)  # Makes it an indeterminate progress bar

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.loading_label)
        layout.addWidget(self.progress_bar)

        # Set up container for loading page
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # QSS Styling
        qss_style = """
            QLabel {
                color: #3A405A;
            }
            QProgressBar {
                border: 2px solid #3A405A;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #3A405A;
                width: 10px;
            }
        """
        self.setStyleSheet(qss_style)
        
        self.setWindowTitle("Konnected Reverse Raffle")
        self.setWindowIcon(QIcon("images/logo/konnected-logo-icon.png"))
        
        self.setMinimumWidth(1000)
        self.setMinimumHeight(650)

        # Set up a separate thread to run subprocess command
        self.subprocess_thread = SubprocessThread()
        self.subprocess_thread.output_detected.connect(self.switch_to_browser)
        self.subprocess_thread.start()

    def switch_to_browser(self):
        self.browser = Browser()
        self.setCentralWidget(self.browser)
        self.browser.load(QUrl(f'http://localhost:{PORT}/admin/')) # or the URL you want to load


class SubprocessThread(QThread):
    output_detected = pyqtSignal()

    def is_server_responding(url):
        # retries = urllib3.Retry(total=50, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
        http = urllib3.PoolManager()

        try:
            # Send a GET request to the URL
            response = http.request('GET', url)

            # If the server responds with a status code that is 200-299, it's considered successful
            if 200 <= response.status < 500:
                return True
        except Exception as e:
            print(f"An error occurred: {e}")

        return False


    def run(self):
        # Detect if running as a PyInstaller package
        if getattr(sys, 'frozen', False):
            command = f'konnected-server.exe runserver {PORT} --noreload'
            subprocess.Popen(command, shell=True)
            # Check for output
            while True:
                try:
                    if SubprocessThread.is_server_responding(f'http://localhost:{PORT}/'):
                        self.output_detected.emit()
                        break
                    time.sleep(1) # Avoid busy-waiting
                except:
                    pass
        else:
            self.output_detected.emit()

class Browser(QWebEngineView):
    def __init__(self):
        super(Browser, self).__init__()
        url = f'http://localhost:{PORT}/admin/'

        # Clear the cache
        # QWebEngineProfile.defaultProfile().clearHttpCache()

        self.setPage(CustomErrorPage(self))

        self.load(QUrl(url))

        self.setMinimumWidth(1000)
        self.setMinimumHeight(650)
        
        self.setWindowTitle("Konnected Reverse Raffle")
        self.setWindowIcon(QIcon("images/logo/konnected-logo-icon.png"))

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)

        # Add a reload action
        reload_action = QAction('Reload', self)
        reload_action.triggered.connect(self.reloadPage)
        context_menu.addAction(reload_action)

        # Show the context menu at the event's position
        context_menu.exec_(event.globalPos())

    def reloadPage(self):
        self.reload()


# if __name__ == "__main__":
#     # browser = HtmlGetter('http://localhost:{PORT}/admin/')
#     import sys
#     import subprocess
#     # Detect if running as a PyInstaller package
#     if getattr(sys, 'frozen', False):
#         subprocess.run(f'konnected-server.exe runserver {PORT} --noreload')
 
#     app = QApplication(sys.argv)
#     browser = Browser()
#     browser.show()
#     sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoadingPage()
    window.show()
    sys.exit(app.exec_())