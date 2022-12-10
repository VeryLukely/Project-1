from tkinter import *


class GUI:
    def __init__(self, window):

        """
        Constructor to create initial state of an account balance object
        :param students: Total number of students.
        :param scores: Students scores in alphabetical order, with spaces inbetween.
        :param lb: Letterbox to display calculated grades
        :param button: Submit button to run code and clear entry boxes.
        """

        # Constructors for GUI objects

        self.window = window

        self.frame_students = Frame(self.window)
        self.label_students = Label(self.frame_students, text='Total number of students:')
        self.entry_students = Entry(self.frame_students)

        self.frame_scores = Frame(self.window)
        self.label_scores = Label(self.frame_scores, text='Enter all scores w/ spaces: ')
        self.entry_scores = Entry(self.frame_scores)

        self.frame_extra = Frame(self.window)
        self.label_extra = Label(self.frame_extra, text='Enter possible extra credit: ')
        self.entry_extra = Entry(self.frame_extra)

        self.lb = Frame(self.window)
        self.lb = Listbox(self.window, height=30, width=40, font='TimesNewRoman', highlightcolor='Gray', fg='Blue', bg='Silver')

        self.frame_button = Frame(self.window)
        self.submit_button = Button(self.frame_button, text='Submit', command=self.clicked)

        # Packs to manage layouts for GUI object

        self.label_students.pack(side='left')
        self.entry_students.pack(side='left', padx=5)
        self.frame_students.pack(anchor='s', pady=10, padx=10)

        self.label_scores.pack(side='left')
        self.entry_scores.pack(side='left', padx=15)
        self.frame_scores.pack(anchor='s', pady=5, padx=10)

        self.frame_extra.pack(anchor='s', pady=10, padx=10)
        self.entry_extra.pack(side='right', padx=15)
        self.label_extra.pack(side='bottom', anchor='center')

        self.frame_button.pack(side='bottom', anchor='center')
        self.submit_button.pack(pady=20)

        self.lb.pack(anchor='center')

    def clicked(self):

        self.lb.delete(0, END)

        students = self.entry_students.get()
        students = int(students)

        extra = self.entry_extra.get()
        extra = int(extra)

        scores = self.entry_scores.get()

        score_list = scores.split()

        best = 0

        # Input validation to confirm number of students matches number of grades

        if len(score_list) > students:
            self.lb.insert(1, "Error: Too many scores for # of students")
            print("Error: Too many scores for amount of students")
            self.entry_students.delete(0, END)
            self.entry_scores.delete(0, END)

        elif len(score_list) < students:
            self.lb.insert(1, "Error: Too few scores for # of students")
            print("Error: Too few scores for amount of students")
            self.entry_students.delete(0, END)
            self.entry_scores.delete(0, END)

        else:
            for i in range(students):

                # Finds best score in order to grade on a curve

                score_list[i] = int(score_list[i])

                if score_list[i] > best:
                    best = score_list[i]

            overflow = 0
            if best > 100:
                overflow = best
                best = 100

            grade_list = []

            # Executes code to assign score_list with corresponding grades in grade_list based on lowest grade

            for i in range(students):
                if score_list[i] >= int(best) - 3:
                    grade_list.append("A+")
                elif score_list[i] >= int(best) - 7:
                    grade_list.append("A")
                elif score_list[i] >= int(best) - 10:
                    grade_list.append("A-")
                elif score_list[i] >= int(best) - 13:
                    grade_list.append("B+")
                elif score_list[i] >= int(best) - 17:
                    grade_list.append("B")
                elif score_list[i] >= int(best) - 20:
                    grade_list.append("B-")
                elif score_list[i] >= int(best) - 23:
                    grade_list.append("C+")
                elif score_list[i] >= int(best) - 27:
                    grade_list.append("C")
                elif score_list[i] >= int(best) - 30:
                    grade_list.append("C-")
                elif score_list[i] >= int(best) - 33:
                    grade_list.append("D+")
                elif score_list[i] >= int(best) - 37:
                    grade_list.append("D")
                elif score_list[i] >= int(best) - 40:
                    grade_list.append("D-")
                elif score_list[i] < int(best) - 40:
                    grade_list.append("F")

            # Clears entry boxes after being read

            self.entry_students.delete(0, END)
            self.entry_scores.delete(0, END)
            self.entry_extra.delete(0, END)

            for i in range(students):

                # Constructs sentences to be displayed in letterbox

                istring = str(i + 1)
                scoreliststring = str(score_list[i])
                gradeliststring = str(grade_list[i])

                userstring = "Student " + istring + "'s score is " + scoreliststring + " and grade is " + gradeliststring

                self.lb.insert(i, userstring)

            # Displays error if highest score is greater than maximum and resets program

            max = 100 + extra
            if overflow > max:
                self.lb.delete(0, END)
                self.lb.insert(1, "Error: Highest score exceeds maximum")
