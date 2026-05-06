ruido_ext = 0
humedad = 0
luz_ext = 0
temp_ext = 0
OLED.init(128, 64)

def on_forever():
    global temp_ext, luz_ext, humedad, ruido_ext
    OLED.clear()
    temp_ext = smarthome.read_temperature(TMP36Type.TMP36_TEMPERATURE_C, AnalogPin.P1)
    luz_ext = smarthome.read_light_intensity(AnalogPin.P2)
    humedad = smarthome.read_soil_humidity(AnalogPin.P4)
    ruido_ext = smarthome.read_noise(AnalogPin.P3)
    OLED.write_string_new_line("Temp externa: " + str(temp_ext) + " oC")
    OLED.write_string_new_line("Temp interna: " + str(input.temperature()) + " oC")
    basic.pause(5000)
    OLED.clear()
    OLED.write_string_new_line("Luz externa: " + str(luz_ext) + " lm")
    OLED.write_string_new_line("Luz interna: " + str(input.light_level()) + " lm")
    basic.pause(5000)
    OLED.clear()
    OLED.write_string_new_line("Humedad: " + str(humedad) + " %")
    basic.pause(5000)
    OLED.clear()
    OLED.write_string_new_line("Ruido externo: " + str(ruido_ext) + " dB")
    OLED.write_string_new_line("Ruido interno: " + str(input.sound_level()) + " dB")
    basic.pause(5000)
basic.forever(on_forever)
