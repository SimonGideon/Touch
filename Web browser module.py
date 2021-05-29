import webbrowser
webbrowser.open("http://github.com/opencv/tree/,mater/data/haarcascades")
# opens the provided link in the default browser
webbrowser.open_new_tab("http://stackflow.com") # Open the link in anew tab


# Opening the URL in a different browser.
s_path = webbrowser.get("C:\Program Files (x86)/firefox.exe")
ff = webbrowser.get(s_path)
ff.open("http:/stackflow.com/")
