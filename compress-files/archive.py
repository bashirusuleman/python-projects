import zipfile
import pathlib


def archive_files(files,folder):
    dest_path = pathlib.Path(folder, 'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for file in files:
            archive.write(file)
            return


    # with zipfile.ZipFile(dest_path, mode="r") as archive:
    #     print(archive.printdir())
#
