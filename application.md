## Подготовка рабочего пространства (направлено на пользователей Windows)

Для начала работы с проектом необходимо скачать [GitBash](https://gitforwindows.org/). После скаивания и установки GitBash, нужно скачать [Anaconda](https://www.anaconda.com/download#downloads): Linux, 64-Bit (x86) Installer (860 MB). Затем скаченный файл *Anaconda3-2023.03-1-Linux-x86_64.sh* необходимо перенести в предпологаемую рабочую папку. В этой папке нужно кликнуть правой кнопкой мыши по свободному пространству, в появившемся окно нежать *Git Bash Here*. В появившемся терминале необходимо прописать следующую команду: bash Anaconda3-2023.03-1-Linux-x86_64.sh

Во всех всплывающих сообщениях нужно написать *yes*, когда сообщения перестанут появляться на экране ничего делать не нужно, это означает процесс устанвки. Когда появится появится похожая надпись: *wqsad@DESKTOP-AGCG4T3 MINGW64 /c/proj* необходимо прописать *exit* и перезагрузить компьютер.

После перезагрузки компьютера, снова нужно открыть GitBash в рабочей папке и прописать следующие команды:

1) conda create -n kandinsky python=3.9
2) conda create -n StableDiffusion python=3.9
3) conda create -n shap python=3.9
4) git clone https://github.com/keoni02032/MouseHub.git
5) echo ". ${PWD}/conda.sh" >> ~/.bashrc
6) echo ". '${PWD}'/conda.sh" >> ~/.bashrc

Теперь нужно прописать *exit* и снова открыть рабочий терминал GitBash.

## Настройка окружения для модели Kandinsky-2

Перед началом работы с каждым из приведенных ниже инструментов необходимо сначала прописать соответствующие ему команды:

1) conda activate kandinsky
2) cd Kandinsky-2
3) pip install "git+https://github.com/ai-forever/Kandinsky-2.git"
4) pip install git+https://github.com/openai/CLIP.git

## Настройка окружения для модели Stable Diffusion

1) conda activate StableDiffusion
2) cd finetuned_diffusion
3) pip install -r requirements.txt
4) pip install gradio

## Настройка окружения для модели shap-e

1) conda activate shap
2) cd shap-e
3) pip install -e .

В случае использования впервые нужно прописывать все команды. Для дальнейшего использования нужно писать только первые два пункта для каждой модели.
