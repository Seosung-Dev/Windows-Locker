# Windows-Locker

# 주의!!
## 이 프로그램은 개발중이며, 이 프로그램으로 인한 피해는 개발자가 보상하지 않습니다.
## 이 프로그램을 clone 또는 fork, 다운로드하는 행위는 위의 경고와 약관을 읽고 동의한 것으로 간주합니다

## 설치 방법

```
pip install python-dotenv screeninfo
```

---

## 환경 설정

1. `.env.example` 파일을 `.env`로 복사하세요.

Windows:
```
copy .env.example .env
```

Linux / Mac:
```
cp .env.example .env
```

2. `.env` 파일을 열고 값을 설정하세요.

```
ID=your_id
PASSWORD=your_password
```

3. `.env` 파일은 보안을 위해 Git에서 제외됩니다.

### TMI : 이 프로그램은 이 인간이 서버돌릴때 부모님이 컴퓨터를 못 보게하기 위해 제작됨