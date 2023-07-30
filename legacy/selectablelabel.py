from PyQt5.QtWidgets import QLabel


class SelectableLabel(QLabel):
    
    def __init__(self, image_path, *args, **kwargs):
        self.window = kwargs.pop('window')
        self.custom_image = kwargs.pop('custom_image', False)
        self.image_path = image_path
        super().__init__(*args, **kwargs)


    def mousePressEvent(self, ev) -> None:
        if self.window:
            self.window.selectBackgroundImage(self, self.custom_image)
        return super().mousePressEvent(ev)
