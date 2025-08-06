# WSL 빌드 환경 설정

이 문서는 WSL(Windows Subsystem for Linux) 환경에서 pydroid-hello 애플리케이션의 빌드 환경을 설정하는 방법을 설명한다.

## 1. WSL 설치

- Windows PowerShell 또는 명령 프롬프트를 관리자 권한으로 실행한다.
- `wsl --install` 명령어를 실행하여 WSL과 기본 Ubuntu 배포판을 설치한다.
- 설치 후 시스템을 재시작한다.

## 2. 필수 패키지 설치

- WSL(Ubuntu) 터미널을 연다.
- 다음 명령어를 실행하여 빌드에 필요한 기본 패키지를 설치한다.
  ```bash
  sudo apt update && sudo apt upgrade -y
  sudo apt install -y git zip unzip openjdk-17-jdk autoconf automake libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
  ```

## 3. Python 및 Poetry 설치

- 프로젝트는 Python 3.13 이상을 사용한다. `pyenv`를 사용하여 특정 Python 버전을 설치하는 것을 권장한다.
  ```bash
  curl https://pyenv.run | bash
  # .bashrc 에 pyenv 설정 추가
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo 'eval "$(pyenv init -)"' >> ~/.bashrc
  exec "$SHELL"
  
  pyenv install 3.13.0
  pyenv global 3.13.0
  ```
- Poetry를 설치한다.
  ```bash
  curl -sSL https://install.python-poetry.org | python3 -
  # .bashrc 에 poetry 경로 추가
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
  exec "$SHELL"
  ```

## 4. 프로젝트 설정 및 의존성 설치

- Git을 사용하여 프로젝트를 클론한다.
  ```bash
  git clone https://github.com/sc7258/pydroid-hello.git
  cd pydroid-hello
  ```
- Poetry를 사용하여 프로젝트 의존성을 설치한다.
  ```bash
  poetry install --no-root
  ```

## 5. Buildozer 설치 및 실행

- Buildozer는 `pyproject.toml`에 개발 의존성으로 추가하거나 전역으로 설치할 수 있다. 여기서는 Poetry를 통해 가상 환경 내에 설치한다.
  ```bash
  poetry add buildozer --group dev
  ```
- Buildozer를 사용하여 안드로이드 디버그 빌드를 실행한다.
  - 최초 실행 시 Android SDK 및 NDK 등 필요한 구성 요소를 다운로드하므로 시간이 오래 걸릴 수 있다.
  ```bash
  poetry run buildozer android debug
  ```
- 빌드가 성공하면 `bin` 디렉터리에 `pydroid-hello-0.1.0-arm64-v8a_armeabi-v7a-debug.apk` 파일이 생성된다.

## 주의 사항

- **빌드 오류 방지를 위한 프로젝트 위치 (중요):** Buildozer와 같은 안드로이드 빌드 도구는 긴 Windows 경로 (`/mnt/c/...`)를 제대로 처리하지 못해 빌드에 실패할 수 있다. **반드시 프로젝트 전체를 WSL 파일 시스템(예: `~/projects`)으로 복사하거나 이동한 후 빌드를 진행해야 한다.**
- **파일 경로:** WSL과 Windows 간의 파일 경로 변환에 주의해야 한다. WSL 내에서는 Linux 스타일의 경로(`/mnt/c/...`)를 사용한다.
- **권한 문제:** Windows 파일 시스템(`ntfs`)에서 작업할 때 파일 권한 문제가 발생할 수 있다. `git config --global core.fileMode false` 설정을 권장한다.
- **네트워크:** WSL2는 가상 네트워크를 사용하므로, `localhost` 접근 시 IP 주소를 확인해야 할 수 있다.
- **성능:** 소스 코드를 Windows 파일 시스템(예: `/mnt/c`)에 두는 것보다 WSL 파일 시스템(예: `~/projects`)에 두는 것이 I/O 성능 면에서 훨씬 유리하다.
