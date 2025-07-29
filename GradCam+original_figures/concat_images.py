import os
from PIL import Image

# 作業ディレクトリのパス
base_dir = "/Users/yamawakidaiki/info3dm/FinalReport_G1/GradCam+original"
output_dir = os.path.join(base_dir, "concat_outputs")
os.makedirs(output_dir, exist_ok=True)

# 画像間の隙間（ピクセル単位）
spacing = 10

# ディレクトリ内の全サブディレクトリを処理
for subdir in sorted(os.listdir(base_dir)):
    subdir_path = os.path.join(base_dir, subdir)
    if not os.path.isdir(subdir_path):
        continue

    # .jpgファイルを取得（5枚前提）
    image_files = sorted([f for f in os.listdir(subdir_path) if f.endswith(".jpg")])
    if len(image_files) != 5:
        print(f"スキップ: {subdir} は画像が5枚ではありません")
        continue

    # 画像を読み込み
    images = [Image.open(os.path.join(subdir_path, f)) for f in image_files]

    # 各画像のサイズ取得
    widths, heights = zip(*(img.size for img in images))
    total_width = sum(widths) + spacing * (len(images) - 1)
    max_height = max(heights)

    # 新しい画像キャンバス（RGB）
    new_image = Image.new('RGB', (total_width, max_height), color=(255, 255, 255))  # 背景白

    # 各画像を横に貼り付け（間にspacingを入れる）
    x_offset = 0
    for img in images:
        new_image.paste(img, (x_offset, 0))
        x_offset += img.width + spacing

    # 保存（ディレクトリ名.jpg）
    save_path = os.path.join(output_dir, f"{subdir}.jpg")
    new_image.save(save_path)
    print(f"保存完了: {save_path}")
