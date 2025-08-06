# Pydroid 안녕

Python, Kivy, Buildozer로 만든 "Hello, World!" 모바일 애플리케이션이다.

## 사전 요구 사항

*   [Python](https://www.python.org/) (호환성을 위해 >=3.8, <3.13 버전 권장)
*   Python 의존성 관리를 위한 [Poetry](https://python-poetry.org/)
*   안드로이드 패키지 빌드를 위한 [WSL(Windows Subsystem for Linux)](https://learn.microsoft.com/ko-kr/windows/wsl/install)

## 1. 개발 환경 설정 (Windows)

이 프로젝트는 Poetry를 사용하여 의존성을 관리한다.

1.  **의존성 설치:**
    프로젝트 최상위 폴더에서 터미널을 열고 다음을 실행한다:
    ```bash
    poetry install
    ```

2.  **데스크톱에서 앱 실행:**
    안드로이드용으로 빌드하기 전에 데스크톱에서 Kivy 애플리케이션을 테스트하려면 다음을 실행한다:
    ```bash
    poetry run python main.py
    ```

## 2. 안드로이드용 빌드 (WSL)

안드로이드 APK(앱 패키지)는 반드시 Linux 환경에서 빌드해야 한다. 이를 위해 WSL을 사용한다.

> **⚠️ 주의:** WSL에서 Buildozer를 사용하여 빌드할 때는 Windows에 설치된 Python 버전과 WSL에 설치된 Python 버전을 동일하게 유지하는 것이 중요하다. 버전이 다를 경우, `poetry.lock` 파일과의 비호환성으로 인해 의존성 관련 문제가 발생할 수 있다.

1.  **WSL 설치:**
    WSL이 설치되어 있지 않다면, PowerShell이나 명령 프롬프트를 관리자 권한으로 열고 다음을 실행한다:
    ```bash
    wsl --install
    ```
    필요하다면 컴퓨터를 재시작한다. 이 과정은 보통 최신 버전의 Ubuntu를 설치한다.

2.  **WSL로 프로젝트 복사:**
    Windows 탐색기에서 전체 프로젝트 폴더(`c:\_work_github_sc7258_demo\pydroid-hello`)를 WSL의 홈 폴더와 같은 디렉터리(예: `~/pydroid-hello`)로 복사한다. Windows 탐색기 주소창에 `\\wsl$`를 입력하여 WSL 파일 시스템에 접근할 수 있다.

3.  **WSL에 Buildozer 및 의존성 설치:**
    WSL 터미널을 열고 방금 복사한 프로젝트 디렉터리로 이동한다. 그런 다음, 아래 명령어를 실행하여 필요한 모든 도구를 설치한다.

    ```bash
    # 패키지 목록 업데이트
    sudo apt update

    # Buildozer에 필요한 시스템 의존성 설치
    sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev

    # Buildozer 및 관련 Python 의존성 설치
    pip install --upgrade cython
    pip install buildozer
    ```

4.  **안드로이드 APK 빌드:**
    설치가 완료되면, 아래 명령어를 실행하여 디버그용 APK를 빌드한다. 처음 실행 시에는 안드로이드 SDK와 NDK를 다운로드해야 하므로 시간이 오래 걸릴 수 있다.

    ```bash
    buildozer android debug
    ```

5.  **앱 실행:**
    빌드가 완료되면 `bin/` 디렉터리에서 APK 파일(예: `pydroid-hello-0.1-debug.apk`)을 찾을 수 있다. 이 파일을 안드로이드 기기로 복사하여 설치하고 애플리케이션을 실행한다.
