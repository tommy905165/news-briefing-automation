#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

def send_email(to_email, subject, body):
    """Gmail을 통해 이메일 발송"""
    sender = "hjkim1203@gmail.com"
    gmail_token = os.environ.get('GMAIL_TOKEN')
    
    if not gmail_token:
        print("❌ GMAIL_TOKEN 환경변수가 설정되지 않았습니다")
        return False
    
    try:
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = to_email
        message['Subject'] = subject
        
        message.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # Gmail SMTP 서버로 이메일 발송
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, gmail_token)
            server.send_message(message)
        
        print(f"✅ 이메일 발송 완료: {to_email}")
        return True
        
    except Exception as e:
        print(f"❌ 이메일 발송 실패: {str(e)}")
        return False

def main():
    """메인 함수"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 이메일 제목
    subject = f"[{today}] AI 칩 공급망 브리핑"
    
    # 이메일 본문 (나중에 뉴스 API와 연결 가능)
    body = """■ NVIDIA

📊 주요 뉴스:
1. Vera Rubin Q3/H2 2026 출시 - 288GB HBM4
2. B300 (Blackwell Ultra) 288GB 메모리 탑재 완료

■ Huawei Ascend

📊 주요 뉴스:
1. Ascend 950DT 최대 8,192개 NPU 연결 - MWC 2026 공개

■ AMD

📊 주요 뉴스:
1. MI350X 288GB HBM3e - Blackwell B300 대비 60% 증가

---
출처: 자동화 브리핑 시스템
"""
    
    # 이메일 발송
    to_email = os.environ.get('EMAIL_TO', 'hjkim@aimtog.co.kr')
    send_email(to_email, subject, body)

if __name__ == "__main__":
    main()
