以下是將教學文件轉為 `README.md` 格式的內容：

```markdown
# 動態更新圖表的 Python 程式

本專案是一個 Python 程式，能夠自動讀取 Excel 檔案中的數據並動態更新圖表。程式會持續檢查 Excel 檔案的變動，當檔案更新後，自動重新讀取數據並更新圖表。

## 前置需求

1. **Python**：請確保您的電腦已安裝 Python。
2. **VSCode**：推薦使用 Visual Studio Code 來編輯與執行 Python 程式。
3. **Python 套件**：
   - `pandas`：用於處理 Excel 數據。
   - `matplotlib`：用於繪製圖表。
   - `openpyxl`：用於讀取 `.xltx` Excel 模板檔案。

## 安裝指南

### 1. 安裝 Visual Studio Code

1. 前往 [Visual Studio Code 官方網站](https://code.visualstudio.com/)。
2. 下載適用於您作業系統的安裝檔案（Windows、macOS 或 Linux）。
3. 安裝完成後，開啟 VSCode。

### 2. 安裝 Python

如果您的電腦尚未安裝 Python，請前往 [Python 官方網站](https://www.python.org/)下載並安裝最新版本的 Python。安裝時，請記得勾選 **Add Python to PATH**（將 Python 添加到系統路徑）選項。

### 3. 安裝必要的 VSCode 擴充套件

1. 開啟 VSCode，點擊左側側邊欄的擴充套件圖示（四個方塊組成的圖標）。
2. 搜尋 **Python** 擴充套件並安裝。
3. 安裝完畢後，VSCode 將支援 Python 語法高亮、即時錯誤提示和自動補全功能。

### 4. 安裝必要的 Python 套件

在 VSCode 的終端機中輸入以下命令來安裝所需的套件：

```bash
pip install pandas matplotlib openpyxl
```

這些指令會分別安裝 `pandas`、`matplotlib` 和 `openpyxl`，以便程式碼能夠順利讀取 Excel 檔案並繪製圖表。

## 使用方法

### 1. 準備 Excel 檔案

建立一個 Excel 檔案（例如 `sample_bankroll_data.xltx`），並確保檔案結構如下：

| Tournament Count | Bankroll |
|------------------|----------|
| 1                | 100      |
| 2                | 105      |
| 3                | 110      |
| ...              | ...      |

將此 Excel 檔案放在與程式碼相同的目錄下。

### 2. 撰寫並執行程式碼

1. 在 VSCode 中建立一個 Python 檔案，例如 `main.py`。
2. 將以下程式碼複製並貼上到 `main.py` 中：

   ```python
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
   ```

3. **執行程式**：在終端機中輸入以下命令執行程式：

   ```bash
   python3 main.py
   ```

   程式將持續檢查 Excel 檔案的變動。每當檔案儲存修改後，圖表會自動更新。

### 3. 停止程式

要結束程式，您可以按下 **Ctrl + C**，這會停止程式的執行。

---

完成上述步驟後，您應該可以在每次更新並儲存 Excel 檔案後，自動查看動態更新的圖表。
```

以上即為完整的 `README.md` 教學文件。
