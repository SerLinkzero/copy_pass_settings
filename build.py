# A simple script to build the dist package
import os
import zipfile

# Files or dirs to exclude
excluded = [
    "__pycache__",
]

# Extra files to include
extras = [
    "./README.md",
    "./LICENSE"
]

version = "0.0.1"

base_path = "./src"
directory = "copy_pass_settings"
output = f"./dist/copy_pass_settings_v{version}.zip"


def package_addon(base_path: str, directory: str, output_file: str, include_empty_dirs: bool = True, include_root: bool = True, include_extra_files: bool = False):
    """
    This function is very specific to this project. Not intended for general use.
    """

    archive = zipfile.ZipFile(output_file, "w", zipfile.ZIP_LZMA)

    if directory == "":
        dir_path = base_path
    else:
        dir_path = f"{base_path}/{directory}"

    # Adding extra files

    if include_extra_files:
        arc_path = os.path.basename(dir_path)
        for path in extras:
            if os.path.exists(path):
                file_name = os.path.basename(path)
                archive.write(path, os.path.join(arc_path, file_name))
                # print(f"{path} :: {arc_path} :: {file_name}")

    for path, dir_names, file_names in os.walk(dir_path):

        current_dir = os.path.basename(path)

        # Skip ignores dirs
        if current_dir in excluded:
            continue

        if include_root:
            folder_path = path.replace(base_path, "")
        else:
            folder_path = path

        # Add files to archives
        for file_name in file_names:
            if file_name in excluded:
                continue

            archive.write(os.path.join(path, file_name),
                          os.path.join(folder_path, file_name))

    print(f"Archive create: {output_file}")
    archive.close()


if __name__ == "__main__":
    # input_path = "./src/copy_pass_settings"

    package_addon(
        base_path=base_path,
        directory=directory,
        output_file=output,
        include_empty_dirs=True,
        include_root=True,
        include_extra_files=True)
