import os
from tkinter import Tk, Label, Button, Scale, HORIZONTAL
from PIL import Image

class ImageResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Resizer")

        # フォルダパスの設定
        self.origin_path = "./origin/"
        self.convert_path = "./convert/"
        self.storage_path = "./storage/"

        # 必要なフォルダがなければ作成
        for path in [self.origin_path, self.convert_path, self.storage_path]:
            if not os.path.exists(path):
                os.makedirs(path)
        
        # ユーザー入力用のUI設定
        Label(root, text="Resize Ratio (1 to 100):").pack()
        self.resize_ratio = Scale(root, from_=1, to=100, orient=HORIZONTAL)
        self.resize_ratio.set(10)  # デフォルトのリサイズ比率を10に設定
        self.resize_ratio.pack()

        Label(root, text="Quality (1 to 100):").pack()
        self.quality = Scale(root, from_=1, to=100, orient=HORIZONTAL)
        self.quality.set(85)  # デフォルトの品質を85に設定
        self.quality.pack()

        Button(root, text="Resize Images", command=self.resize_images).pack()

    def resize_images(self):
        list_files = os.listdir(self.origin_path)
        for file_name in list_files:
            image_path = os.path.join(self.origin_path, file_name)
            if os.path.isfile(image_path):
                # 画像加工
                imagedata = Image.open(image_path)
                width, height = imagedata.size
                ratio = self.resize_ratio.get()
                quality = self.quality.get()
                width_convert = int(width / ratio)
                height_convert = int(height / ratio)
                imagedata_resize = imagedata.resize((width_convert, height_convert))
                
                # 変換後の画像リネームと保存
                new_file_name = "new_" + file_name
                save_path = os.path.join(self.convert_path, new_file_name)
                imagedata_resize.save(save_path, quality=quality, optimize=True)
                
                # 元データの移動
                replace_path = os.path.join(self.storage_path, file_name) 
                os.replace(image_path, replace_path)

        print("Image resizing completed.")

def main():
    root = Tk()
    app = ImageResizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
