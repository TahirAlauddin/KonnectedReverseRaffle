pyinstaller -Fw --onefile --name=konnected-reverse-raffle --icon=images/logo/konnected-logo-icon.ico main.py

pyinstaller --name=konnected-server --onefile --additional-hooks-dir=hooks --add-data="reverseRaffle/frontend/static;reverseRaffle/frontend/static" --add-data="reverseRaffle/frontend/templates;reverseRaffle/frontend/templates" --add-data="reverseRaffle/frontend/media;reverseRaffle/frontend/media" manage.py


pyinstaller --name=konnected-server --onefile --additional-hooks-dir=hooks manage.py


1000x650
