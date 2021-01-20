import os


if os.environ.get("CI") == True:
    print("yay")
else:
    print("nay")
