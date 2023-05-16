import data
import tool
import handle

'''
储存手势关键点条件及判断
'''

def UpdateGesture(hand_landmarks, mp_hands):

    global gesture_open 
    global gesture_otherOpen 
    global gesture_rightOpen 
    global gesture_leftOpen 
    global gesture_fist 
    global gesture_downGlide 
    global gesture_kneading 
    global gesture_kneadingOn 
    global gesture_together 
    global gesture_middle 

    #region 手势判断条件
    gesture_open = [
        data.fingerOriginDiffAverage_y < -0.2
        -0.08 < data.fingerAverage_z,
        data.fingerAverage_z < 0.1,
        data.fingerJointAverage_x - data.fingerAverage_x > -0.05,
        tool.GetFingerAverage((2,3),'y') < tool.GetFingerAverage((1,1),'y'),
        tool.GetFingerAverage((0,1,2,3,4),'y') < tool.GetFingerJointAverage((0,1,2,3,4),'y')
    ] # 张开手

    gesture_otherOpen = [
        data.fingerOriginDiffAverage_y > 0,
        data.fingerAverage_z < -0.1,
        tool.GetFingerJointAverage((1,2,3,4),'y') - tool.GetFingerAverage((1,2,3,4),'y') < 0
    ] # 张开手反向

    gesture_rightOpen = [
        data.fingerOriginDiffAverage_x > 0.25,
        data.fingerAverage_z < 0.1,
        data.fingerDiffAverage_y < 0.15
    ] # 张开手右

    gesture_leftOpen = [
        data.fingerOriginDiffAverage_x < -0.25,
        data.fingerAverage_z < 0.1,
        data.fingerDiffAverage_y < 0.15
    ] # 张开手左

    gesture_fist = [
        data.fingerOriginDiffAverage_y > (-0.2 * handle.distanceCoefficient), 
        data.fingerDiffAverage_x < (0.07 * handle.distanceCoefficient), 
        data.fingerAverage_z > -0.04, 
        abs(data.fingerJointAverage_y) < abs(data.fingerAverage_y),
        tool.GetFingerAverageDiff((1,2,3,4),'y') < 0.05
    ] # 握拳

    gesture_downGlide = [
        data.fingerOriginDiffAverage_y > (-0.3 * handle.distanceCoefficient),
        data.fingerDiffAverage_x < (0.1 * handle.distanceCoefficient),
        data.fingerAverage_z < -0.1
    ] # 下滑

    gesture_kneading = [
        data.f0f1diff_x < 0.015,
        data.f0f1diff_y < 0.07,
        data.f2f3f4Average_x > tool.GetFingerAverage((0,1),'x'),
        data.f2f3f4Average_y > tool.GetFingerAverage((0,1),'y'),
        data.originY > data.f2f3f4Average_y,
        tool.GetFingerAverage((2,3),'y') > tool.GetFingerAverage((1,1),'y'),
        abs(tool.GetFingerAverage((0,1),'x') - data.f2f3f4Average_x - data.originX) > 0.6
    ] # 双指捏合

    gesture_kneadingOn = [
        data.f0f1diff_x < 0.07,
        data.f0f1diff_y < 0.05,
        data.f2f3f4Average_y > tool.GetFingerAverage((0,1),'y'),
        data.originY > data.f2f3f4Average_y,
        tool.GetFingerAverage((2,3),'y') > tool.GetFingerAverage((1,1),'y'),
        abs(tool.GetFingerAverage((0,1),'x') - data.f2f3f4Average_x - data.originX) < 0.5,
        tool.GetFingerJointAverage((0,1),'y') > tool.GetFingerAverage((0,1),'y'),
        abs(tool.GetFingerJointAverage((0,1),'x') - tool.GetFingerAverage((0,1),'x')) < 0.04
    ] # 双指朝上捏合

    gesture_together = [
        tool.GetFingerAverageDiff((1,2),'x') < 0.08,
        tool.GetFingerAverageDiff((1,2),'y') < 0.07,
        abs(tool.GetFingerAverage((1,1),'x') - tool.GetFingerJointAverage((1,1),'x')) < 0.02,
        tool.GetFingerAverage((0,3,4),'y') > tool.GetFingerJointAverage((1,2),'y'),
        tool.GetFingerAverage((0,3,4),'y') > tool.GetFingerAverage((1,2),'y'),
        data.originY > tool.GetFingerAverage((0,3,4),'y'),
        tool.GetFingerJointAverage((3,4),'y') - tool.GetFingerAverage((3,4),'y') < 0,
        tool.GetFingerJointAverage((1,2),'y') - tool.GetFingerAverage((1,2),'y') > 0
    ] # 双指向上并拢

    gesture_middle = [
        tool.GetFingerAverageDiff((2,2),'x') < 0.08,
        tool.GetFingerAverage((0,1,3,4),'y') > tool.GetFingerJointAverage((2,2),'y'),
        tool.GetFingerAverage((0,1,3,4),'y') > tool.GetFingerJointAverage((0,1,3,4),'y')
    ]

    #endregion