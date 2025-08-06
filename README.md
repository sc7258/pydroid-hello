# Pydroid 안녕 (Pydroid Hello)

이 프로젝트는 Python, [Kivy](https://kivy.org/), [Buildozer](https://github.com/kivy/buildozer)를 사용하여 "Hello, World!"를 출력하는 간단한 안드로이드 모바일 애플리케이션입니다.

Windows 환경에서 Kivy를 이용해 데스크톱 애플리케이션을 개발 및 테스트하고, WSL(Windows Subsystem for Linux) 환경에서 Buildozer를 사용해 안드로이드 APK로 패키징하는 표준적인 개발 워크플로우를 보여줍니다.

## 기술 스택 (Technology Stack)

*   **언어 (Language):** Python 3.10
*   **GUI 프레임워크 (GUI Framework):** Kivy
*   **빌드 도구 (Build Tool):** Buildozer
*   **의존성 관리 (Dependency Management):** Poetry

## 주요 기능 (Features)

*   Poetry를 사용한 Python 프로젝트 의존성 관리
*   Kivy를 사용한 크로스플랫폼 GUI 애플리케이션 작성
*   Buildozer를 이용한 안드로이드 APK 빌드 자동화
*   Windows(개발)와 WSL(빌드)을 연동하는 하이브리드 개발 환경 구성

## 사용 방법 (How to Use)

전체 개발 환경 설정 및 빌드 과정에 대한 자세한 설명은 **docs/BUILD.md** 문서를 참고하세요.

### 1. 데스크톱에서 앱 테스트 (Windows)

안드로이드용으로 빌드하기 전에, Windows 개발 환경에서 Kivy 애플리케이션을 데스크톱 버전으로 실행하고 테스트할 수 있습니다.

```bash
# 의존성 설치
poetry install --no-root

# 데스크톱 앱 실행
poetry run python main.py
```

### 2. 안드로이드 앱 빌드 (WSL)

안드로이드 APK 패키징은 Linux 환경에서 Buildozer를 통해 수행됩니다.

```bash
# (WSL 환경에서)
# 자세한 환경 설정은 docs/BUILD.md 참고
poetry run buildozer android debug
```

빌드가 완료되면 `bin/` 디렉터리에서 생성된 APK 파일을 확인할 수 있습니다.
