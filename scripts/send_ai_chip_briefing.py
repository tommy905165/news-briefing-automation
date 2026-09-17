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
    gmail_password = os.environ.get('GMAIL_TOKEN')
    
    if not gmail_password:
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
            server.login(sender, gmail_password)
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
    
    # 이메일 본문
    body = """■ NVIDIA

📊 주요 뉴스:
1. Vera Rubin Q3/H2 2026 출시 - 288GB HBM4, 5배 인퍼런스 성능
2. B300 (Blackwell Ultra) 288GB HBM3e - 50% 성능 향상
3. B200 세계 반도체 업계 표준화 - 주요 클라우드 모두 채택

💡 시장 분석:
Nvidia는 Vera Rubin으로 3.5배 훈련 성능과 10배 추론 토큰 원가 절감을 약속.
2026년 AI칩 시장의 70% 이상 점유율 유지 전망.


■ Huawei Ascend

📊 주요 뉴스:
1. Ascend 950DT Atlas 950 SuperPoD 최대 8,192개 NPU 연결 - MWC 2026 공개
2. DeepSeek V4에서 Ascend NPU 채택 - NVIDIA GPU와 병렬 사용 중
3. 2026년 생산 목표 약 1.6백만 개 칩 - Ascend 950 시리즈 600만 개 예상

💡 시장 분석:
화웨이 Ascend는 국내 중국 시장 독점에서 벗어나 국제 협력 강화 중.
DeepSeek 채택으로 신뢰성 입증, 향후 한국 시장 진출 가능성 높음.


■ AMD MI 시리즈

📊 주요 뉴스:
1. MI350X/MI355X 288GB HBM3e (Blackwell B300 180GB 대비 60% 증가) - 2025년 Q4 출시
2. MI350 Llama 3.1 405B에서 MI300X 대비 4배 성능 향상 - Advancing AI 2026 발표
3. MI400 2026년 출시 - CDNA 5 아키텍처, 7.2조 원 첫해 매출 전망

💡 시장 분석:
AMD는 메모리 용량 우위로 대규모 언어모델 운영에서 경쟁력 강화.
Microsoft Azure, Oracle 전략 파트너십으로 NVIDIA 점유율 12-20% 목표.


■ 반도체 공급망 동향

📊 주요 뉴스:
1. 2026년 전체 반도체 시장 1조 달러 규모 - AI 인프라 투자로 3년 연속 고성장
2. HBM 메모리 공급 2026년 완전 매진 - Micron 용량 부족 심화
3. ABF 기판이 새로운 병목 - 고대역폭 메모리 패키징 수요 폭증

💡 시장 분석:
TSMC 대만 집중도 90% 이상 (3nm 이하 칩). 미국 인플레이션 감축법(IRA) 영향으로
2026년 미국, 한국 생산 다원화 진행 중. 지정학적 리스크 증가로 국내 AI칩 공급망
다각화 전략 필수.

---
자동화 브리핑 시스템
발송 시간: {today} 09:40 KST
"""
    
    # 이메일 발송
    to_email = os.environ.get('EMAIL_TO', 'hjkim@aimtog.co.kr')
    send_email(to_email, subject, body)

if __name__ == "__main__":
    main()
