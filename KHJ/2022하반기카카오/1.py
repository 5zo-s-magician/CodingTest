def solution(today, terms, privacies):
    answer = []
    today = list(map(int, today.split(".")))
    
    terms_dic = {}
    for term in terms:
        _term = term.split(" ")
        terms_dic[_term[0]] = int(_term[1])

    for i, privacy in enumerate(privacies):
        date, term = privacy.split(" ")
        date = list(map(int, date.split(".")))
        if isDueEnd(today, date, terms_dic[term]):
            answer.append(i+1)
    
    return answer


def isDueEnd(today, comp, limit):
    div, mod = divmod(comp[1] + limit, 12)
    due = [comp[0]+div, mod, comp[2]-1]
    if due[2] == 0:
        due[2] = 28
        due[1] -= 1
    if due[1] < 1:
        due[1] = 12+due[1]
        due[0] -= 1


    
    for i in range(3):
        if due[i] < today[i]:
            return True
        elif due[i] > today[i]:
            return False
    return False






# today = "2022.05.19"
# terms = ["A 6", "B 12", "C 3"]
# privacies = ["2021.06.01 A", "2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]


today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

solution(today, terms, privacies)