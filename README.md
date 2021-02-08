# pseudo.py
Simple Library For Joining And Controlling Google Meet.
NO! Selenium - No More Your Browser May Be Insecure...
Requirements: pyautogui
pip install pyautogui

Connect To Desired Meet:
Join the meet at least once before because PSEUDO does not wait for you to be let in.
To join a meet type:

import pseudo
pseudo.connectToMeet("meet url")

Commands:

pseudo.mic() - Turns On/Off Mic (Have to be in meet already)<br>
pseudo.cam() - Same but Camera<br>
pseudo.leave() - Leave Meet<br>
pseudo.presentScreen() - Present Screen (Full Window)
pseudo.selectScreen(urlorprogram) - Selects Screen - E.G. pseudo.presentScreen(); pseudo.selectScreen("calc") - add a /max switch before to make it fullscreen
pesudo.stopShare() - Stops presentScreen() share.
pseudo.sendChat(message) - Send message in chat.





