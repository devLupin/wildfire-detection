# 실시간 화재 감지

AI를 이용한 완벽한 화재 감지

- 실시간 감지
  - 카메라(예:CCTV)로부터 얻은 비디오에서 화재 감지
  - 화재가 감지되면 삡 소리가 들립니다.
    - 계속된 감시는 잠이 오게 만드니까요:)
- 유저 신고
  - 누구나 화재 상황을 웹앱을 통해 신고할 수 있습니다.
  - 신고자의 현재 위치와 전화 번호도 함께 전송됩니다.
- 대시보드
  - 녹화된 영상에 화재 감지기를 적용합니다.
  - 각 신고자의 화재 영상, 위치를 확인할 수 있습니다.

![platform](https://user-images.githubusercontent.com/33558083/260911667-3f33d2bc-0fe2-4ff3-9855-b1ce2437ff18.png)

- 예시 (실제로 불을 지를 수 없어, 상황을 재현했습니다.)
  - 실시간 감지

    https://github.com/devLupin/wildfire-detection/assets/33558083/cd6bec32-f55f-46d5-bc14-b751d8a42276

  - 유저 신고

    https://github.com/devLupin/wildfire-detection/assets/33558083/22d12e96-9e88-419d-a0db-85cc7e92c1d4

  - 대시보드

    https://github.com/devLupin/wildfire-detection/assets/33558083/13943350-d262-48b1-a51a-814c87120dfb

 

## 01. 사용된 데이터셋
<hr>
 
- [화재영상 3D 객체 데이터 생성](https://aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=realm&dataSetSn=71472)
- [WILDFIRE-I](https://data.mendeley.com/datasets/9kz5pfw4xm/3)
- [DFireDataset](https://github.com/gaiasd/DFireDataset)

## 02. 전처리
<hr>

- 포맷 변경 (원본 데이터셋 <-> COCO 데이터셋)
  - `preprocess/[Dataset]_preprocess.py` 참고

## 03. 모델
<hr>

- 주요 모델
  - [YOLOv8](https://github.com/ultralytics/ultralytics) 전이 학습
- 추가
  - [RetinaNet](https://arxiv.org/abs/1708.02002) : 성능 나쁨.

## 04. 설정 (Windows만 해당)
<hr>

- 사전 요구사항
  - [위치 API](https://ipstack.com/) 키
    
    ```python
    ## Config.py
    class Config:
      LOCATION_API = 'YOUR_LOCATION_API_KEY'
    ```

  - 가상 환경
    
    ```shell
    conda create -n wildfire-detection python=3.8
    conda activate wildfire-detection
    cd [your-work-dir]
    ```

  - 패키지
    - 우선, CUDA 및 Torch >= 2.0.0
      - 본인은 CUDA 11.7 / Torch == 2.0.0
    - 그리고 나서, `pip install -r [wildfire-detection/requirements.txt]`

- [best.ckpt file](https://drive.google.com/file/d/1VCHBUoSWpHvnYKxJ00bxzmAUKgenF3DZ/view?usp=drive_link) 설치
  - `[wildfire-detection]/yolov8/runs/train/weights`로 이동


## 05. 빠른시작
<hr>

- 우선, 화재 감지 영상을 위해 `detect_video_backend.py` 실행
  - 신고자가 업로드한 영상을 화재가 감지된 영상으로 변환
  - 5초마다 실행

- 웹앱
  - 만약 카메라와 마이크에 대한 권한을 요청하면, 승인해주세요.
  - 콘솔창을 열고,
    - Real-time Detection : [real-time_detection.py](real-time_detection.py)
    - User report : [report.py](report.py)
    - Dashboard : [dashboard.py](dashboard.py)

    ```shell
    cd [wildfire-detection]
    streamlit run [code.py]


    // 다음과 같은 메시지를 확인하실 수 있습니다.
    You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
    Network URL: http://[YOUR-INTERNAL-IP-ADDRESS]:8501
    ```

  - 그리고 http://localhost:[PORT] 접속
    - 외부에서 접속하고 싶다면, 포트포워딩이나 인바운드 규칙을 설정하세요.

## 06. 결과

- [학습](yolov8/runs3/train/)
- [검증](yolov8/runs3/val/)

## 라이센스
<hr>

비상업적인 용도로만 사용 가능합니다.
