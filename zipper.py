import zlib
import zipfile


def compress(file_namess, num):
    print("File Paths:")
    print(file_namess)

    path = "output/"

    # Select the compression mode ZIP_DEFLATED for compression
    # or zipfile.ZIP_STORED to just store the file
    compression = zipfile.ZIP_DEFLATED

    # create the zip file first parameter path/name, second mode
    with zipfile.ZipFile("/output/zips/UkiyoeYokaiZIP#{}.zip".format(num), mode="w") as myzip:
        myzip.write()
    try:
        for file_name in file_namess:
            # Add file to the zip file
            # first parameter file to zip, second filename in zip
            zf.write(path + file_name, file_name, compress_type=compression)

    except FileNotFoundError:
        print("An error occurred")
    finally:
        # Don't forget to close the file!
        zf.close()


file_names = []
zip_size = 0
zip_number = 1
for i in range(1, 4441):
    file_names.append("UkiyoeYokai#{}.png".format(i))
    if zip_size == 500:
        compress(file_names, zip_number)
        file_names.clear()
        zip_number += 1
        zip_size = 0
    zip_size += 1
