import subprocess


def get_device_udid():
    device = subprocess.check_output(
        'adb devices', encoding='utf-8'
    ).splitlines()[1]
    if device:
        return device.split()[0]
    else:
        raise Exception('No active devices to connect')


def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '10',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': get_device_udid(),
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }
