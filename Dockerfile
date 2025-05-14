FROM ubuntu:22.04

# 현재 디렉토리의 모든 파일들을 컨테이너의 /app 디렉토리에 복사한다.
COPY . /app

# flask의 작업 위치가 /app이라는 뜻
WORKDIR /app

RUN apt update && apt install python3 pip --yes && pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "/app/app.py"]
