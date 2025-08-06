# 개발 과정 요약 (HOW-TO)

이 문서는 `pydroid-hello` 프로젝트를 개발하면서 수행한 작업 절차와 문제 해결 과정을 요약한다.

## 1. 초기 요구사항 분석

*   **사용자 요구사항:** `poetry`와 `android`를 이용하여 "Hello, World!"를 출력하는 프로그램 제작.
*   **초기 접근 방식:** Python으로 안드로이드 앱을 만들기 위한 두 가지 주요 기술 스택을 고려한다.
    1.  **Toga (BeeWare) + Briefcase:** 네이티브 위젯을 사용하여 플랫폼별 고유 디자인을 따르는 앱 제작 방식.
    2.  **Kivy + Buildozer:** 자체 렌더링 엔진을 사용하여 모든 플랫폼에서 동일한 디자인을 제공하는 앱 제작 방식.

## 2. Toga를 이용한 1차 시도 및 문제 발생

1.  `poetry init` 명령으로 `pyproject.toml` 파일을 생성한다.
2.  `poetry add toga` 명령으로 GUI 라이브러리인 Toga 설치를 시도한다.
3.  **문제 발생:** Toga의 의존성인 `pythonnet`이 당시 설정된 Python 3.13 버전과 호환되지 않아 설치에 실패한다.
4.  **해결 시도:** `pyproject.toml` 파일의 `requires-python` 설정을 `pythonnet`이 지원하는 `"<3.13"`으로 낮춘다.
5.  **추가 문제 발생:** 프로젝트의 Python 버전 제약과 현재 시스템에 설치된 Python 3.13 버전이 맞지 않아 `poetry`가 작업을 거부한다. `poetry env use`를 통해 Python 버전을 전환하려 했으나, 시스템에서 해당 버전(e.g., 3.12)을 찾지 못해 실패한다.

## 3. Kivy + Buildozer로 방향 전환

사용자가 Kivy와 Buildozer 조합에 대해 문의하여, 해당 방식으로 구현 방향을 전환하기로 결정한다. 이 조합은 Toga와 달리 자체 렌더링 엔진을 사용하며, 특히 `buildozer`는 Linux 환경에서의 빌드를 표준으로 한다.

1.  **Python 버전 복원:** `pyproject.toml`의 Python 버전 제약을 원래대로(`>=3.13`) 되돌린다.
2.  `poetry add kivy buildozer` 명령으로 Kivy와 Buildozer 설치를 시도한다.
3.  **문제 발생:** Buildozer의 의존성인 `sh` 패키지가 Windows에서 지원되지 않는 `fcntl` 모듈을 필요로 하여 설치에 실패한다.
4.  **해결 방안:**
    *   Windows 환경에서는 Kivy 앱 코드 작성 및 데스크톱 테스트만 진행하기로 결정한다.
    *   안드로이드 APK 빌드는 **WSL(Windows Subsystem for Linux)** 환경에서 `buildozer`를 사용하여 진행하는 것으로 계획을 수정한다.

## 4. 최종 구현 단계

1.  **Kivy 설치:** `poetry add kivy` 명령으로 Windows에 Kivy 라이브러리만 성공적으로 설치한다.
2.  **애플리케이션 코드 작성:** "Hello, World!"를 표시하는 간단한 Kivy 앱 코드를 `main.py` 파일로 작성한다.
3.  **Buildozer 설정 파일 생성:** `buildozer`가 Linux 환경에서 앱을 빌드할 때 참조할 `buildozer.spec` 파일을 수동으로 생성한다. 이 파일에는 앱 이름, 버전, 요구사항 등의 메타데이터를 포함시킨다.
4.  **문서화:**
    *   프로젝트의 전체적인 설정 및 빌드 방법을 `README.md` 파일에 국문으로 상세히 작성한다.
    *   본 `HOWTO.md` 파일을 작성하여 개발 과정 전체를 기록한다.

## 결론

최종적으로 Windows에서는 Poetry를 사용하여 Kivy 코드 개발 및 테스트 환경을 구성하고, 실제 안드로이드 앱 패키징은 WSL(Linux) 환경에서 Buildozer를 통해 수행하는 하이브리드 워크플로우를 구축한다. 이는 Python으로 크로스플랫폼 모바일 앱을 개발할 때 발생하는 OS 종속성 문제를 해결하는 표준적인 접근 방식이다.