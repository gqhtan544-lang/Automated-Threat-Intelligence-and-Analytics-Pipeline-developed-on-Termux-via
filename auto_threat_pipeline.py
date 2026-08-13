import pandas as pd
import random
from datetime import datetime, timedelta

print("[-] بدء تشغيل منظومة معالجة وإدارة البيانات الأمنية...")

# 1. توليد بيانات سجلات هجمات سيبرانية لمحاكاة الواقع (SOC Log Generator)
attack_types = ['DDoS Attempt', 'Telnet Scan', 'Web Exploit', 'Botnet Activity', 'Malware Injection', 'SSH Scan', 'Phishing Host', 'Brute Force Attack']
countries = ['United States', 'India', 'United Kingdom', 'Russia', 'Netherlands', 'Germany', 'Brazil', 'China']
ips = ['104.244.42.1', '210.212.5.4', '82.102.23.8', '45.142.12.9', '194.26.29.3', '185.220.101.5', '177.47.11.2', '222.186.31.6']

simulated_logs = []
base_time = datetime.now()

# توليد 50 سجل هجوم مطابق تماماً لتصميم الـ Dashboard الخاصة بك
for i in range(50):
    log_time = base_time - timedelta(minutes=random.randint(1, 1440))
    attack = random.choice(attack_types)
    country = random.choice(countries)
    ip = random.choice(ips)
    record_count = random.randint(1, 10)
    
    simulated_logs.append({
        'Timestamp': log_time.strftime('%Y-%m-%d %H:%M:%S'),
        'Attack_IP_IOC': ip,
        'Target_Country': country,
        'Threat_Type': attack,
        'Record_Count': record_count
    })

# 2. إدارة البيانات وتحليلها باستخدام Pandas (Data Engineering & Analytics)
df = pd.DataFrame(simulated_logs)

# فرز البيانات حسب الوقت
df = df.sort_values(by='Timestamp', ascending=False)

print(f"\n[+] تم معالجة وتحليل {len(df)} سجل تهديد سيبراني بنجاح!")
print("\n[!] أعلى 3 أنواع هجمات تم رصدها وتحليلها إحصائياً:")
print(df['Threat_Type'].value_counts().head(3))

# 3. تصدير البيانات إلى ملف CSV متوافق مع Looker Studio
df.to_csv("cyber_threats_analytics.csv", index=False)
print("\n[+] تم حفظ ملف البيانات النهائي بنجاح: cyber_threats_analytics.csv")
