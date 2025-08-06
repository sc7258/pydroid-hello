# 빌드 환경 설정 및 APK 생성 가이드

이 문서는 `pydroid-hello` 애플리케이션을 개발하고 안드로이드 APK로 빌드하기 위한 전체 환경 설정 과정을 안내합니다.

개발은 Windows에서 진행하고, 안드로이드 빌드는 WSL(Windows Subsystem for Linux)을 사용하는 것을 기준으로 설명합니다.

## 사전 요구 사항

*   **Windows:** 개발 및 데스크톱 테스트용 운영체제
*   **WSL(Windows Subsystem for Linux):** 안드로이드 패키지 빌드를 위한 Linux 환경. (이 가이드에서는 Ubuntu 22.04 LTS 기준)
*   **Python:**
    *   Windows와 WSL 양쪽에 모두 **Python 3.10.x** 버전이 설치되어 있어야 합니다.
    *   > Ubuntu 22.04 LTS는 기본적으로 Python 3.10.12를 제공하므로 별도 설치가 필요하지 않을 수 있습니다.
*   **Poetry:** Python 의존성 관리를 위해 사용합니다.

---

## 1단계: Windows 개발 환경 설정 (데스크톱 테스트용)

이 단계에서는 Windows에 Kivy를 설치하여 데스크톱 환경에서 앱을 실행하고 테스트하는 방법을 설명합니다.

1.  **프로젝트 클론:**
    ```bash
    git clone https://github.com/sc7258/pydroid-hello.git
    cd pydroid-hello
    ```

2.  **Poetry 설치:**
    Windows에 Poetry가 설치되어 있지 않다면, 공식 문서를 참고하여 설치합니다.

3.  **프로젝트 의존성 설치:**
    프로젝트 최상위 폴더에서 터미널을 열고 다음을 실행합니다. 이 명령은 `pyproject.toml`에 명시된 Kivy와 같은 라이브러리를 설치합니다.
    ```bash
    poetry install --no-root
    ```

4.  **데스크톱에서 앱 실행:**
    다음 명령으로 Kivy 애플리케이션을 데스크톱 창으로 실행하여 테스트할 수 있습니다.
    ```bash
    poetry run python main.py
    ```

> **💡 팁:** `pyproject.toml` 파일에 새로운 의존성을 추가하는 등 변경사항이 생기면, `poetry lock && poetry install --no-root` 명령을 실행하여 `poetry.lock` 파일을 업데이트하고 의존성을 다시 설치해야 합니다.

---

## 2단계: 안드로이드 빌드 환경 설정 (WSL)

안드로이드 APK(앱 패키지)는 반드시 Linux 환경에서 빌드해야 합니다. 이를 위해 WSL을 사용합니다.

1.  **WSL 설치:**
    WSL이 설치되어 있지 않다면, PowerShell이나 명령 프롬프트를 관리자 권한으로 열고 다음을 실행합니다.
    ```bash
    wsl --install
    ```
    이 과정은 보통 최신 버전의 Ubuntu를 설치하며, 필요 시 컴퓨터를 재시작합니다.

2.  **WSL로 프로젝트 복사:**
    Windows 탐색기에서 전체 프로젝트 폴더(`pydroid-hello`)를 WSL의 홈 디렉터리(예: `~/pydroid-hello`)로 복사합니다.

    > **⚠️ 중요:** 프로젝트를 Windows 파일 시스템 경로(예: `/mnt/c/...`)에 두고 빌드하면, 긴 파일 경로 문제나 권한 문제로 인해 Buildozer가 실패할 수 있습니다. **반드시 프로젝트를 WSL의 내부 파일 시스템(예: `~` 또는 `~/projects`)으로 복사한 후 빌드를 진행해야 합니다.** 이렇게 하면 빌드 성능도 크게 향상됩니다.
    >
    > Windows 탐색기 주소창에 `\\wsl$`를 입력하면 WSL 파일 시스템에 쉽게 접근할 수 있습니다.

3.  **WSL(Ubuntu)에 빌드 도구 및 의존성 설치:**
    WSL 터미널을 열고, 복사한 프로젝트 디렉터리로 이동합니다. (예: `cd ~/pydroid-hello`)
    그런 다음, 아래 명령어를 순서대로 실행하여 빌드에 필요한 모든 도구를 설치합니다.

    ```bash
    # 1. 시스템 패키지 업데이트 및 필수 라이브러리 설치
    sudo apt update && sudo apt upgrade -y
    sudo apt install -y git zip unzip openjdk-17-jdk autoconf automake libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

    # 2. Poetry 설치 및 설정
    # 시스템에 apt로 설치된 구버전 poetry가 있다면 제거하여 충돌을 방지합니다.
    sudo apt-get remove -y poetry
    # 공식 스크립트로 최신 버전의 Poetry를 설치합니다.
    curl -sSL https://install.python-poetry.org | python3 -
    # Poetry 실행 경로를 셸 환경변수 PATH에 추가하고, 현재 세션에 즉시 적용합니다.
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
    export PATH="$HOME/.local/bin:$PATH"
    
    # 설치 확인 (경로: /home/user/.local/bin/poetry, 최신 버전 출력)
    which poetry
    poetry --version

    # 3. 프로젝트 의존성 설치 (buildozer 포함)
    # Windows에서 생성된 poetry.lock 파일을 사용하여 동일한 의존성을 설치합니다.
    poetry install --no-root
    ```
    > **⚠️ 주의:** Windows와 WSL 환경의 Python 버전(3.10.x)을 통일하는 것이 중요합니다. 버전이 다를 경우, `poetry.lock` 파일과의 비호환성으로 인해 의존성 관련 문제가 발생할 수 있습니다.

---

## 3단계: 안드로이드 APK 빌드

모든 설정이 완료되면, 아래 명령어를 실행하여 디버그용 APK를 빌드합니다.

> **참고:** Buildozer는 `buildozer.spec` 파일의 `requirements` 목록을 참조하여 APK에 필요한 패키지를 포함시킵니다. 이 목록은 `pyproject.toml`과는 별개로 관리됩니다.

```bash
poetry run buildozer android debug
```

최초 실행 시에는 안드로이드 SDK, NDK 등 필요한 구성 요소를 다운로드하므로 시간이 오래 걸릴 수 있습니다.

## 4단계: 앱 실행

빌드가 성공적으로 완료되면 `bin/` 디렉터리에서 APK 파일(예: `pydroid-hello-0.1.0-arm64-v8a_armeabi-v7a-debug.apk`)을 찾을 수 있습니다. 이 파일을 안드로이드 기기로 복사하여 설치하고 애플리케이션을 실행합니다.
