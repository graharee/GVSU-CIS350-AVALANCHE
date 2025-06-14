
# Overview

This document describes the software requirements for LectureBot, a user-friendly mobile app designed 
to assist students with lecture review and study. LectureBot records audio during lectures and converts
the recordings into text files that can be downloaded. These transcriptions can then be used for later 
study purposes.

# Functional Requirements

1. GUI 
   1. R1: The GUI shall have a download button that is marked with a download symbol.
   2. R2: The GUI shall display uploaded files in a list, in the order in which they were downloaded.
   3. R3: The GUI shall allow users to enter the names they desire for their files into the input boxes.
   4. R4: The GUI shall show an orange panel if the pancake button is pressed. 
   5. R5: The GUI shall have a peach background.

2. Audio-to-text
   1. R6: When the audio button is clicked, the program shall use the device's microphone to start listening.
   2. R7: The audio-to-text button shall have a microphone on it.
   3. R8: The audio-to-text button shall indent when clicked on.
   4. R9: The audio-to-text button shall activate the user's microphone to begin recording audio.
   5. R10: The audio-to-text button shall be in the upper right corner of the GUI at the end of the button line.

3. Download button
   1. R11: The user shall download the files to the user's computer by pressing the download button.
   2. R12: The download button shall download the file to the downloads folder in File Explorer on the user's computer.
   3. R13: By clicking the download button, the application shall prompt the user to name the document they saved.
   4. R14: The download button shall have an arrow pointing downwards to a line to indicate a file being downloaded.
   5. R15: The download button shall be in the upper right corner of the GUI.

4. Transcript Panel
   1. R16: Clicking the transcript button shall display a menu of past lecture transcripts that were saved by the user.
   2. R17: The panel shall display the names of the transcripts that have been downloaded.
   4. R18: Clicking the transcript button after pressing it once before shall close the transcript panel.
   5. R19: The transcript panel shall be orange in color.
   6. R20: The transcript panel shall display all files as .txt.
   7. R21: The transcript panel logo shall have three lines stacked on top of each other.
   8. R22: The transcript panel shall be in the upper left-hand corner. 

5. Translate Button
   1. R23: The translation button shall prompt the user to pick a language from a drop-down menu.
   2. R24: The translation button shall make a new file that is translated and download it to the user's computer.
   3. R25: The translation button shall prompt the user to name the translated file.
   4. R26: The translation button shall be allowed to translate non-character-based and character-based languages.
   5. R27: The translation button shall have a "T" on the button. 

6. Upload Audio File
   1. R28: The upload audio file function shall take a file of type .wave.
   2. R29: The upload button shall be in the upper right corner next to the download button. 
   3. R30: The upload button shall open up a window leading to the user's file explorer to pick a .wave file.
   4. R31: The upload file button shall paste the transcribed text into the textbox in the GUI.
   5. R32: The upload button shall have a box with an arrow pointing out of it. 

# Non-Functional Requirements

1. GUI 
   1. NR1: The GUI shall have correct grammar.
   2. NR2: The GUI shall use colors that are able to contrast with one another to be easier to read.
   3. NR3: The rendering of the GUI shall update within 30 seconds.
   4. NR4: The GUI shall not crash after a button is pushed.
   5. NR5: The GUI shall always be available whenever the code is run.

2. Audio-to-text
   1. NR6: The audio button shall always be available whenever the application is used.
   2. NR7: The audio button shall start recording audio with a 5-second delay.
   3. NR8: The text output shall be updated within 10 seconds of the audio being recorded.
   4. NR9: The text output shall be with minimal audio-to-text errors.
   5. NR10: The microphone shall stop listening after silence for 3 seconds.

3. Download Button
   1. NR11: The download button shall download the file within 5 seconds.
   2. NR12: The download button shall download the file named with the name you gave it.
   3. NR13: The download button shall always be available when clicked on.
   4. NR14: The download button shall access your File Explorer download folder and place the file there.
   5. NR15: The download button shall keep the contents of the file being downloaded accurate by copying it over exactly.

4. Transcript Menu
   1. NR16: The transcript panel shall display upon pancake button press.
   2. NR17: The transcripts will be available whenever the application is used.
   3. NR18: The transcripts shall open when the user presses the button with a "T" on it (Transcript button).
   5. NR19: The transcripts will be able to display 23 names of files at a time.
   6. NR20: The transcript menu shall open every time you press the pancake button.

5. Translate Button
   1. NR21: The translation shall be translated accurately from the original file using the Google trans package.
   2. NR22: The translation shall be completed within 3 seconds.
   3. NR23: The application shall be able to translate 1500 characters.
   4. NR24: The translation shall translate the text every time the translation button is pressed.
   5. NR25: The translation button shall translate correctly to no other language than the one selected by the user.

6. Upload Audio File
   1. NR26: The uploaded audio file shall be transcribed within 3 minutes.
   2. NR27: The upload button shall always be available every time the upload button is clicked.
   3. NR28: The upload button shall accurately transcribe the audio file that was uploaded.
   4. NR29: The upload button shall always open File Explorer so the .wave file can be clicked.
   5. NR30: The amount of text that shall be transcribable is 1200 words.

