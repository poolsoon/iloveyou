from getmac import get_mac_address
import socket
import requests
import subprocess # CPU ID 추출 모듈
import tkinter as tkinter # mac_address 추출 모듈
import platform # 윈도우 버전 추출
# -----------------------------------------------------------------------------------------------------
    # 내컴퓨터 공인 IP 호출
def get_cpu_id():
    command = "wmic cpu get ProcessorId"
    cpu_id = subprocess.check_output(command, shell=True).decode().strip().split("\n")[1]
    return cpu_id
# -----------------------------------------------------------------------------------------------------
def get_isp(ip_address=None):
    # 내컴퓨터 공인 IP 호출
    if ip_address is None:
        ip_address = requests.get('https://api.ipify.org').text
            
    # 아이피 정보 가입회사 호출 
    url = f'https://ipinfo.io/{ip_address}/json'
    response = requests.get(url)
    
    # JSON 에서 호출 data 적용
    data = response.json()
    isp = data.get('org')

    return isp

isp = get_isp()

# IP 사용국가--------------------------------------------------------------------------------------------

def get_isp2(ip_address=None):
    # IP 주소가 없으면, 자신의 공인 IP 주소로 조회
    if ip_address is None:
        ip_address = requests.get('https://api.ipify.org').text
        
    # ipinfo.io API 호출
    url = f'https://ipinfo.io/{ip_address}/json'
    response = requests.get(url)
    
    # JSON 응답에서 ISP 정보 추출
    data = response.json()
    isp2 = data.get('timezone')
    
    return isp2

isp2 = get_isp2()
# 물리적 주소 호출---------------------------------------------------------------------------------------
mac_address = get_mac_address()
# 공인아이피 v4 주소-------------------------------------------------------------------------------------
response = requests.get('https://api.ipify.org') # 'https://ipinfo.io/json' 
ipout_address = response.text
# 컴퓨터 이름--------------------------------------------------------------------------------------------
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
# 윈도우 버전 추출---------------------------------------------------------------------------------------
os_name = platform.system()
os_version = platform.version()
os_release = platform.release()
architecture = platform.architecture()
processor = platform.processor()

print()
print("--------------------------------------")
print(f"MAC 주소: {mac_address}")
print(f"호스트명: {hostname}")
print(f"아이피 v4주소: {ip_address}")
print(f"공인아이피 v4주소: {ipout_address}")
print("CPU ID :", get_cpu_id())
print(f"ISP 회사: {isp}")
print(f"ISP 국가: {isp2}")
print("--------------------------------------")
print(f"OS Name: {os_name}")
print(f"OS Version: {os_version}")
print(f"OS Release: {os_release}")
print(f"Architecture: {architecture}")
print(f"Processor: {processor}")
print("======================================")
print()


