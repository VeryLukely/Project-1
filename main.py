from gui import *
def main():

    window = Tk()
    widgets = GUI(window)

    window.title('Lab 2 Revamped')
    window.geometry('500x400')
    window.resizable(False, False)

    window.mainloop()

if __name__ == '__main__':
    main()