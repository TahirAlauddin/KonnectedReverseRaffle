import os
from platform import system

def install_fonts(font_path):


    if system().lower() == 'windows':
        import win32api
        import win32con
        
        # Register the font
        win32api.AddFontResource(font_path, win32con.FR_PRIVATE, 0)

        # Broadcast the WM_FONTCHANGE message to inform other windows of the font change
        win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_FONTCHANGE, 0, 0)

    elif system().lower() == 'darwin':
        from fontTools.ttLib import TTFont

        # Load the font file using fontTools
        font = TTFont(font_path)

        # Get the font name
        font_name = font["name"].getName(1, 3, 1, 1033).toUnicode()

        # Define the destination font directory
        font_dir = os.path.expanduser('~/Library/Fonts')

        # Create the font directory if it doesn't exist
        os.makedirs(font_dir, exist_ok=True)

        # Save the font file to the destination font directory
        font.save(os.path.join(font_dir, font_name + ".ttf"))

    else:
        # OS not supported
        raise Exception("OS not supported")
    