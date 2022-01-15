def solution(id_list, report, k):
    report_dic = {}
    report_num_dic = {}
    report_id = []
    answer = []
    
    for i in id_list:  
        report_dic[i] = []
        report_num_dic[i] = 0
        answer.append(0)
        
    for i in report:
        tmp = i.split(' ')
        report_dic[tmp[0]].append(tmp[1])
    
    for i in id_list:
        report_set = set(report_dic[i])
        report_dic[i] = list(report_set)
    
    for i in id_list:
        for j in report_dic[i]:
            report_num_dic[j] += 1
    
    for i in id_list:
        if report_num_dic[i] >= k:
            report_id.append(i)
            
    for i in range(0, len(id_list)):
        for j in report_dic[id_list[i]]:
            if(j in report_id):
                answer[i] += 1
    
    return answer