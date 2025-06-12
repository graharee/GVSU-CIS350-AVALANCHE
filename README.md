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
Nathan or Kalia? 
**all photos that are uploaded should be added into the figures folder on Git**
### 3.1 UML Diagram
brief description here

### 3.2 Use Case Diagram
brief description here

### 3.3 Communication Diagram
brief description here

## 4. User Guide / Implementation  

### 4.1 Main Screen

<p align="left">
  <img src="https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/LectureBot/Main%20Screen.png" alt="Main Screen" width="400" height='300'>
</p>

### 4.2 Recording Lecture

<p align="left">
  <img src="" alt="Recording" width="250">
</p>

### 4.3 Editing Text

<p align="left">
  <img src="https://github.com/graharee/GVSU-CIS350-AVALANCHE/blob/main/LectureBot/Editing.png" alt="Editing" width="250">
</p>

### 4.4 Saving Text

<p align="left">
  <img src="" alt="Saving" width="250">
</p>

### 4.5 Downloading File

<p align="left">
  <img src="" alt="Downloading" width="250">
</p>
pancake panel
<p align="left">
  <img src="" alt="Main Screen" width="250">
</p>

### 4.6 Translating File

<p align="left">
  <img src="" alt="Translating" width="250">
</p>

### 4.7 Uploading Audio File

<p align="left">
  <img src="" alt="Uploading" width="250">
</p>

## 5. Risk Analysis and Retrospective  
In the initial stages of creating **LectureBot** our main goals was first to create an application that listens to audio lecture and save this as a text file that can be editted. As development went on other features were added: uploading pre-exisiting audio files, and translating files into other languages. Overall, our goal along the way stayed consistent of creating a better learning experience for the user. 

One risk that was encountered later in development, was the time it takes to have **LectureBot** translate a .wav audio file into a text file. This risk was introduced because of the limited abilities free API have to offer. This risk included further testing and development to see if improvement could be made by processing smaller parts of audio at a time. After this was done, it was found that this slow translating to test process is something are willing to have since we are using free APIs. In the future, it would be awesome to do research about other APIs that could help us with this issue.

Another risk that was encountered was during the development of the translating text files feature. It was found that languages that include characters, like Chinese, are not something that **LectureBot** is able to handle. This is because it would immensely increase the size of **LectureBot** because it would have to hold each different character. This is something we were willing to sacrifice for right now, and would love to implement in the future when we have more resources available.

These two risks are not anything detrimental to **LectureBot**'s overall design. We are glad we were able to implement these as best as we could, and are excited for when we can improve our app!

## 6. Conclusion  
Overall, we believe that **LectureBot** helps improve students learning experiences. Instead of hurrying to write down notes, students are able to relax and know that **LectureBot** will handle it for them. We hope that **LectureBot** can be used to help the stress of busy students while also helping them in learning more. Of course, there is always room for improvement when it comes to app development, and this something we will continue to strive to do.  

## 7. Walkthrough Demonstration  
[Video Demo](put video demo here, Nathan or Kalia to make)  
