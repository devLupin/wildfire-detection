# Real-time wildfire detection
- author : Lupin

A faster way to detect fire using A.I.

https://github.com/devLupin/wildfire-detection/assets/33558083/a18ba917-625c-4e84-a1ae-9f5265e4ea31

## 01. Used Dataset
<hr>
 
- [화재영상 3D 객체 데이터 생성](https://aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=realm&dataSetSn=71472)
- [WILDFIRE-I](https://data.mendeley.com/datasets/9kz5pfw4xm/3)

## 02. Preprocessing
<hr>

- convert format to Origin dataset <-> COCO dataset
  - refer to `*_preprocess.py`

## 03. Model
<hr>

- **Main**
  - [YOLOv8](https://github.com/ultralytics/ultralytics) transfer learning
- additional
  - RetinaNet : bad performance

## 04. Setting (Windows Only)
<hr>

- prerequisite
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

- [train](yolov8/runs/train/)
- [validation](yolov8/runs/val/)

## License
<hr>

Non-commercial ONLY
