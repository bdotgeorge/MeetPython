РЕШЕНИЕ ДЛЯ МАК -в системном терминале вот такую команду запустили: python3 -m pip install --upgrade pip  


РЕШЕНИЕ ДЛЯ WINDOWS - В Windows при установке Python необходимо было установить галочку для установки pip, установить путь Python в папку с:\Program Files, а не в User, и обязательно поставить галочку add PATH

иногнда в винде в командной строке - Set-ExecutionPolicy -ExecutionPolicy AllSigned , если не активируется

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser




вручную надо было добавить pip в Переменную среду Path
Это в свойствах компьютера надо лазить.
На Windows 10. Параметры -> Изменение системных переменных среды -> Переменные среды. Потом находим или создаем Path и добавляем путь до pip.

python -m venv venv
python3 -m venv venv

source venv/bin/activate - мак

venv\Scripts\activate - винда