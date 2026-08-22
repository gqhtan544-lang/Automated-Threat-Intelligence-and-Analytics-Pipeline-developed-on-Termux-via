import pandas as pd
import random
from datetime import datetime, timedelta
import requests
import time

def send_security_alert(attack_type, country, ip, record_count):
    message = (
        f"🚨 ATTACK DETECTED! 🚨\n\n"
        f"🛡️ System: GenAI Firewall\n"
        f"🕵️‍♂️ Attack Type: {attack_type}\n"
        f"🌍 Target Country: {country}\n"
        f"🌐 Attacker IP: {ip}\n"
        f"📊 Record Count: {record_count}\n"
        f"📝 Action: Alert logged successfully."
    )
    
    # استبدل النص أدناه بـ Token البوت الخاص بك المستخرج من BotFather
    BOT_TOKEN = "7950505193:AAEyOonw9F8E4z7yD4VfP5uV4W-xyz" 
    url = f"https://telegram.org{BOT_TOKEN}/sendMessage"
    
    payload = {
        "chat_id": "862592502", 
        "text": message
    }
    
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Network error: {e}")

print("... يتم تشغيل منظومة معالجة وزارة البيانات الأمنية لـ AI ...")

# بيانات محاكاة لهجمات سيبرانية لمراقبة أنظمة الـ AI
attack_types = ['DDoS Attempt', 'Telnet Scan', 'Web Exploit', 'Botnet Activity', 'Malware Injection', 'SSH Scan', 'Phishing Host', 'Brute Force Attack', 'Normal']
countries = ['United States', 'India', 'United Kingdom', 'Russia', 'Netherlands', 'Germany', 'Brazil', 'China']
ips = ['104.244.42.1', '210.212.5.4', '82.102.23.8', '45.142.12.9', '194.26.29.3', '185.220.101.5', '177.47.11.2', '222.186.30.2']

simulated_logs = []
base_time = datetime.now()

# حلقة التكرار لتوليد 30 سجل هجوم مطابق تماماً لتصميم الـ Dashboard
for i in range(30):
    log_time = base_time - timedelta(minutes=random.randint(1, 1440))
    attack = random.choice(attack_types)
    country = random.choice(countries)
    ip = random.choice(ips)
    record_count = random.randint(1, 10)
    
    # إرسال التنبيه الفوري إلى تليجرام
    send_security_alert(attack, country, ip, record_count)
    time.sleep(1)
    
    simulated_logs.append({
        "Timestamp": log_time.strftime('%Y-%m-%d %H:%M:%S'),
        "Attack_IP_IOC": ip,
        "Target_Country": country,
        "Threat_Type": attack,
        "Record_Count": record_count
    })

# إدارة البيانات وتحليلها باستخدام مكتبة Pandas (Data Engineering & Analytics)
df = pd.DataFrame(simulated_logs)

# فرز البيانات حسب الوقت
df = df.sort_values(by='Timestamp', ascending=False)

print(f"\n[+] تم معالجة وتحليل ({len(df)}) سجل تهديد سيبراني بنجاح :)")
print(" أعلى 3 أنواع هجمات تم رصدها وتحليلها إحصائياً [!] ")
print(df['Threat_Type'].value_counts().head(3))

# تصدير ملف CSV متوافق مع Looker Studio
df.to_csv("cyber_threats_analytics.csv", index=False)
print("\n[✔] تم حفظ ملف البيانات النهائي بنجاح باسم: cyber_threats_analytics.csv")
