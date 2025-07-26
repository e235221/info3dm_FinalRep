import matplotlib.pyplot as plt
import numpy as np

# 本スクリプトは，各モデルの学習曲線を可視化し，画像ファイルとして保存するために実装されたものである。
# The present script is implemented for the purpose of visualizing the learning curves of each model and saving them as image files.

def plot_learning_curve(epochs, train_acc, val_acc, model_name):
    """
    学習曲線を描画し，ファイルとして保存する関数。
    A function to plot the learning curve and save it to a file.
    """
    # グラフの描画領域を作成する。
    # This process creates a new figure for plotting.
    plt.figure(figsize=(10, 6))

    # 訓練データと検証データの精度をプロットする。
    # This procedure plots the training and validation accuracy.
    plt.plot(epochs, train_acc, 'o-', label='Train Accuracy')
    plt.plot(epochs, val_acc, 's-', label='Validation Accuracy')

    # 【変更点】グラフのタイトルをモデル名のみに設定する。
    # [MODIFICATION] The title of the graph is set to the model name only.
    plt.title(f'{model_name}', fontsize=16)
    
    plt.xlabel('Epoch', fontsize=12)
    plt.ylabel('Accuracy (%)', fontsize=12)
    
    # X軸の目盛りを整数にする。
    # The ticks on the x-axis are set to integer values.
    plt.xticks(epochs)

    # Y軸の範囲を設定して，精度の違いを見やすくする。
    # The range of the y-axis is defined to enhance the visibility of accuracy differences.
    min_acc = min(min(train_acc), min(val_acc))
    plt.ylim(min(94, min_acc - 0.5), 100.1)

    # グリッドと凡例を表示する。
    # The grid and legend are subsequently displayed.
    plt.grid(True)
    plt.legend(fontsize=12)

    # 【変更点】グラフをPNGファイルとして保存する。ファイル名はモデル名に基づく。
    # [MODIFICATION] The plot is saved as a PNG file, with the filename based on the model name.
    filename = f"{model_name}.png"
    plt.savefig(filename, dpi=300)
    
    # 【追加点】描画領域を閉じてメモリを解放する。
    # [ADDITION] The figure is closed to release memory.
    plt.close()

    print(f"グラフを '{filename}' という名前で保存しました。")


# 各モデルの学習データ。
# The training data for each respective model is defined below.
# 情報源: ユーザー提供のLaTeXテーブル
data = {
    'ResNet-18': {
        'epochs': np.arange(1, 11),
        'train_acc': [97.92, 99.23, 99.47, 99.61, 99.68, 99.76, 99.83, 99.83, 99.88, 99.88],
        'val_acc': [99.28, 99.22, 99.53, 99.48, 99.52, 99.38, 99.59, 99.51, 99.45, 99.52]
    },
    'ResNet-34': {
        'epochs': np.arange(1, 11),
        'train_acc': [97.74, 99.27, 99.40, 99.55, 99.59, 99.65, 99.72, 99.80, 99.79, 99.84],
        'val_acc': [99.08, 99.34, 99.27, 99.50, 99.40, 99.27, 99.31, 99.49, 99.56, 99.47]
    },
    'ResNet-50': {
        'epochs': np.arange(1, 11),
        'train_acc': [95.26, 98.69, 99.10, 99.32, 99.39, 99.50, 99.54, 99.66, 99.71, 99.75],
        'val_acc': [98.58, 98.76, 99.20, 99.25, 99.34, 99.37, 99.40, 99.28, 99.36, 99.39]
    },
    'EfficientNet': {
        'epochs': np.arange(1, 11),
        'train_acc': [94.47, 99.00, 99.40, 99.63, 99.79, 99.85, 99.89, 99.92, 99.93, 99.95],
        'val_acc': [98.76, 99.19, 99.54, 99.59, 99.79, 99.82, 99.94, 99.96, 99.87, 99.96]
    },
    'CustomModel': {
        'epochs': list(range(1, 11)),
        'train_acc': [99.48, 100.00, 100.00, 99.97, 100.00, 100.00, 100.00, 100.00, 100.00, 100.00],
        'val_acc': [100.00, 99.99, 99.99, 100.00, 100.00, 100.00, 100.00, 100.00, 100.00, 100.00]
	}
    }

# 各モデルのデータを用いて学習曲線をプロットし，保存する。
# The learning curve for each model is plotted and saved using its corresponding data.
for model_name, model_data in data.items():
    plot_learning_curve(
        model_data['epochs'],
        model_data['train_acc'],
        model_data['val_acc'],
        model_name
    )

print("\nすべてのグラフの保存が完了しました。")
