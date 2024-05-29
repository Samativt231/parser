from omgtu import getFaculties
from write import writeTxt

if __name__ == '__main__':
    faculties = getFaculties()
    if faculties:
        writeTxt(faculties)