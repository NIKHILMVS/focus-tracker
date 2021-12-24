import ctypes
import argparse
import sys
import win32gui
import uiautomation as auto

def url_to_name(url):
    string_list = url.split('/')
    return string_list[2]

def get_chrome_url():
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        window = win32gui.GetForegroundWindow()
        chromeControl = auto.ControlFromHandle(window)
        edit = chromeControl.EditControl()
        return 'https://' + edit.GetValuePattern().Value
    else:
        print("sys.platform={platform} is not supported."
              .format(platform=sys.platform))
        print(sys.version)
    return "_active_window_name"


# ctypes.windll.user32.MessageBoxW(0, u"Error", u"BOBO", 0)
def focus_tracker(donot_watch_list):
    print("CTRL+C to Quit:")
    while True:
        if sys.platform not in ['linux', 'linux2']:
            temp=None
            while True:
                if not temp:
                    temp=""
                window=win32gui.GetForegroundWindow()
                _active_window_name = win32gui.GetWindowText(window)
                if "google chrome" in _active_window_name.lower():
                    _active_window_name = url_to_name(get_chrome_url())
                for i in donot_watch_list:
                    if i in _active_window_name:
                        ctypes.windll.user32.MessageBoxW(0, u"Pss, Please concentrate on your work without deviating",u"*** FOCUS MODE ***", 0)
                if _active_window_name!=temp:
                    print(_active_window_name)
                    temp=_active_window_name
        else:
            print("yet to work on this")
            pass

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-start",help="*** FOCUS MODE ON ***")
    parser.add_argument("-stop",help="*** FOCUS MODE OFF ***")
    parser.add_argument("-OUT",help="*** FOCUS OUT ON ***")
    args = parser.parse_args()
    import pdb;pdb.set_trace()
    if args.start:
    # if True:
        donot_watch_list=[]
        while True:
            inp=str(input())
            if "q" in inp:
                break
            donot_watch_list.append(inp)
        focus_tracker(donot_watch_list)


if __name__=='__main__':
    main()


