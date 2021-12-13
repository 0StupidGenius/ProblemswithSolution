# test cases:
movies_list = ['Bala', 'Race', 'a', 'Pink',  'Black', 'n', 'New york']
start_date = ['1 jan', '7 jan', '16 jan', '17 jan',
              '02 feb', '1 feb', '14 feb']
end_date = ['14 jan', '19 jan', '04 feb', '01 feb ',
            '13 feb', '12 feb', '28 feb']
# solution
start_day = []
end_day = []


def date_into_day(sequence, new_sequence):
    for i in range(0, len(sequence)):
        x = sequence[i].split(' ')
        if x[1] == 'jan':
            day = int(x[0])
        if x[1] == 'feb':
            day = int(x[0])+31
        if x[1] == 'mar':
            day = int(x[0])+59
        if x[1] == 'apr':
            day = int(x[0])+90
        if x[1] == 'may':
            day = int(x[0])+120
        if x[1] == 'jun':
            day = int(x[0])+151
        if x[1] == 'jul':
            day = int(x[0])+181
        if x[1] == 'aug':
            day = int(x[0])+212
        if x[1] == 'sept':
            day = int(x[0])+243
        if x[1] == 'oct':
            day = int(x[0])+273
        if x[1] == 'nov':
            day = int(x[0])+304
        if x[1] == 'dec':
            day = int(x[0])+334
        new_sequence.append(day)


date_into_day(start_date, start_day)
date_into_day(end_date, end_day)

movies_dict = {}
for i in range(0, len(movies_list)):
    movies_dict[movies_list[i]] = [start_day[i], end_day[i]]
print(movies_dict)


def is_movie(m, n, list):
    if n == len(movies_list):
        return True
    if end_day[m] < start_day[n]:
        if (end_day[movies_list.index(list[-1])] < start_day[n]):
            list.append(movies_list[n])
        is_movie(m, n+1, list)


def movies_todo():
    movie_odd = []
    for i in range(0, len(movies_list)):
        one_list = []
        for j in range(i+1, len(movies_list)):
            all_list = []
            all_list.append(movies_list[i])
            is_movie(i, j, all_list)
            one_list.append(all_list)
        movie_odd += one_list

    longestList = max(movie_odd, key=lambda i: len(i))
    print("Sequence of movies:{}".format(longestList))
    print(f"Earnings:{len(longestList)} crores")


movies_todo()
