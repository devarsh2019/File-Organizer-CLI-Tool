import os
import shutil
import argparse

# Define file type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
}

def get_category(file_ext):
    for category, extensions in FILE_TYPES.items():
        if file_ext.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Path does not exist.")
        return

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            _, ext = os.path.splitext(item)
            category = get_category(ext)

            category_folder = os.path.join(folder_path, category)
            os.makedirs(category_folder, exist_ok=True)

            shutil.move(item_path, os.path.join(category_folder, item))
            print(f"✅ Moved: {item} → {category}/")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize files in a folder by type.")
    parser.add_argument("folder", help="Path to the folder to organize")
    args = parser.parse_args()
    organize_folder(args.folder)
