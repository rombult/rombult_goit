import os
import shutil
import re
import glob
import sys

folder_name = ['images', 'videos', 'documents', 'music', 'archives', 'unknown']

MUSIC = "music"
ARCHIVES = "archives"
IMAGES = "images"
VIDEOS = "videos"
DOCUMENTS = "documents"
UNKNOWN = "unknown"

extensions = {
    "ogg": MUSIC,
    "wav": MUSIC,
    "amr": MUSIC,
    "mp3": MUSIC,
    "zip": ARCHIVES,
    "tar": ARCHIVES,
    "gz": ARCHIVES,
    "png": IMAGES,
    "jpeg": IMAGES,
    "svg": IMAGES,
    "jpg": IMAGES,
    "mov": VIDEOS,
    "avi": VIDEOS,
    "mkv": VIDEOS,
    "mp4": VIDEOS,
    "doc": DOCUMENTS,
    "gnp": DOCUMENTS,
    "pptx": DOCUMENTS,
    "xlsx": DOCUMENTS,
    "txt": DOCUMENTS,
    "docx": DOCUMENTS,
    "pdf": DOCUMENTS
}

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r",
               "s", "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize(file_name):

    m = re.match(r"^(.+)\.([\w\d]{2,4})$", file_name)
    file_name = m.group(1)
    extension = m.group(2)
    translated_name = ""
    for let in file_name:
        if TRANS.get(ord(let)):
            translated_name += TRANS[ord(let)]
        else:
            translated_name += let
    translated_name = re.sub(r"[^\w\d]", "_", translated_name)
    return f"{translated_name}.{extension}"


def sort_folders(path):

    files = os.listdir(path)
    print(files)
    for file_item in files:
        if not os.path.isdir(file_item):
            extension = re.match(r".+\.([\w\d]{2,4})$", file_item)
            if extension:
                target_path = extensions.get(extension.group(1), UNKNOWN)
                shutil.move(os.path.join(path, file_item), os.path.join(
                    path, f"{target_path}/{normalize(file_item)}"))


def main():

    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    for folder in folder_name:
        print(os.path.join(path, folder))
        if not os.path.exists(os.path.join(path, folder)):
            os.makedirs(os.path.join(path, folder))
    for path in glob.glob(path, recursive=True):
        print(path)
    sort_folders(path=path)


if __name__ == '__main__':
    main()
    
    
