import RPi.GPIO as GPIO
import time

# GPIO 핀 설정
LCD_RS = 11
LCD_E = 10
LCD_D4 = 6
LCD_D5 = 5
LCD_D6 = 4
LCD_D7 = 1

# 명령어 상수
LCD_CLEAR = 0x01
LCD_RETURN_HOME = 0x02
LCD_ENTRY_MODE_SET = 0x04
LCD_DISPLAY_CONTROL = 0x08
LCD_CURSOR_SHIFT = 0x10
LCD_FUNCTION_SET = 0x20
LCD_SET_CGRAM_ADDR = 0x40
LCD_SET_DDRAM_ADDR = 0x80

# GPIO 초기화
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LCD_RS, GPIO.OUT)
GPIO.setup(LCD_E, GPIO.OUT)
GPIO.setup(LCD_D4, GPIO.OUT)
GPIO.setup(LCD_D5, GPIO.OUT)
GPIO.setup(LCD_D6, GPIO.OUT)
GPIO.setup(LCD_D7, GPIO.OUT)

# LCD 초기화 함수
def lcd_init():
    lcd_byte(0x33, False)
    lcd_byte(0x32, False)
    lcd_byte(LCD_FUNCTION_SET | LCD_4BITMODE | LCD_2LINE | LCD_5x8DOTS, False)
    lcd_byte(LCD_DISPLAY_CONTROL | LCD_DISPLAY_ON, False)
    lcd_byte(LCD_CLEAR, False)
    time.sleep(0.002)

# LCD 바이트 전송 함수
def lcd_byte(bits, mode):
    GPIO.output(LCD_RS, mode)
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits & 0x10 == 0x10:
        GPIO.output(LCD_D4, True)
    if bits & 0x20 == 0x20:
        GPIO.output(LCD_D5, True)
    if bits & 0x40 == 0x40:
        GPIO.output(LCD_D6, True)
    if bits & 0x80 == 0x80:
        GPIO.output(LCD_D7, True)
    lcd_toggle_enable()

    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits & 0x01 == 0x01:
        GPIO.output(LCD_D4, True)
    if bits & 0x02 == 0x02:
        GPIO.output(LCD_D5, True)
    if bits & 0x04 == 0x04:
        GPIO.output(LCD_D6, True)
    if bits & 0x08 == 0x08:
        GPIO.output(LCD_D7, True)
    lcd_toggle_enable()

# LCD Enable 토글 함수
def lcd_toggle_enable():
    time.sleep(0.0005)
    GPIO.output(LCD_E, True)
    time.sleep(0.0005)
    GPIO.output(LCD_E, False)
    time.sleep(0.0005)

# LCD 문자열 출력 함수
def lcd_string(message):
    message = message.ljust(16, " ")
    for i in range(16):
        lcd_byte(ord(message[i]), True)

# LCD 지우기 함수
def lcd_clear():
    lcd_byte(LCD_CLEAR, False)
    time.sleep(0.002)

# 메인 함수
def main():
    # LCD 초기화
    lcd_init()

    # LCD에 문자열 출력
    lcd_string("HELLO WORLD")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        pass

    finally:
        # LCD 지우기
        lcd_clear()
        GPIO.cleanup()

if __name__ == '__main__':
    main()


# import wiringpi as wp
# from time import sleep

# LCD_RS = 11
# LCD_E = 10
# LCD_D4 = 6
# LCD_D5 = 5
# LCD_D6 = 4
# LCD_D7 = 1

# # Initialize wiringPi
# wp.wiringPiSetup()

# # Initialize the LCD
# lcd = wp.lcdInit(2, 16, 4, LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7, 0, 0, 0, 0)

# if lcd == -1:
#     print("lcd init failed!")
#     exit(1)

# # Set the cursor to the first position (0, 0)
# wp.lcdPosition(lcd, 0, 0)

# # Print the message to the LCD
# wp.lcdPuts(lcd, "HELLO WORLD")

# # Wait for user input
# input("Press Enter to clear the LCD...")

# # Clear the LCD
# wp.lcdClear(lcd)
