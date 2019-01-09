# Submitter: ademerat(Demerath, Arthur)
# Partner  : ktiet1(Tiet, Khuong)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody
import prompt
from collections import defaultdict



def read_graph(file : open) -> {str:{str}}:
    return_dict = defaultdict(set)
    text = file.readlines()
    for item in text:
        return_dict[item[0]].add(item[2])
    return return_dict


def graph_as_str(graph : {str:{str}}) -> str:
    answer_string = ''
    for key, value in sorted(graph.items()):
        answer_string += '  {} -> {}\n'.format(key, sorted(value))
    return answer_string
    
    
def reachable(graph : {str:{str}}, start : str) -> {str}:
    graph = defaultdict(set, graph)
    return_set = set()
    search_list = list(start)
    while search_list != []:
        #for item in search_list:
        return_set.add(search_list[0])
        search_list.extend(list(graph[search_list[0]]))
        search_list.pop(0)
    return return_set
    
    
    
#temp_file = open('graph1.txt', 'r')
#print(reachable(read_graph(temp_file), 'a') == {'d', 'e', 'b', 'g', 'f', 'a', 'c'})
#temp_file.close()


if __name__ == '__main__':
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
