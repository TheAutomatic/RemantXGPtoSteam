import os
import shutil
import argparse

def copy_and_rename_files(source, target):
    profilenum = 0
    savenum = 0

    if not os.path.exists(target):
        os.makedirs(target)

    for root, _, files in os.walk(source):
        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)

            if 5120 < size < 94800:
                shutil.copy2(file_path, os.path.join(target, "profile.sav"))
                profilenum += 1
            elif size > 97200:
                shutil.copy2(file_path, os.path.join(target, "save_0.sav"))
                savenum += 1

    print("Success!")
    print(f"profilenum: {profilenum}, savenum: {savenum} (all of them must be 1)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy and rename files based on size.")
    parser.add_argument("source", nargs="?", default=r"C:\Users\user\source", help="Source directory")
    parser.add_argument("target", nargs="?", default=r"C:\Users\user\target", help="Target directory")
    args = parser.parse_args()

    try:
        copy_and_rename_files(args.source, args.target)
    except Exception as e:
        print(f"Error: {e}")
