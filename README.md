# Real-time wildfire detection

A perfect way to detect fire using A.I.

- Real-time Detection
  - Detect fire from images obtained from cameras(e.g,.CCTV)
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
  - Real-time Detection

  - User report

  - Dashboard

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
    conda create -n fire-detection python=3.8
    conda activate fire-detection
    cd [your-work-dir]
    ```

  - Package
    - First, CUDA, Torch >= 2.0.0
      - In my case, CUDA 11.7 / Torch >= 2.0.0
    - And then, `pip install -r [fire-detection/requirements.txt]`

- Install [best.ckpt file](https://drive.google.com/file/d/1QDZ6sb2CwK5jALB5LAwaW2LkHUxd8PI0/view?usp=sharing)
  - Move it `[wildfire-detection]/yolov8/runs/train/weights`


## 05. Quick Start
<hr>

- Fire Detection from webcam
  - Then run it with Streamlit and open http://localhost:8501/.
    - You see the app view, so click the "START" button.
    - Then, video and audio streaming starts. If asked for permissions to access the camera and microphone, allow it.

  ```shell
  cd [wildfire-detection]
  streamlit run app.py
  ```

## 06. Result

- [train](yolov8/runs3/train/)
- [validation](yolov8/runs3/val/)

## License
<hr>

Non-commercial ONLY
