tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
#Список для проверки None
klasses2 = [
    '9А', '7В', '9Б', '9В', '8Б'
]

def task_generetor(tutors, klasses):
    for i in range(len(tutors)):
        if i < len(klasses):
            yield (tutors[i], klasses[i])
        else:
            yield (tutors[i], None)

gen = task_generetor(tutors, klasses)
for i in range(len(tutors)):
    print(next(gen))

print("\n------------------\n")
#Проверяем None
gen_2 = task_generetor(tutors, klasses2)
for i in range(len(tutors)):
    print(next(gen_2))