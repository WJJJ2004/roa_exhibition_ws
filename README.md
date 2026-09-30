# ROA 전시용 모션 플레이어

ROA 21-DOF 로봇에서 게임패드로 인사, 경례, 악수 모션을 실행하기 위한 ROS 2
workspace입니다. Hardware interface와 motion player는 전시용 100 Hz 설정을
사용합니다.

[RViz 실행 영상](docs/rviz.webm)

자세한 하드웨어 실행 및 안전 절차는 [전체 실행 가이드](docs/로아_전시회_운영가이드.pdf)를
참고하세요.

## Clone

```bash
git clone --recurse-submodules https://github.com/WJJJ2004/roa_exhibition_ws.git
cd roa_exhibition_ws
git submodule update --init --recursive
```

## 빌드

기존 보행용 `~/colcon_ws`를 source하지 않은 새 터미널에서 실행합니다.

```bash
./build_exhibition.sh
```

## 환경 소싱

전시 시스템을 실행할 새 터미널마다 다음 스크립트를 source합니다.

```bash
cd roa_exhibition_ws
source setup_exhibition.bash
```
