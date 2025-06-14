import unittest
from LectureBotGUI import LectureBot

class Test_GUI(unittest.TestCase):
    def setUp(self):
        self.app = LectureBot()
        self.gui = self.app.build()

    def test_app_exists(self):
        '''
            Description: This test checks if the app exists
            Return: NONE
        '''
        self.assertIsNotNone(self.app)

    def test_gui_exists(self):
        '''
            Description: This test checks if the gui exists
            Return: NONE
        '''
        self.assertIsNotNone(self.gui)

    def test_logo_img_exists(self):
        '''
            Description: This test checks if the logo image exists
            Return: NONE
        '''
        self.assertIsNotNone(self.gui.logo, "logo image does not exist")

    def test_download_button_img_exists(self):
        '''
            Description: This test checks if the download image exists
            Return: NONE
        '''
        self.assertIsNotNone(self.gui.downloadButtonImg, "download button image does not exist")

    def test_audio_button_img_exists(self):
        '''
            Description: This test checks if the audio image exists
            Return: NONE
        '''
        self.assertIsNotNone(self.gui.audioButtonImg, "audio button image does not exist")

    def test_pancake_button_img_exists(self):
        '''
            Description: This test checks if the audio image exists
            Return: NONE
        '''
        self.assertIsNotNone(self.gui.pancakeButtonImg, "pancake button image does not exist")

    def test_save_button_visible(self):
        '''
            Description: This test checks if the save button exists
            Return: NONE
        '''
        self.assertIsNotNone(self.gui.saveButton, "save button is not visible on the GUI")

    def test_download_button_visible(self):  # UT1 in Test Specifications 
        '''
            Description: This test checks if the download button exists
            Return: NONE
        '''
        self.assertIsNotNone(self.gui.downloadButton, "download button is not visible on the GUI")

    def test_pancake_button_visible(self):   # UT2 in Test Specifications
        '''
            Description: This test checks if the pancake button exists
            Return: NONE
        '''
        self.assertIsNotNone(self.gui.pancakeButton, "pancake button is not visible on the GUI")

    def test_audio_button_visible(self):  # UT3 in Test Specifications
        '''
            Description: This test checks if the audio button exists
            Return: NONE
        '''
        self.assertIsNotNone(self.gui.audioButton, "audio button is not visible on the GUI")

    def test_transcript_button_visible(self):  
        '''
            Description: This test checks if the transcript button exists
            Return: NONE
        '''
        self.assertIsNotNone(self.gui.transcriptButton, "transcript button is not visible on the GUI")

    def test_audio_file_button_visible(self):  # UT4 in Test Specifications
        '''
            Description: This test checks if the audio file button exists
            Return: NONE
        '''
        self.assertIsNotNone(self.gui.audiofilebutton, "audio file button is not visible on the GUI")

    def test_pancake_panel_exists(self):
        '''
            Description: This test checks if the pancake exists
            Return: NONE
        '''
        self.assertIsNotNone(self.gui.pancakePanel, "pancake panel does not exist")

if __name__ == '__main__':
    unittest.main()

