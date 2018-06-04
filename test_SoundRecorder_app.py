from appium import webdriver
import unittest
from selenium.webdriver.common.proxy import Proxy, ProxyType
from subprocess import call
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from appium.webdriver.common.touch_action import TouchAction


class SoundRecorderUITestSuite(unittest.TestCase):

    def setUp(self):
        """Set up for the test"""
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Pixel 2 Emulator'
        desired_caps['name'] = 'SoundRecorder Appium Test'
        desired_caps['app'] = '/Users/KevinChuang/PycharmProjects/android-ui-testing/com.danielkim.soundrecorder_130.apk'
        desired_caps['autoGrantPermissions'] = True
        desired_caps['fullReset'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=desired_caps, keep_alive=True)

    def test_whether_app_is_installed(self):
        "Test if the app has been installed correctly"
        self.driver.is_app_installed('com.danielkim.soundrecorder')

    def test_recording(self):
        record_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "com.danielkim.soundrecorder:id/btnRecord")))
        record_button.click()

        # self.driver.implicitly_wait(10000)

        stop_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "com.danielkim.soundrecorder:id/btnRecord")))
        stop_button.click()

        saved_recordings_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='SAVED RECORDINGS']")))
        saved_recordings_button.click()

        self.assertTrue(self.driver.find_elements_by_id('com.danielkim.soundrecorder:id/card_view'))

    def test_playback(self):
        record_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "com.danielkim.soundrecorder:id/btnRecord")))
        record_button.click()

        stop_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "com.danielkim.soundrecorder:id/btnRecord")))
        stop_button.click()

        saved_recordings_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='SAVED RECORDINGS']")))
        saved_recordings_button.click()

        recorded_file = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "com.danielkim.soundrecorder:id/card_view")))
        recorded_file.click()

        self.assertTrue(self.driver.find_elements_by_id('com.danielkim.soundrecorder:id/mediaplayer_view'))
        self.assertTrue(self.driver.find_elements_by_id('com.danielkim.soundrecorder:id/seekbar'))
        # self.assertTrue(self.driver.find_elements_by_id('com.danielkim.soundrecorder:id/fab_play'))

        play_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "com.danielkim.soundrecorder:id/fab_play")))
        play_button.click()

    def test_delete_file(self):
        record_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "com.danielkim.soundrecorder:id/btnRecord")))
        record_button.click()

        stop_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "com.danielkim.soundrecorder:id/btnRecord")))
        stop_button.click()

        saved_recordings_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='SAVED RECORDINGS']")))
        saved_recordings_button.click()

        ## Check if there is a file present
        self.assertTrue(self.driver.find_elements_by_id('com.danielkim.soundrecorder:id/card_view'))

        actions = TouchAction(self.driver)
        actions.long_press(self.driver.find_element_by_xpath("//android.widget.FrameLayout[contains(@resource-id,'card_view')]"))
        actions.perform()

        delete_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Delete File']")))
        delete_button.click()

        confirm_yes_button =  WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='YES']")))
        confirm_yes_button.click()

        ## Assert that there is more files here
        self.assertFalse(self.driver.find_elements_by_id('com.danielkim.soundrecorder:id/card_view'))


    def tearDown(self):
        """Tear down the test"""
        self.driver.quit()