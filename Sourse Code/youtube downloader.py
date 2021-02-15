import webbrowser

url = input("Give me the url :")
download = url [:12] + "ss" + url [12:]

webbrowser.open(download)