<img src="https://github.com/mistertay0dimon/ProgramAnalyze/blob/main/images/ProgramAnalyze_logo.png">
ProgramAnalyze это библиотека для анализа исходного кода программ и показа сколько процентов занимает тот или иной язык программирования
При помощи нее можно создавать скрипты которые анализируют исходный код программы и выводят процентное соотношение языков программирования

Пример:
<img src="https://github.com/mistertay0dimon/ProgramAnalyze/blob/main/images/termux_demo.jpg">

# Установка
```bash
pip install ProgramAnalyze
```

# Пример использования
```python
from ProgramAnalyze import analyze_code, print_results

filepaths = [
    'my_project/server.py'
    'my_project/index.html'
    'my_project/script.js'
]

results = analyze_code(filepaths)
print_results(results)
```

Более упрощённый пример (Со звёздочкой):
```python
from ProgramAnalyze import AnalyzeAll, print_resul>

filepaths = [
    '*'  # Указываем '*' для анализа всех файлов в текущей директории
]

results, file_counts = AnalyzeAll(filepaths)
print_results(results, file_counts)
```
