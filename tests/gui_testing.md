## GUI Testing  
 
# Overview  
This testing is by print statements. Since the GUI does not have parameters that are passed from function to function, to ensure effective testing, print statements were placed each time the GUI changes. For example, when the download button is pressed, on the console terminal it says "download button pressed" in the task that follows the button pressed. This way of testing ensures the correct function follows the corresponding button press.  

# 1. Initializing Buttons  
When initializing the GUI, buttons are placed on the application by **placeButtons()**. When this process is finished, "buttons have been placed on GUI" is printed to the console terminal within this function.  

# 2. Translate Button  
When the translate button is pressed the program goes to **translatePress()**. This function immendiately prints "translate button is pressed" to the console terminal.  

# 3. Audio Button   
When the audio button is pressed the program goes to **audioPress()**. This function immendiately prints "audio button is pressed" to the console terminal.   

# 4. Save Button on Main Window  
When the save button is pressed the program goes to **savePress()**. This function immendiately prints "Saving..." to the console terminal.   

# 5. Pancake Button   
When the pancake button is pressed the program goes to **pancakePress()**. This function immendiately prints "pancake button is pressed" to the console terminal. 

# 6. Pancake Button Panel Visible
When the pancake button is pressed the program goes to **pancakePress()** and the state is determinded by **isPanelVisible**. This variable is initially set to **False** which indicates the panel is not visible, therefore should now be visible. When the panel is visible the function prints "pancake panel is visible" to the console terminal.

# 7. Pancake Button Panel Not Visible
When the pancake button is pressed the program goes to **pancakePress()** and the state is determinded by **isPanelVisible**. This variable is initially set to **False** which indicates the panel is not visible, therefore should now be visible. When **isPanelVisible** is true, the function makes the panel go away and the function prints "pancake panel is not visible" to the console terminal.

# 8. Download Button   
When the download button is pressed the program goes to **downloadPress()**. This function immendiately prints "download button is pressed" to the console terminal. 

# 9. Download Pop-Up Window 
When the download button is pressed the program goes to **downloadPress()**, this function then makes the popup window appear. This function immendiately prints "saving popup is shown" to the console terminal after the popup window appears.

# 10. Saving Button on Download Pop-Up Window 
When the save button is pressed on the download pop-up window the program goes to **getFilename()**. This function immendiately prints "save button is pressed" to the console terminal. 