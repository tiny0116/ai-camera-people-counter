# ai-camera-people-counter
「對 AI 輸入『現場人數』『鏡頭中人數』等關鍵詞」→ 呼叫人數偵測功能 → 實際透過鏡頭拍攝 → 偵測畫面中有多少人 → 回傳或顯示結果。
ai-camera-people-counter/
│
├─ README.md               # 專案說明：運行步驟、硬體需求、配置方式
├─ requirements.txt        # Python 所需套件列表
├─ Dockerfile             # (選擇性) 若要容器化，可撰寫 Dockerfile
├─ .gitignore
│
├─ src/
│   ├─ main.py             # 主程式入口：負責解析指令/啟動人數偵測/輸出結果
│   ├─ camera.py           # 控制攝影機的模組 (Raspberry Pi Camera 或 USB Camera)
│   ├─ yolo_inference.py   # YOLOv8 (或 YOLOv5) 推論流程
│   ├─ nlp_agent.py        # (範例) 若要模擬 AI Agent 對指令做 NLP 分析
│   └─ config.py           # (選擇性) 儲存一些參數或 API Key
│
├─ models/
│   └─ yolov8n.pt          # (範例) YOLOv8 輕量化模型檔，可自行下載放置
│
└─ tests/
    └─ test_main.py        # (選擇性) 單元測試檔
