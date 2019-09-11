#!/Users/william881218/anaconda3/bin/python3
from crawler import TutorCase
import sys, getopt
opts_list = "hi:a:c:l:n:s:t:u:d:f:"
args_list = ["id=", "age=", "city=", "location=", "new=", "subject=", "time=", "url=", "day=", "frequent="]
opts_dict = {"--id":0, "--age":1, "--city":2, "--location":3, "--new":4, "--subject":5, "--time":6, "--price":5, \
"--day":6, "--frequent":6, "-i":0, "-a":1, "-c":2, "-l":3, "-n":4, "-s":5, "-t":6, "-p":5, "-d":6, "-f":6}
"""
id, age, city, loc, new, subject, time
"""
def print_tutorial():
    f_tutorial = open('argument_tutorial')
    for line in f_tutorial:
        print(line, end='')
    f_tutorial.close()

def main(argv):
    url = 'http://teaching.com.tw/member/case-list.php'
    try:
        opts, args = getopt.getopt(argv, opts_list, args_list)
    except getopt.GetoptError:
        print_tutorial()
        sys.exit()
    target = []
    for opt, arg in opts:
        if opt == '-h':
            print_tutorial()
            sys.exit()
        elif opt in ('-u', '--url'):
            url = arg
        else:
            target.append((opts_dict[opt], arg))
    tutorCase = TutorCase(url)
    for id, arg in target:
        print(id, ':', arg)
    print(tutorCase)

if __name__ == '__main__':
    main(sys.argv[1:])
