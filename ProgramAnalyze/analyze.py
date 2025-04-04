import os

def analyze_code(filepaths):
    total_lines = 0
    language_counts = {}

    for filepath in filepaths:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                total_lines += len(lines)

                # Определение языка на основе расширения файла
                ext = os.path.splitext(filepath)[1].lower()
                language = None
                if ext in ['.py']:
                    language = 'Python'
                elif ext in ['.js']:
                    language = 'JavaScript'
                elif ext in ['.html', '.htm']:
                    language = 'HTML'
                elif ext in ['.css']:
                    language = 'CSS'
                elif ext in ['.java']:
                    language = 'Java'
                elif ext in ['.c', '.cpp', '.h']:
                    language = 'C/C++'
                elif ext in ['.pas', '.pp', '.inc', '.dpr', '.lpr']:
                        language = 'Pascal'
                elif ext in ['.kt']:
                     language = 'Kotlin'
                elif ext in ['.cs']:
                     language = 'C#'

                if language:
                    if language not in language_counts:
                        language_counts[language] = 0
                    language_counts[language] += len(lines)
        except Exception as e:
            print(f"Ошибка при обработке файла {filepath}: {e}")

    if total_lines == 0:
        print("Нет строк кода для анализа.")
        return {}  

    language_percentages = {}
    for language, count in language_counts.items():
        percentage = (count / total_lines) * 100
        language_percentages[language] = percentage

    return language_percentages

def print_results(language_percentages):
    
    if not language_percentages:
        print("Нет данных для отображения.")
        return

    print("Процентное соотношение языков программирования:")
    for language, percentage in language_percentages.items():
        print(f"{language}: {percentage:.2f}%")
