let ruido_ext = 0
let humedad = 0
let luz_ext = 0
let temp_ext = 0
OLED.init(128, 64)
basic.forever(function () {
    OLED.clear()
    temp_ext = smarthome.ReadTemperature(TMP36Type.TMP36_temperature_C, AnalogPin.P1)
    luz_ext = smarthome.ReadLightIntensity(AnalogPin.P2)
    humedad = smarthome.ReadSoilHumidity(AnalogPin.P4)
    ruido_ext = smarthome.ReadNoise(AnalogPin.P3)
    OLED.writeStringNewLine("Temp externa: " + temp_ext + " oC")
    OLED.writeStringNewLine("Temp interna: " + input.temperature() + " oC")
    OLED.writeStringNewLine("Luz: " + luz_ext + " lm")
    if (temp_ext >= 20 || input.temperature() >= 20 || luz_ext == 345) {
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
    }
    basic.pause(5000)
    OLED.clear()
    OLED.writeStringNewLine("Humedad: " + humedad + " %")
    OLED.writeStringNewLine("Ruido externo: " + ruido_ext + " dB")
    OLED.writeStringNewLine("Ruido interno: " + input.soundLevel() + " dB")
    basic.pause(5000)
})
