from flask import Flask, render_template
import socket
import os

app = Flask(__name__)

def get_pod_ip():
    """
    Pod IP 주소를 가져옵니다.
    환경 변수 'MY_POD_IP'를 사용하여 IP 주소를 가져옵니다.
    환경 변수가 설정되어 있지 않으면 None을 반환합니다.
    """
    return os.environ.get('MY_POD_IP')

@app.route('/')
def index():
    """
    기본 경로('/')에 대한 뷰 함수입니다.
    호스트 이름, 호스트 IP 주소, Pod IP 주소를 가져와서 템플릿에 전달합니다.
    """
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    pod_ip = get_pod_ip()  # Pod IP 주소를 가져옵니다.

    return render_template('index.html', host_name=host_name, host_ip=host_ip, pod_ip=pod_ip)

if __name__ == "__main__":
    # 가능한 경우, 프로덕션 환경을 위해 Gunicorn과 같은 WSGI 서버를 사용하세요.
    # app.run(host="0.0.0.0", port=5000, debug=True)  # 개발 환경에서 실행하는 경우
    app.run(host="0.0.0.0", port=5000)

