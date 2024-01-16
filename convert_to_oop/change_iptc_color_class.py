import exiftool


class ChangeIptcData:

    # def __new__(cls, *args, **kwargs):
    #     print("metod __new__")

    def __init__(self, file_path, image_title, color_label):
        self.file_path = file_path
        self.image_title = image_title
        self.color_label = color_label

    def change_color_class(self):
        with exiftool.ExifToolHelper() as et:
            et.set_tags(
                [self.file_path],
                tags={"XMP:Title": self.image_title,
                      "XMP:Label": self.color_label
                      },
                params=["-P", "-overwrite_original"]
            )


if __name__ == '__main__':
    editor = ChangeIptcData(
        "/Volumes/big4photo-4/2023/12_December/20231219_Топ менеджер Ъ/20231219DSC_0070.NEF",
        'Man',
        "Red"
        )
    print(editor)

    # editor.change_color_class()
