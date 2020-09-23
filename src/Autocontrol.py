#Robomaster Python

variable_LedID = 0
list_LedList = RmList()

def user_defined_gimbalSpin():
    global variable_LedID
    global list_LedList
    gimbal_ctrl.set_rotate_speed(100)
    chassis_ctrl.set_rotate_speed(180)
    media_ctrl.play_sound(rm_define.media_sound_gimbal_rotate)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_marquee)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
    gimbal_ctrl.rotate(rm_define.gimbal_left)
    chassis_ctrl.rotate_with_time(rm_define.clockwise, 0.4)
    gimbal_ctrl.rotate(rm_define.gimbal_right)
    chassis_ctrl.rotate_with_time(rm_define.anticlockwise, 0.8)
    gimbal_ctrl.rotate(rm_define.gimbal_left)
    chassis_ctrl.rotate_with_time(rm_define.clockwise, 0.4)
    led_ctrl.turn_off(rm_define.armor_all)
    rmexit()

def start():
    global variable_LedID
    global list_LedList
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    media_ctrl.play_sound(rm_define.media_sound_count_down)
    led_ctrl.set_top_led(rm_define.armor_top_all, 69, 215, 255, rm_define.effect_always_off)
    time.sleep(0.5)
    variable_LedID = 0
    while not 7 < variable_LedID:
        variable_LedID = variable_LedID + 1
        list_LedList.append(variable_LedID)
        led_ctrl.set_single_led(rm_define.armor_top_all, list_LedList, rm_define.effect_always_on)
        time.sleep(0.4)
    user_defined_gimbalSpin()


