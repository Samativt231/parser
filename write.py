def writeTxt(faculties):
    with open('faculties.txt', 'w', encoding='utf-8') as f:
        for faculty in faculties:
            f.write(faculty + '\n')