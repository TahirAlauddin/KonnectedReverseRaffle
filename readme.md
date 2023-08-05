pyinstaller -Fw --onefile --name=konnected-reverse-raffle --icon=images/logo/konnected-logo-icon.ico main.py

pyinstaller --name=konnected-server --onefile --additional-hooks-dir=hooks --add-data="frontend/static;frontend/static" --add-data="frontend/templates;frontend/templates" --add-data="frontend/media;frontend/media" manage.py

pyinstaller --name=konnected-server --onefile --additional-hooks-dir=hooks manage.py


1000x650
