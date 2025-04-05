import os

def analyze_directory(directory):
    filepaths = []
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            filepaths.append(filepath)
    return filepaths
