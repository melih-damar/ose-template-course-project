import os


if os.environ.get("CI") == "true":
    print("yay")
else:
    print("nay")

print(os.environ.get("CI"))
