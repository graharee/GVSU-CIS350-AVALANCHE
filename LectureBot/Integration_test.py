import unittest
from pathlib import Path
import asyncio
from googletrans import Translator
from unittest.mock import patch, Mock


class Mock_Download_to_Pancake:

    def __init__(self):
        self.filename = None
        self.lectureName = None
        self.Filelist = []

    def download_button_press(self):
        self.filename = input("Enter file name: ")

    def get_filename(self):
        self.lectureName = self.filename + ".txt"
        self.Filelist.append(self.lectureName)

    def display_pancake_panel(self):
        return self.Filelist


class Download_to_Pancake(unittest.TestCase):

    # Integration Test
    def test_download_to_pancake(self):
        m = Mock_Download_to_Pancake()
        m.download_button_press()
        m.get_filename()
        m.display_pancake_panel()
        name = m.filename + ".txt"
        self.assertIn(name, m.Filelist)


class Mock_Download_to_Computer:

    def __init__(self):
        self.filename = None
        self.lectureName = None
        self.doc = "Int_testing_down_comp.txt"
        self.downloads = None
        self.file_path = None
        self.content = None

    def download_press(self):
        self.filename = input("Enter file name: ")

    def get_file_name(self):
        self.lectureName = self.filename + ".txt"

    def save_file(self):
        self.downloads = Path.home() / "Downloads"
        self.file_path = self.downloads / self.lectureName

        with open(self.doc, "r") as output:
            self.content = output.read()

        with open(self.file_path, "w") as new_file:
            new_file.write(self.content)

        with open(self.doc, "w") as output:
            output.write("")


class Download_to_Computer(unittest.TestCase):

    def assertIsFile(self, file_path):
        path = file_path.is_file()
        return Path

    # Integration Test
    def test_download_to_computer(self):
        m = Mock_Download_to_Computer()
        m.download_press()
        m.get_file_name()
        m.save_file()
        file_path = m.file_path
        self.assertIsFile(file_path)
        original_content = m.content
        f = open(file_path, "r")
        new_content = f.read()
        f.close()
        self.assertEqual(original_content, new_content)


class Mock_Translate:

    def __init__(self):
        self.translate_name = None
        self.Filelist = []
        self.lectureName = None
        self.doc = "Int_testing_translate.txt"
        self.downloads = None
        self.file_path = None
        self.content = None
        self.src_list = []
        self.dest_list = []
        self.LANGUAGES = dict({'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy',
                          'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs',
                          'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny',
                          'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co',
                          'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en',
                          'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr',
                          'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el',
                          'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he',
                          'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig',
                          'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw',
                          'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku',
                          'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt',
                          'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml',
                          'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my',
                          'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa',
                          'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru',
                          'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn',
                          'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so',
                          'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg',
                          'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur',
                          'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh',
                          'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'})

    def translatePress(self):
        self.translate_name = input("Enter translated file name: ")
        self.src_list = ['Afrikaans', 'Albanian', 'Amharic', 'Arabic',
                         'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian',
                         'Catalan', 'Cebuano', 'Chichewa', 'Chinese (simplified)', 'Chinese (traditional)',
                         'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian',
                         'Filipino', 'Finnish', 'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek',
                         'Gujarati', 'Haitian creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hebrew', 'Hindi', 'Hmong',
                         'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese',
                         'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Korean', 'Kurdish (Kurmanji)', 'Kyrgyz', 'Lao',
                         'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay',
                         'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Myanmar (burmese)', 'Nepali',
                         'Norwegian', 'Odia', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Romanian',
                         'Russian', 'Samoan', 'Scots gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi', 'Sinhala',
                         'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tajik',
                         'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek',
                         'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu']
        self.dest_list = ['Zulu', 'Afrikaans', 'Albanian', 'Amharic', 'Arabic',
                          'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian',
                          'Catalan', 'Cebuano', 'Chichewa', 'Chinese (simplified)', 'Chinese (traditional)',
                          'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian',
                          'Filipino', 'Finnish', 'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek',
                          'Gujarati', 'Haitian creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong',
                          'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese',
                          'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Korean', 'Kurdish (Kurmanji)', 'Kyrgyz',
                          'Lao', 'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy',
                          'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Myanmar (burmese)',
                          'Nepali', 'Norwegian', 'Odia', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi',
                          'Romanian', 'Russian', 'Samoan', 'Scots gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi',
                          'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish',
                          'Tajik', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek',
                          'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba']

    async def translate(self, text, src_lang, dest_lang):
        trans = Translator()
        translation = await trans.translate(text, src=src_lang, dest=dest_lang)
        print(translation.text)
        # Writes to the
        f = open(f"Int_testing_translate.txt", "w")
        f.close()
        trans_file = open(f"Int_testing_translate.txt", "r+", encoding="utf-8", errors='ignore')
        trans_file.write(translation.text)
        trans_file.close()


class Translate(unittest.TestCase):

    def assertIsFile(self, file_path):
        path = file_path.is_file()
        return Path

    # Integration Test
    async def test_translate(self):
        mt = Mock_Translate()
        d = open("Int_testing_translate.txt", "r")
        reading = d.read()
        d.close()
        self.assertEqual(reading, "This is a tesing doc. It will be translated.\n")
        trans = Translator()
        i = 0
        j = 0
        for i in mt.src_list:
            for j in mt.dest_list:
                translation = await trans.translate(reading, i, j)
                output = asyncio.run(mt.translate(reading, i, j))
                self.assertEqual(output, translation.text)


if __name__ == "__main__":
    dp = Download_to_Pancake()
    dp.test_download_to_pancake()
    dc = Download_to_Computer()
    dc.test_download_to_computer()
    mt = Mock_Translate()
    t = Translate()
    text = "This is a tesing doc. It will be translated.\n"
    for i in mt.src_list:
        for j in mt.dest_list:
            asyncio.run(t.test_translate())