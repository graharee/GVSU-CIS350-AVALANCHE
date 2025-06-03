
# Overview

This document describes the software requirements for LectureBot, a user-friendly mobile app designed 
to assist students with lecture review and study. LectureBot records audio during lectures and converts
the recordings into text files that can be downloaded. These transcriptions can then be used for later 
study purposes.

# Functional Requirements

1. GUI 
   1. R1: The GUI shall use have a download button that is marked with a download symbol.
   2. R2: The GUI shall display uploaded files in a list according to how they were downloaded.
   3. R3: The GUI shall allow users to enter text into input fields to name the files created.
   4. R4: The GUI shall show an orange panel if the pancake button is pressed. 
   5. R5: The GUI shall have a white background.

2. Audio-to-text
   1. R6: When the audio button is clicked, the program shall use the device's microphone to start listening.
   2. R7: The audio-to-text button shall have a microphone on it.
   3. R8: The audio-to-text button shall indent when clicked on.

3. Download button
   1. R9: The user shall download the files to the user's computer by pressing the download button.
   2. R10: By clicking the download button, the application shall prompt the user to name the document they saved.

4. Transcript Panel
   1. R11: Clicking the transcript button shall display a menu of past lecture transcripts that were saved by the user.
   2. R12: The panel shall display the names of the transcipts downloaded.
   3. R13: Selecting the transcript file shall dispaly it within the application.
   4. R14: Clicking the transcript button after pressing it once before, shall close the transcript panel.

5. Translate Button
   1. R15: The translation button shall prompt the user to enter a non-character based language.
   2. R16: The translation button shall make a new file that is translated and download it to the user's computer.

6. Upload Audio File
   1. R17: The upload audio file function shall take file as type .wave.

# Non-Functional Requirements

1. GUI 
   1. NR1: The GUI shall use be easy for the user to read and understand.
   2. NR2: The GUI shall use colors that are able to contrast one another.
   3. NR3: The speed of the GUI shall update within a minute. 

2. Audio-to-text
   1. NR4: The audio button shall always be available whenever the application is used.
   2. NR5: The audio button shall start recording audio with a 5 second delay.
   3. NR6: The text output shall be updated within 10 seconds of the audio being recorded.
   4. NR7: The text output shall be with minimal audio to text errors.

3. Download Button
   1. NR8: The download button shall download the file in within 5 seconds.

4. Transcript Menu
   1. NR9: The transcript panel shall display upon pancake button press.
   2. NR10: The transcripts will be available whenever the application is used.
   3. NR11: The transcripts shall open upon user's press.
   4. NR12: The data in the transcripts will be held securly onto user's computer.
   5. NR13: The transcripts will be able to hold a high volume of text.

5. Translate Button
   1. NR14: The translation shall be translated accurate from the original file.
   2. NR15: The translation shall be translated within 3 seconds.
   3. NR16: The application shall be able to translate a large amount of text.

6. Upload Audio File
   1. NR17: The uploaded audio file shall be transcribed within 3 minutes.
