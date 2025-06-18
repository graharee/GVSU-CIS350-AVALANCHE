# CIS 350 Project - Team Avalanche  

# LectureBot 

<p align="center">
  <img src="https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/LectureBot/logo.png" alt="LectureBot Logo" width="250">
</p>

## Team Members and Roles

* [Reegan Graham](https://github.com/graharee/CIS350-HW2-GRAHAM) (Developer, Documentor)
* [Kalia Dorgelo](https://github.com/DorgeloK/CIS350-HW2-Dorgelo/tree/main) (Developer, Tester)
* [Nathan Finkel](https://github.com/nathanfinkel/CIS350-HW2-Finkel.git) (Developer, Tester)

## How to Run the Code

To run this code, you need a couple of things. You need a Python IDE, and to download the following packages:
* SpeechRecognition
* PyAudio
* pyttsx3
* tkinter

You also need to download a feature called ffmpeg. The following are the steps to download it for Windows Users:
  1. Type in the Google search engine "install ffmpeg"
  2. Click the link that says "Download FFmpeg".
  3. Hover over the type of computer you have (Linux, Windows, or Apple); in most cases, it's Windows.
  4. Click on the top link that says "gyan.dev"
  5. Scroll down to "Git master branch build"
  6. Click "ffmpeg-git-full.7g"
  7. Open up the folder that it downloads into
  8. Right-click on it and go down to 7-Zip
  9. Click Extract files and archive it somewhere other than the download folder
  10. Go to where you extracted it to, click into the folder
  11. Then click into the bin folder
  12. Then copy the path of that (it's right to the left of the search bar)
  13. Hit the Windows button and type path. Then click Enter
  14. Go into the "Environmental Variables"
  15. In the first scroll-down menu, look for the word "Path" and click it.
  16. Click Edit
  17. In the pop-up that should appear, click new
  18. Paste in the path that you copied earlier
  19. Click "Ok" for the 3 pop-ups
  20. To test that you installed it correctly, you can press the Windows button again
  21. Type "cmd" then press Enter
  22. Then type in the terminal "ffmpeg" and click enter
  23. If you get a whole bunch of stuff, then you did it correctly.

Last but not least, go into your IDE Terminal and type "pip install -U openai-whisper to have whisper working.

After all of that is downloaded, you can go into the Python code in your IDE and click run.
A screen should pop up with a text box and buttons in the top right and left corners, that is LectureBot

Congratulations! You are now running the application. Below in the "User Guide / Implementation" section, you can see how the app works.

## Important Links   

[Github](https://github.com/graharee/GVSU-CIS350-AVALANCHE)  

[Jira](https://cis350-avalanche.atlassian.net/jira/software/projects/SCRUM/boards/1)

[UML Class Diagram](https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/figures/CIS350_Class_Diagram_Final.pdf)

[Communication Diagram](https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/figures/CIS350_Communication_Diagram.pdf)

[Use Case Diagram Explanation](https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/artifacts/use_case_diagram.md)

## 1. Abstract 
School is difficult, students often face challenges that effect their ability to fully engage in lecture halls. These include mental fatigue, difficulty concentrating during long class periods, and instructors who speak too quickly for hand written note-taking to keep up. Such issues can lead to incomplete notes, missed information, and added stress when reviewing material outside of class. To address these problems, we developed **LectureBot** that acts as an additional pair of ears for the student. **LectureBot** is designed to capture and process spoken lecture content, providing students with organized summaries of what was discussed. By reducing the cognitive load during class and supporting review afterward, **LectureBot** enhances the overall learning experience. It empowers students to focus on understanding, and ensures that no important detail is lost.

## 2. Introduction  
**LectureBot** aims to help students cultivate a better learning experience within the classroom. This application allows students to record lectures (in-person or online), edit the transcripts, and save it as a text file for later studying. Not only does **LectureBot** offer a way to record a live lecture, students are able to get a written transcript of a recorded lecture, simply by uploading a .wav file. Lastly, to further enhance the user's learning experience, **LectureBot** allows users to be able to translate their lecture into a non-charcter language of their choosing.   

## 3. Architectural Design  

**all photos that are uploaded should be added into the figures folder on Git**
### 3.1 UML Diagram

<p align="left">
  <img src="https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/figures/CIS350_Class_Diagram_Final.pdf" alt="UML Diagram" width="300" height='300'>
</p>

### 3.2 Use Case Diagram

<p align="left">
  <img src="https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/artifacts/use_case_diagram.pdf" alt="Use Case Diagram" width="300" height="300">
</p>

### 3.3 Communication Diagram

<p align="left">
  <img src="https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/figures/CIS350_Communication_Diagram.pdf" alt="Communication Diagram" width="300" height="300">
</p>

## 4. User Guide / Implementation  

### 4.1 Main Screen

<p align="left">
  <img src="https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/LectureBot/Main%20Screen.png" alt="Main Screen" width="400" height='400'>
</p>
When you first open the app. This is what it looks like.

### 4.2 Recording Lecture

<p align="left">
  <img src="https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/LectureBot/Recording.png" alt="Recording" width="450" height='400'>
</p>
When you click on the microphone button at the top, you can see your microphone activate at the bottom left hand of the photo and as you talk you can see the text box update with what you said.

### 4.3 Editing Text

<p align="left">
  <img src="https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/LectureBot/Editing.png" alt="Editing" width="400" height='400'>
</p>
You can type new sentences and fix grammar by typing in the text box.

### 4.4 Saving Text

<p align="left">
  <img src="https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/LectureBot/Saving.png" alt="Saving" width="450" height='400'>
</p>
There is no physical change when you press the save button at the top, but in the screenshot, you can see "Saving..." in the terminal on PyCharm to prove that it's saving.

### 4.5 Downloading File

<p align="left">
  <img src="https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/LectureBot/Downloading.png" alt="Downloading" width="400" height='400'>
</p>
When you hit the download button in the upper right-hand corner, you can see that a window pops up prompting you to name the file.

### 4.6 Pancake Panel

<p align="left">
  <img src="https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/LectureBot/Pancake.png" alt="Pancake" width="400" height='400'>
</p>
After you name the file from the download button, it will pop up here. In this case, I named the file "Demo" and it popped up over on the pancake panel.

### 4.7 Translating File

<p align="left">
  <img src="https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/LectureBot/Translating.png" alt="Translating" width="400" height='400'>
</p>
When you click the "T" button in the upper right-hand corner, this window pops up, and you can select the language you want to go to. Its default starting language is English, and its default ending language is Spanish. Underneath, you can name the new translated file (The name you put here will also show up on the pancake panel). 

### 4.8 Uploading Audio File

<p align="left">
  <img src="https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/LectureBot/Uploading.png" alt="Uploading" width="400" height='400'>
</p>
Your file explorer window pops up when you click on the upload button in the upper right-hand corner, so you can select your .wave file. 

## 5. Risk Analysis and Retrospective  
In the initial stages of creating **LectureBot**, our main goal was first to create an application that listens to audio lectures and saves them as a text file that can be edited. As development went on, other features were added: uploading pre-existing audio files and translating files into other languages. Overall, our goal along the way stayed consistent in creating a better learning experience for the user. 

One risk that was encountered later in development was the time it takes to have **LectureBot** translate a .wav audio file into a text file. This risk was introduced because of the limited abilities free API have to offer. This risk included further testing and development to see if improvement could be made by processing smaller parts of the audio at a time. After this was done, it was found that this slow translation to test process is something we are willing to have since we are using free APIs. In the future, it would be awesome to do research about other APIs that could help us with this issue.

This risk is not anything detrimental to **LectureBot**'s overall design. We are glad we were able to implement these as best as we could, and are excited for when we can improve our app!

## 6. Conclusion  
Overall, we believe that **LectureBot** helps improve students' learning experiences. Instead of hurrying to write down notes, students are able to relax and know that **LectureBot** will handle it for them. We hope that **LectureBot** can be used to help the stress of busy students while also helping them in learning more. Of course, there is always room for improvement when it comes to app development, and this is something we will continue to strive to do.  

## 7. Walkthrough Demonstration  
[Video Demo](https://gvsu.hosted.panopto.com/Panopto/Pages/Capture.aspx?folderId=7ffa5170-2254-48eb-8150-b300012061e9)
