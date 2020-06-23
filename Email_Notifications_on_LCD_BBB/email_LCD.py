import easyimap
import time
import Adafruit_CharLCD as LCD
import Adafruit_BBIO.GPIO as GPIO

login = 'sagarp3199@gmail.com'
password = '399ansimla2603'

lcd_rs = 'P8_8'
lcd_en = 'P8_10'
lcd_d4 = 'P8_18'
lcd_d5 = 'P8_16'
lcd_d6 = 'P8_14'
lcd_d7 = 'P8_12'
lcd_backlight = 'P8_7'
led='P9_16'

LCD_COLUMNS = 16
LCD_ROWS = 4

GPIO.setup(led,GPIO.OUT)

lcd = LCD.Adafruit_CharLCD(lcd_rs,lcd_en,lcd_d4,lcd_d5,lcd_d6,lcd_d7,LCD_COLUMNS,LCD_ROWS,lcd_backlight)

imapper = easyimap.connect('imap.gmail.com', login, password)
delay=20
body_email={}
extra=['"',"'",'!',"~","@",'#','$','%','^','&','*','`','{','}','[',']','\'','|','<','>',':',';']
while True:
    lcd.clear()

    for mail_id in imapper.listids(limit=5):
        mail = imapper.mail(mail_id)
        print("Sender: "+mail.from_addr)
        ss=mail.from_addr
        f=''
        GPIO.output(led,GPIO.HIGH)
        for i in ss:
            if i=='<':
                break
            if i in extra:
                continue
            f+=i
        lcd.message(f)
        lcd.message('\n')
        bb=mail.title
        count=0
        tt=''
        for i in bb:
            count+=1
            if i in extra:
                continue
            if count>15:
                break
            tt+=i
        lcd.message(tt)
        time.sleep(5)
        lcd.clear()
        GPIO.output(led,GPIO.LOW)
    time.sleep(delay)
