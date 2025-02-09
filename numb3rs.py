import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    matches = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$",ip)
    if matches !=None:
        for i in matches.groups():
                if int(i)>255:
                    return False
        return True
    else:
         return False



if __name__ == "__main__":
    main()
