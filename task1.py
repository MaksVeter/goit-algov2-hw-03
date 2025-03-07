import os
import shutil
import sys


def copy_files(source_dir, destination_dir):
    try:
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)
            if os.path.isdir(source_path):
                # Рекурсивний виклик для піддиректорій
                copy_files(source_path, destination_dir)
            else:
                _, ext = os.path.splitext(item)
                ext = ext[1:] if ext else 'no_extension'
                dest_subdir = os.path.join(destination_dir, ext)
                os.makedirs(dest_subdir, exist_ok=True)
                dest_path = os.path.join(dest_subdir, item)
                shutil.copy2(source_path, dest_path)
                print(f"Копіюємо {source_path} -> {dest_path}")
    except Exception as e:
        print(f"Помилка при копіюванні: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Не вказані шляхи до вихідної та/або цільової директорій.")
        print(
            "Використання: python3 task1.py <шлях_до_вихідної_директорії> [<шлях_до_цільової_директорії>]")
        sys.exit(1)

    source_dir = sys.argv[1]
    if len(sys.argv) > 2:
        destination_dir = sys.argv[2]
    else:
        destination_dir = "dist"

    if not os.path.exists(source_dir):
        print(f"Шлях до вихідної директорії '{source_dir}' не існує.")
        sys.exit(1)

    copy_files(source_dir, destination_dir)
