import pyshorteners

link = input("Enter your link here: ")

linkshortener= pyshorteners.Shortener()

x=linkshortener.tinyurl.short(link)
print(x)