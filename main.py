import os
from PIL import Image

# 元画像の倍率設定
ratio = 10

# パスの設定
origin_path = "./origin/"
convert_path = "./convert/"
strage_path = "./strage/"

# 画像ファイルのリスト化
list1 = os.listdir(origin_path)

for i in range(len(list1)):
    # 画像パスの取得
    image_path = os.path.join(origin_path, list1[i])
    # 画像加工
    imagedata = Image.open(image_path)
    width, height = imagedata.size
    width_convert = width / ratio
    height_convert = height / ratio
    imagedata_resize = imagedata.resize((int(width_convert), int(height_convert)))
    # 変換後の画像リネーム
    new_file_name = "new" + list1[i]
    save_path = convert_path + new_file_name
    imagedata_resize.save(save_path, quality=85, optimize=True)
    # 元データの移動
    replace_path = os.path.join(strage_path, list1[i]) 
    os.replace(image_path, replace_path)