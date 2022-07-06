import os, re, subprocess

class color:
    VIOLET, CYAN, DARK_CYAN, BLUE, GREEN, YELLOW, RED, WHITE, BLACK, GRAY, MAGENTA, BOLD, DIM, NORMAL, UNDERLINED, STOP = '\033[95m', '\033[96m', '\033[36m', '\033[94m', '\033[92m', '\033[93m', '\033[91m', '\033[37m', '\033[30m','\033[38;2;88;88;88m', '\033[35m', '\033[1m', '\033[2m', '\033[22m', '\033[4m', '\033[0m'

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'[ {color.YELLOW}>{color.STOP} ] {color.GREEN}{color.BOLD}unBerserker{color.STOP}\n[ {color.YELLOW}>{color.STOP} ] {color.GRAY}Made with {color.RED}<3{color.GRAY} by{color.STOP} Artic ({color.DARK_CYAN}{color.UNDERLINED}https://github.com/ArticOff{color.STOP})\n')
    with open(input(f'[ {color.MAGENTA}?{color.STOP} ] {color.GRAY}Enter the file\'s name:{color.STOP} ')) as code:
        data = code.read()
        try:
            s1 = re.search("if self.(.+?) in open", data).group(1)
            s1s = s1.replace("15", "12"); s2 = re.findall("{(.+?)}", data)
            source = (data.replace(s1, s1s).replace("{" + s2[0] + "}", "print").replace(",{" + s2[1] + "}()", ""))
        except AttributeError:
            return input(f'\n[ {color.RED}>{color.STOP} ] {color.GRAY}Please, enter a obfuscated file !{color.STOP}\n\nPress enter to continue... ')
        print('')
        f = open('tmpfile.py', "w")
        f.write(source)
        f.close()
        subprocess.run(f"py tmpfile.py")
        os.unlink('tmpfile.py')
        return input(f'\n[ {color.MAGENTA}*{color.STOP} ] {color.GRAY}Thanks for using our unberserker !{color.STOP}\n\nPress enter to continue... ') | exit()

if __name__ == "__main__":
    main()
