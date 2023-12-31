# Real-time wildfire detection([한국어](README-KOR.md))

A perfect way to detect fire using A.I.

- Real-time Detection
  - Detect fire from video obtained from cameras(e.g,.CCTV)
  - When detect fire, A beep sounds.
    - Constant surveillance can make you sleepy:)
- User report
  - Anyone can report the current fire situation through the web app.
  - The current location and phone number of the reporter are also sent.
- Dashboard
  - Apply fire detector to recorded video.
  - You can check the fire video and location for each reporter.

![platform](https://user-images.githubusercontent.com/33558083/260911667-3f33d2bc-0fe2-4ff3-9855-b1ce2437ff18.png)

- Examples (I couldn't actually start a fire, so I tried to reproduce the situation.)
  - Real-time Detection with beep sounds

    https://github.com/devLupin/wildfire-detection/assets/33558083/cd6bec32-f55f-46d5-bc14-b751d8a42276

  - User report

    https://github.com/devLupin/wildfire-detection/assets/33558083/22d12e96-9e88-419d-a0db-85cc7e92c1d4

  - Dashboard

    https://github.com/devLupin/wildfire-detection/assets/33558083/13943350-d262-48b1-a51a-814c87120dfb

 

## 01. Used Dataset
<hr>
 
- [화재영상 3D 객체 데이터 생성](https://aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=realm&dataSetSn=71472)
- [WILDFIRE-I](https://data.mendeley.com/datasets/9kz5pfw4xm/3)
- [DFireDataset](https://github.com/gaiasd/DFireDataset)

## 02. Preprocessing
<hr>

- convert format to Origin dataset <-> COCO dataset
  - refer to `preprocess/[Dataset]_preprocess.py`

## 03. Model
<hr>

- **Main**
  - [YOLOv8](https://github.com/ultralytics/ultralytics) transfer learning
- additional
  - [RetinaNet](https://arxiv.org/abs/1708.02002) : bad performance

## 04. Setting (Windows Only)
<hr>

- prerequisite
  - [Location API](https://ipstack.com/) Key
    
    ```python
    ## Config.py
    class Config:
      LOCATION_API = 'YOUR_LOCATION_API_KEY'
    ```

  - Virtual Environment
    
    ```shell
    conda create -n wildfire-detection python=3.8
    conda activate wildfire-detection
    cd [your-work-dir]
    ```

  - Package
    - First, CUDA, Torch >= 2.0.0
      - In my case, CUDA 11.7 / Torch == 2.0.0
    - And then, `pip install -r [wildfire-detection/requirements.txt]`

- Download [best.ckpt file](https://drive.google.com/file/d/1VCHBUoSWpHvnYKxJ00bxzmAUKgenF3DZ/view?usp=drive_link)
  - Move it `[wildfire-detection]/yolov8/runs/train/weights`


## 05. Quick Start
<hr>

- First of all, run `detect_video_backend.py` for make fire detection video.
  - The video uploaded by the reporter is converted into a video in which a fire is detected.
  - Runs every 5 seconds.

- Web APP
  - If asked for permissions to access the camera and microphone, allow it.

  - Open console
    - Real-time Detection : [real-time_detection.py](real-time_detection.py)
    - User report : [report.py](report.py)
    - Dashboard : [dashboard.py](dashboard.py)

    ```shell
    cd [wildfire-detection]
    streamlit run [code.py]


    // You will see these messages.
    You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
    Network URL: http://[YOUR-INTERNAL-IP-ADDRESS]:8501
    ```

  - Then open http://localhost:[PORT]
    - If you want external access, set up port forwarding or inbound rules.

## 06. Result

- [train](yolov8/runs3/train/)
- [validation](yolov8/runs3/val/)

## License
<hr>

Non-commercial ONLY
