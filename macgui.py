import subprocess
import tkinter as tk
from getmac import get_mac_address
import socket
import requests
import platform

# -----------------------------------------------------------------------------------------------------
# 내컴퓨터 공인 IP 호출
def get_cpu_id():
    command = "wmic cpu get ProcessorId"
    cpu_id = subprocess.check_output(command, shell=True).decode().strip().split("\n")[1]
    return cpu_id

# -----------------------------------------------------------------------------------------------------
def get_isp(ip_address=None):
    if ip_address is None:
        ip_address = requests.get('https://api.ipify.org').text
    url = f'https://ipinfo.io/{ip_address}/json'
    response = requests.get(url)
    data = response.json()
    isp = data.get('org')
    return isp

# -----------------------------------------------------------------------------------------------------
def get_isp2(ip_address=None):
    if ip_address is None:
        ip_address = requests.get('https://api.ipify.org').text
    url = f'https://ipinfo.io/{ip_address}/json'
    response = requests.get(url)
    data = response.json()
    isp2 = data.get('timezone')
    return isp2

# -----------------------------------------------------------------------------------------------------
# 물리적 주소 호출
mac_address = get_mac_address()
# 공인아이피 v4 주소
response = requests.get('https://api.ipify.org')
ipout_address = response.text
# 컴퓨터 이름
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
# 윈도우 버전 추출
os_name = platform.system()
os_version = platform.version()
os_release = platform.release()
architecture = platform.architecture()
processor = platform.processor()

# -----------------------------------------------------------------------------------------------------
# 작업 관리자 실행 함수 (PowerShell을 사용해 관리자 권한 요청)
def open_taskmgr():
    try:
        # PowerShell을 통해 관리자 권한으로 taskmgr 실행
        subprocess.run(["powershell", "Start-Process", "taskmgr", "-Verb", "runAs"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# -----------------------------------------------------------------------------------------------------
# GUI를 위한 Tkinter 설정
def display_info():
    root = tk.Tk()
    root.title("푸름정보기술")
    root.geometry("500x470")

    # 라벨들을 생성하여 정보를 표시
    tk.Label(root, text=f"MAC 주소: {mac_address}").pack(pady=5)
    tk.Label(root, text=f"호스트명: {hostname}").pack(pady=5)
    tk.Label(root, text=f"아이피 v4주소: {ip_address}").pack(pady=5)
    tk.Label(root, text=f"공인아이피 v4주소: {ipout_address}").pack(pady=5)
    tk.Label(root, text=f"CPU ID: {get_cpu_id()}").pack(pady=5)
    tk.Label(root, text=f"ISP 회사: {get_isp()}").pack(pady=5)
    tk.Label(root, text=f"ISP 국가: {get_isp2()}").pack(pady=5)
    tk.Label(root, text="--------------------------------------").pack(pady=5)
    tk.Label(root, text=f"OS Name: {os_name}").pack(pady=5)
    tk.Label(root, text=f"OS Version: {os_version}").pack(pady=5)
    tk.Label(root, text=f"OS Release: {os_release}").pack(pady=5)
    tk.Label(root, text=f"Architecture: {architecture}").pack(pady=5)
    tk.Label(root, text=f"Processor: {processor}").pack(pady=5)

    # "작업 관리자" 버튼
    tk.Button(root, text="작업 관리자", command=open_taskmgr).pack(pady=20)

    # GUI 루프 시작
    root.mainloop()

# -----------------------------------------------------------------------------------------------------
# GUI 표시
display_info()
