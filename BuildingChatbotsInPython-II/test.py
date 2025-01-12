import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3

def assistant(response):
    
    print(response)  # สามารถเปลี่ยนเป็นการพูดด้วยเสียงได้หากต้องการ
    assistantvoice(response)

def assistantvoice(audio): 
    engine = pyttsx3.init()
    # getter: To get the current
    # engine property value

    # setter method
    # [0] for male voice
    # [1] for female voice
    TH_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_THAI"
    engine.setProperty('voice', TH_voice_id)
    # Method governing assistant's speech
    engine.say(audio)
    # Blocks/processes queued commands
    engine.runAndWait()

def audioinput():
    aud = sr.Recognizer()
    with sr.Microphone() as source:
        print('กำลังฟังและประมวลผล...')
        aud.pause_threshold = 0.7
        audio = aud.listen(source)
        
        try:
            print("กำลังเข้าใจ...")
            phrase = aud.recognize_google(audio, language='th-TH')  # เปลี่ยนเป็นภาษาไทย
            print("คุณพูดว่า: ", phrase)
        except Exception as exp:
            print(exp)
            print("ช่วยพูดอีกครั้งได้ไหม")
            return "None"
    
    return phrase

def theDay():
    # ฟังก์ชันนี้ใช้เพื่อบอกวันปัจจุบัน
    day = datetime.datetime.today().weekday() + 1  # 0 = จันทร์, 6 = อาทิตย์
    Day_dict = {
        1: 'จันทร์', 
        2: 'อังคาร',
        3: 'พุธ', 
        4: 'พฤหัสบดี',
        5: 'ศุกร์', 
        6: 'เสาร์',
        7: 'อาทิตย์'
    }
    
    if day in Day_dict.keys():
        weekday = Day_dict[day]
        print(weekday)
        assistant("วันนี้คือ " + weekday)

def theTime():
    # ฟังก์ชันนี้ใช้เพื่อบอกเวลา
    time = str(datetime.datetime.now())
    hour = time[11:13]
    min = time[14:16]
    assistant("ตอนนี้เวลา " + hour + " ชั่วโมง " + min + " นาที")

# ลูปหลักสำหรับผู้ช่วยเสมือน
while True:
    # เปลี่ยนข้อความเป็นตัวพิมพ์เล็กเพื่อให้ทำงานได้ดีขึ้น
    phrase = audioinput().lower()

    if "คุณชื่ออะไร" in phrase:
        assistant("ฉันคือผู้ช่วยเสมือนที่ไม่มีชื่อ")
        continue

    # เงื่อนไขสำหรับออกจากโปรแกรม
    elif "ลาก่อน" in phrase:
        assistant("ออกจากระบบแล้ว ขอให้คุณมีวันที่ดี!")
        break

    elif "วันนี้วันอะไร" in phrase:
        theDay()
        continue

    elif "ตอนนี้เวลาอะไร" in phrase:
        theTime()
        continue
    
    elif "วิกิ" in phrase:
        # เพื่อดึงข้อมูลจากวิกิพีเดีย
        assistant("กำลังตรวจสอบวิกิพีเดีย...")
        phrase = phrase.replace("วิกิ ", "")
        # จะจำกัดสรุปเป็นสี่บรรทัด
        result = wikipedia.summary(phrase, sentences=4)
        assistant("ตามที่วิกิพีเดียกล่าวว่า")
        assistant(result)
        continue