# Test Specification

## Unit Tests

### 1
| ID | Description | Steps | Input Values | Expected Output | Actual Output | Pass/Fail | Requirement Link |

| :-------------: | :----------: | :----------: | :----------: | :----------:| :----------: | :----------: | :----------: |

| UT1 | Testing if the download button exists. | 1. Run the unit test. | No inputs to this test. | No expected output of this unit test. | No output of this test case. | Pass | R14, R15 |

### 2
| ID | Description | Steps | Input Values | Expected Output | Actual Output | Pass/Fail | Requirement Link |

| :-------------: | :----------: | :----------: | :----------: | :----------:| :----------: | :----------: | :----------: |

| UT2 | Test that the audio button exists within the GUI. | 1. Run the unit test. | There are no input values for this test case. | No expected output. | There was no output. | Pass | R7, R10 |

### 3
| ID | Description | Steps | Input Values | Expected Output | Actual Output | Pass/Fail | Requirement Link |

| :-------------: | :----------: | :----------: | :----------: | :----------:| :----------: | :----------: | :----------: |

| UT3 | This tests if the pancake button exists within the GUI. | 1. Run the unit test. | No input values for this test case. | No expected output. | No output. | Pass | R21, R22 |

### 4
| ID | Description | Steps | Input Values | Expected Output | Actual Output | Pass/Fail | Requirement Link |

| :-------------: | :----------: | :----------: | :----------: | :----------:| :----------: | :----------: | :----------: |

| UT4 | This tests if the upload button exists within the GUI. | 1. Run the unit test. | No inputs to this unit test. | No expected output. | No actual output. | Pass | R29 |

## Integration Tests

### 1
| ID | Description | Steps | Input Values | Expected Output | Actual Output | Pass/Fail | Requirement Link |

| :-------------: | :----------: | :----------: | :----------: | :----------:| :----------: | :----------: | :----------: |

| IT1 | This tests that when the download button is pressed, the file will appear in the Transcript Panel | 1. Run "if_name_ == "_main_"" function| Inputs for this test is a document and a name for the file. | No expected output. | No actual output. | Pass | R13, R16, R17, R20 |

### 2
| ID | Description | Steps | Input Values | Expected Output | Actual Output | Pass/Fail | Requirement Link |

| :-------------: | :----------: | :----------: | :----------: | :----------:| :----------: | :----------: | :----------: |

| IT2 | <TC1 description> | <steps to execute TC1> | <input values to this
test case> | <expected output as a result of test case> | <actual output of
test case> | <did it pass or fail?> | <requirement IDs this test case is
linked to> |

### 3
| ID | Description | Steps | Input Values | Expected Output | Actual Output | Pass/Fail | Requirement Link |

| :-------------: | :----------: | :----------: | :----------: | :----------:| :----------: | :----------: | :----------: |

| IT3 | <TC1 description> | <steps to execute TC1> | <input values to this
test case> | <expected output as a result of test case> | <actual output of
test case> | <did it pass or fail?> | <requirement IDs this test case is
linked to> |

## System Tests

### 1
| ID | Description | Steps | Input Values | Expected Output | Actual Output | Pass/Fail | Requirement Link |

| :-------------: | :----------: | :----------: | :----------: | :----------:| :----------: | :----------: | :----------: |

| ST1 | <TC1 description> | <steps to execute TC1> | <input values to this
test case> | <expected output as a result of test case> | <actual output of
test case> | <did it pass or fail?> | <requirement IDs this test case is
linked to> |

### 2
| ID | Description | Steps | Input Values | Expected Output | Actual Output | Pass/Fail | Requirement Link |

| :-------------: | :----------: | :----------: | :----------: | :----------:| :----------: | :----------: | :----------: |

| ST2 | <TC1 description> | <steps to execute TC1> | <input values to this
test case> | <expected output as a result of test case> | <actual output of
test case> | <did it pass or fail?> | <requirement IDs this test case is
linked to> |

### 3
| ID | Description | Steps | Input Values | Expected Output | Actual Output | Pass/Fail | Requirement Link |

| :-------------: | :----------: | :----------: | :----------: | :----------:| :----------: | :----------: | :----------: |

| ST3 | <TC1 description> | <steps to execute TC1> | <input values to this
test case> | <expected output as a result of test case> | <actual output of
test case> | <did it pass or fail?> | <requirement IDs this test case is
linked to> |


# Software Artifacts

These are diagrams that we made throughout the project to describe and represent how we coded and expect LectureBot to run. These diagrams include the UML Class Diagram, the Communication Diagram, the Use Case Diagram, a link to our Jira account, where we kept track of what else needed to be done, and lastly, our Burn-up and Ghantt Charts that show our progress throughout the project.

* [Jira](https://cis350-avalanche.atlassian.net/jira/software/projects/SCRUM/boards/1)
* [UML Class Diagram](https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/figures/CIS350_Class_Diagram_Final.pdf)
* [Communication Diagram](https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/figures/CIS350_Communication_Diagram.pdf)
* [Use Case Diagram Explanation](https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/artifacts/use_case_diagram.md)
* [Burn-Up Chart](https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/figures/Burn_Up_Chart.pdf)
