import os
import shutil

FOLDER_PATH = 'D:/Загрузки/хром' # Наша папка с фалами для сортировки
OUTER_PATH = 'D:/Загрузки' # Папка в которой будут создаваться наши категории
OTHER = 'Other' # Для неизвестных расширений
# Список расширений и соответствующих папок
EXTENSIONS = {
    'Documents': ('.txt', '.doc', '.docx', '.xls', '.xlsx', '.pdf'),
    'Photos': ('.jpg', '.jpeg', '.png', '.gif'),
    'Videos': ('.avi', '.mp4', '.mkv'),
    'Music': ('.mp3', '.wav'),
    'Archives': ('.rar', '.zip', '.7zip'),
    'Programs': ('.exe', '.msi'),
    '3D_print': ('.stl',),
    'Torrent_files': ('.torrent',)
}
def make_directory() -> None:
    '''Создаем папки, если их нет'''
    for folder in EXTENSIONS.keys():
        folder_path = os.path.join(OUTER_PATH, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)


def check_directory(extension: str) -> str:
    '''Ищем расширение в EXTENSIONS и возвращаем папку'''
    for k, v in EXTENSIONS.items():
        if extension in v:
            return k
    return OTHER


if __name__ == '__main__':
    make_directory()

    # Получаем список файлов в отслеживаемой папке
    files = os.listdir(FOLDER_PATH)
    for file_name in files:
        # Полный путь к файлу
        file_path = os.path.join(FOLDER_PATH, file_name)

        # Получаем расширение файла
        extension = os.path.splitext(file_name)[1]

        if extension: # Если попалась папка или расширения нет, ничего не делаем
            # Получаем название папки по расширению
            folder_name = check_directory(extension)
            folder_path = os.path.join(OUTER_PATH, folder_name)
            shutil.move(file_path, folder_path)