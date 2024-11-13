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
