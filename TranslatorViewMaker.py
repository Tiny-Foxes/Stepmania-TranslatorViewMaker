import configparser

parser = configparser.RawConfigParser(delimiters=('='),default_section=('Common'))
parser.optionxform = lambda option: option
parser.read("en.ini", encoding="utf-8")
# ⇈These lines are untouchable so DONT TOUCH THEM⇈
for parser.sections in parser:
    print(parser.sections)