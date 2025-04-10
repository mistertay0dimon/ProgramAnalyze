import os
from ProgramAnalyze.directory_analyzer import analyze_directory

def get_language(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext in ['.py']:
        return 'Python'
    elif ext in ['.js']:
        return 'JavaScript'
    elif ext in ['.html', '.htm']:
        return 'HTML'
    elif ext in ['.css']:
        return 'CSS'
    elif ext in ['.java']:
        return 'Java'
    elif ext in ['.c', '.cpp', '.h']:
        return 'C/C++'
    elif ext in ['.pas', '.pp', '.inc', '.lpr']:
        return 'Pascal'
    elif ext in ['.kt']:
        return 'Kotlin'
    elif ext in ['.cs']:
        return 'C#'
    elif ext in ['.bat']:
        return 'Batch'
    elif ext in ['.ps1']:
        return 'PowerShell'
    elif ext in ['.dpr']:
        return 'Delphi'
    else:
        return None

def analyze_code(filepaths):
    if '*' in filepaths and len(filepaths) == 1:
        filepaths = analyze_directory(".")

    total_lines = 0
    language_counts = {}
    file_counts = {}

    for filepath in filepaths:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                total_lines += len(lines)

                language = get_language(filepath)
                if language:
                    if language not in language_counts:
                        language_counts[language] = 0
                        file_counts[language] = 0
                    language_counts[language] += len(lines)
                    file_counts[language] += 1
        except FileNotFoundError:
            print(f"Ошибка: Файл {filepath} не найден.")
            continue
        except Exception as e:
            print(f"Ошибка при обработке файла {filepath}: {e}")
            continue

    if total_lines == 0:
        print("Нет строк кода для анализа.")
        return {}, {}

    language_percentages = {}
    for language, count in language_counts.items():
        percentage = (count / total_lines) * 100
        language_percentages[language] = percentage

    return language_percentages, file_counts

def print_results(language_percentages, file_counts):
    if not language_percentages:
        print("Нет данных для отображения.")
        return

    print("Процентное соотношение языков программирования:")
    for language, percentage in language_percentages.items():
        print(f"{language}: {percentage:.2f}% (Файлов: {file_counts[language]})")
