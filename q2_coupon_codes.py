student_id = input("請輸入完整學號：").strip().upper()
tail = student_id[-3:]

def collect_codes(raw_codes, saved=None):
    if saved is None:
        result = []
    else:
        result = saved.copy()

    for code in raw_codes:
        code = code.strip().upper()
        if code and code not in result:
            result.append(code)

    return result

saved = ["BASE"]
raw_a = [" welcome" + tail + " ", "vip" + tail, "",
         "WELCOME" + tail, "   "]
raw_b = [" new" + tail + " ", " welcome" + tail + " "]

activity_a = collect_codes(raw_a, saved=saved)
activity_b = collect_codes(raw_b)

print("學號：", student_id)
print("活動A：", activity_a)
print("活動B：", activity_b)
print("原始saved：", saved)
print("原始raw_a：", raw_a)
print("空資料：", collect_codes([]))
