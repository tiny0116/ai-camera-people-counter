import time
from camera import Camera
from yolo_inference import YoloDetector
from nlp_agent import NLPEngine

def main():
    # 初始化 NLP, Camera, YOLO
    nlp = NLPEngine()
    cam = Camera(camera_index=0)
    detector = YoloDetector(model_path="models/yolov8n.pt", device="cpu")  # or "cuda" if GPU is available

    try:
        print("=== AI Camera People Counter ===")
        print("輸入指令 (e.g. '現場人數')，或輸入 'exit' 結束。")

        while True:
            user_input = input("\n請輸入指令: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print("程式結束。")
                break

            # Step 1: NLP 分析意圖
            intent = nlp.parse_intent(user_input)
            print(f"辨識意圖: {intent}")

            # Step 2: 依照意圖做對應行為
            if intent == "CountPeopleInFrame":
                print("啟動攝影機擷取畫面...")
                frame = cam.get_frame()
                person_count = detector.count_person(frame)
                print(f"【偵測結果】 鏡頭中人數: {person_count}")
            else:
                print("目前不支援此指令，請再試一次。")

    except KeyboardInterrupt:
        print("偵測到 Ctrl+C，程式結束。")
    finally:
        cam.release()

if __name__ == "__main__":
    main()
