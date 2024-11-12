import pandas as pd
import matplotlib.pyplot as plt
import time
import os

# 定義 Excel 檔案路徑
file_path = './sample_bankroll_data.xltx'  # 替換為你的檔案路徑
last_modified_time = None

def update_chart(file_path):
    """
    從 Excel 檔案讀取數據並繪製圖表
    """
    # 讀取 Excel 資料
    df = pd.read_excel(file_path)

    # 確保數據格式正確
    tournament_count = df['Tournament Count']
    bankroll = df['Bankroll']

    # 清除之前的圖表並繪製新圖表
    plt.clf()
    plt.plot(tournament_count, bankroll, 'o-', color='blue', label="Bankroll")
    plt.axhline(y=100, color='green', linestyle='--', label="Initial Bankroll (100 USD)")
    plt.axhline(y=30, color='red', linestyle='--', label="Stop-Loss (30 USD)")

    # 添加標題和標籤
    plt.title("MTT Bankroll Progression with 30 USD Stop-Loss")
    plt.xlabel("Tournament Count")
    plt.ylabel("Bankroll (USD)")

    # 顯示圖例
    plt.legend()

    # 顯示更新後的圖表
    plt.draw()
    plt.pause(0.1)  # 暫停以允許更新顯示

# 初始化圖表
plt.ion()  # 開啟互動模式
plt.figure(figsize=(10, 6))

# 每隔5秒檢查文件變動
try:
    while True:
        # 獲取檔案最後修改時間
        modified_time = os.path.getmtime(file_path)

        # 檢查檔案是否有更新
        if last_modified_time is None or modified_time != last_modified_time:
            last_modified_time = modified_time
            update_chart(file_path)
            print("檢測到 Excel 檔案變動，圖表已更新。")

        # 每隔5秒檢查一次
        time.sleep(5)

except KeyboardInterrupt:
    print("程式終止。")
finally:
    plt.ioff()  # 關閉互動模式
    plt.show()  # 顯示最終圖表
