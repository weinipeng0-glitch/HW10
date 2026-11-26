student_id = input("請輸入完整學號：").strip().upper()
tail = student_id[-3:]
a = int(student_id[-3])
b = int(student_id[-2])
c = int(student_id[-1])
s = a + b + c

def ad_report(impressions, clicks, target=3.0):
    if impressions == 0:
        return None, False
    ctr = clicks / impressions * 100
    return ctr, ctr >= target

ads = [
    ("搜尋廣告", 1000 + 100 * a, 30 + 5 * b),
    ("社群廣告", 1200 + 100 * b, 24 + 4 * c),
    ("影音廣告", 0, 0)
]

target = 2.5 + 0.1 * c
count = 0

print(f"學號：{student_id}")
print(f"CTR門檻：{target:.2f}%")

for name, impressions, clicks in ads:
    ctr, passed = ad_report(impressions, clicks, target=target)

    if ctr is None:
        ctr_text = "無曝光資料"
    else:
        ctr_text = f"{ctr:.2f}%"

    if passed:
        count += 1

    print(f"{name}：曝光={impressions}，點擊={clicks}，CTR={ctr_text}，達標={passed}")

print(f"達標廣告數：{count}")
print("預設門檻測試：", ad_report(1000, 30))
print("零點擊測試：", ad_report(1000, 0))
