import pandas as pd
import random
from datetime import datetime, timedelta
import requests
import time
import os                 # مكتبة التعامل مع نظام التشغيل
from dotenv import load_dotenv  # مكتبة قراءة ملفات البيئة

# تحميل الرمز السري من ملف .env المخفي
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def send_security_alert(attack_type, country, ip, record_count):
    message = (
        f"🚨 **ATTACK DETECTED** 🚨\n"
        f"🖥️ **System:** GenAI Firewall\n"
        f"🔥 **Attack Type:** {attack_type}\n"
        f"🎯 **Target Country:** {country}\n"
        f"🌐 **Attacker IP:** {ip}\n"
        f"📊 **Record Count:** {record_count}\n"
        f"✅ **Action:** Alert logged successfully."
    )
    
    url = f"https://telegram.org{BOT_TOKEN}/sendMessage"
    
    payload = {
        "chat_id": "6625925902",
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Network error: {e}")

print("🤖 جاري إنشاء وتوليد بيانات الأمن السيبراني للذكاء الاصطناعي...")

# البيانات المحاكاة لمراقبة أنظمة الذكاء الاصطناعي
attack_types = ['DDoS Attempt', 'Telnet Scan', 'Web Exploit', 'Botnet Activity', 'Malware Injection', 'SSH Scan', 'Phishing Host', 'Brute Force Attack']
countries = ['United States', 'India', 'United Kingdom', 'Russia', 'Netherlands', 'Germany', 'Brazil', 'China']
ips = ['104.244.42.1', '210.212.3.4', '82.102.23.0', '43.142.12.9', '194.26.29.5', '103.220.101.5', '177.47.11.2', '222.101.45.6']

simulated_logs = []
base_time = datetime.now()

# حلقة التكرار لتوليد 30 سجل هجوم وإرسالها للتليجرام
for i in range(30):
    log_time = base_time - timedelta(minutes=random.randint(1, 1440))
    attack = random.choice(attack_types)
    country = random.choice(countries)
    ip = random.choice(ips)
    record_count = random.randint(1, 10)
    
    # إرسال التنبيه الفوري
    send_security_alert(attack, country, ip, record_count)
    time.sleep(1) # تأخير بسيط لعدم حظر السيرفر
    
    simulated_logs.append({
        "Timestamp": log_time.strftime("%Y-%m-%d %H:%M:%S"),
        "Attacker_IP": ip,
        "Target_Country": country,
        "Threat_Type": attack,
        "Record_Count": record_count
    })

# بناء واستخراج وإدارة البيانات الكبيرة باستخدام مكتبة Pandas
df = pd.DataFrame(simulated_logs)
df = df.sort_values(by='Timestamp', ascending=False)

print(f"✔️ تم معالجة وتحليل ({len(df)}) سجل تهديد سيبراني بنجاح")
df.to_csv("cyber_threats_analytics.csv", index=False)
print("💾 تم حفظ ملف البيانات النهائي بنجاح باسم 'cyber_threats_analytics.csv'")
