# 4_module_Final
Это финальный проект курса по селениум. Проект выполнен на версии Python 3.8.2

## Выполните следующии шаги для стабильной работы проекта:

### 1. 

Установите необходимую версию драцвера Chrome и Firefox для Вашей операционной системы по инструкции:

#### Установка и Selenium-драйвера chromedriver для Chrome:

##### для браузера: Windows
- Скачайте с сайта https://sites.google.com/a/chromium.org/chromedriver/downloads драйвер для вашей версии браузера. Разархивируйте скачанный файл.
- Создайте на диске C: папку chromedriver и положите разархивированный ранее файл chromedriver.exe в папку C:\chromedriver.
- Добавьте в системную переменную PATH папку C:\chromedriver. Как это сделать в разных версиях Windows, описано здесь: https://www.computerhope.com/issues/ch000549.htm.

##### для браузера: Linux

- Укажите нужную Вам версию ChromeDriver для загрузки. Для получения ссылки перейдите в браузере на нужную вам версию драйвера по ссылке на https://sites.google.com/a/chromium.org/chromedriver/downloads. На открывшейся странице нажмите на файле для Linux правой кнопкой и скопируйте путь к файлу. 
- Замените в примере ниже путь к файлу для команды wget вашей ссылкой:
wget https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_linux64.zip
```unzip chromedriver_linux64.zip```
- Переместите разархивированный файл с СhromeDriver в нужную папку и разрешите запускать chromedriver как исполняемый файл:
```sudo mv chromedriver /usr/local/bin/chromedriver```
```sudo chown root:root /usr/local/bin/chromedriver```
```sudo chmod +x /usr/local/bin/chromedriver```
- Проверьте, что chromedriver доступен, выполнив команду chromedriver в терминале, вы должны получить сообщение о том, что процесс успешно запущен.
- Если вы получили сообщение "Command 'chromedriver' not found": То повторите установку драйвера по инструкциям выше.

##### для браузера: macOS

- При установке Python вы уже, скорее всего, установили пакетный менеджер Homebrew. Если нет, то сделате это сейчас, а затем с его помощью установить программу wget для загрузки файлов по сети.
```brew install wget```
- Для установки драйвера откройте сайт https://sites.google.com/a/chromium.org/chromedriver/downloads и скопируйте ссылку на ту версию ChromeDriver, которая соответствует версии вашего браузера. Чтобы узнать версию браузера, откройте новое окно в Chrome, в поисковой строке наберите: chrome://version/ — и нажмите Enter. В верхней строчке вы увидите информацию про версию браузера.
```cd ~/Downloads```
```wget https://chromedriver.storage.googleapis.com/76.0.3809.68/chromedriver_mac64.zip```
- Разархивируйте скачанный файл и переместите его в папку /usr/local/bin, чтобы он был глобально доступен в вашей системе.
```unzip chromedriver_mac64.zip```
```sudo mv chromedriver /usr/local/bin```
- Проверьте, что нужная версия chromedriver установлена.
```chromedriver --version```
- Вы должны увидеть ответ системы:
```ChromeDriver 76.0.3809.68 (420c9498db8ce8fcd190a954d51297672c1515d5-refs/branch-heads/3809@{#864})```
- В этом случае все хорошо, и можно переходить к следующему шагу.
- Если вы видите что-то вроде:
```bash: chromedriver: command not found```
то необходимо проверить папку /usr/local/bin на наличие файла chromedriver. Если файла там нет, то нужно повторить команды, описанные выше.


#### Установка Selenium-драйвера geckodriver для Firefox:
- Для установки Firefox скачайте его с официального сайта и установите в вашей ОС: https://www.mozilla.org/firefox/new/.
- Selenium-драйвер для Firefox носит название geckodriver. Скачайте последнюю версию geckodriver с сайта https://github.com/mozilla/geckodriver/releases и распакуйте его в папку C:\geckodriver на Windows, /usr/local/bin на Ubuntu и macOS. Для более подробной инструкции по установке geckodriver смотрите https://selenium-python.com/install-geckodriver. Для Windows не забудьте добавить в системную переменную PATH папку C:\geckodriver и перезапустить командную строку, чтобы путь стал доступен.

---

### 2.

После того как проект скачан на Ваш компьютер, активизируйте виртуально окружение, далее командой в терминале pip install -r requirements.txt
загрузите все необходимые библиотеки.

---

### 3.

Все тесты в терминале можно вызвать командой: ```pytest -s -v test_main_page.py``` или ```pytest -s -v test_product_page.py```

Тесты к финальному заданию необходимо вызвать в терминале командой: ```pytest -v --tb=line --language=en -m need_review```

---

Приятного ознакомления с проектом!!!
