import os
import time

import inspect

from matplotlib import pyplot as plt
from pandas.compat import numpy
from twisted.python import filepath

from SudokuGeneticAlgorithm import profile
from SudokuGeneticAlgorithm.profile import format_bytes
from SudokuGeneticAlgorithm.sudoku import Sudoku


def get_file_path(filepath):
    #get the txt file path under simple package
    path_list = []
    for file in os.listdir(filepath):
        if file.endswith(".txt"):
            path_list.append(os.path.join(filepath, file))
    return path_list

def get_puzzle():
    simple_path = "/Users/congqinyan/TCD LECTURES/semester two/AI/team-project/AI_TEAM_PROJECT/SudokuGeneticAlgorithm/simple"
    medium_path = "/Users/congqinyan/TCD LECTURES/semester two/AI/team-project/AI_TEAM_PROJECT/SudokuGeneticAlgorithm/medium"
    hard_path = "/Users/congqinyan/TCD LECTURES/semester two/AI/team-project/AI_TEAM_PROJECT/SudokuGeneticAlgorithm/hard"
    simple_list = get_file_path(simple_path)
    medium_list = get_file_path(medium_path)
    hard_list = get_file_path(hard_path)
    return simple_list, medium_list, hard_list
def get_simple_result(file_list):
    results = []
    rss_list = []
    vms_list = []
    for i in range(0,10):
        simple_list[i]
        rss_before, vms_before = profile.get_process_memory()
        s = Sudoku(200, 140, 1500)
        s.load(simple_list[i])
        start = time.time()
        s.solve()
        end = time.time()
        rss_after, vms_after = profile.get_process_memory()
        elapsed_time = profile.elapsed_since(start)
        print("Time: ", end - start)
        print("RSS: {:>8} | VMS: {:>8} | time: {:>8}"
              .format(
                      format_bytes(rss_after - rss_before),
                      format_bytes(vms_after - vms_before),
                      elapsed_time))
        results.append(end-start)
        rss_list.append(format_bytes(rss_after - rss_before))
        vms_list.append(format_bytes(vms_after - vms_before))
    return results, rss_list, vms_list

simple_list, medium_list, hard_list = get_puzzle()
get_simple_result(medium_list)
profile.get_process_memory()
print(get_simple_result(medium_list))
# hard_time = [7.559381008148193, 35.28113412857056, 57.57910108566284, 34.4009952545166, 11.411736965179443, 17.377499103546143, 29.255064010620117, 10.807416915893555, 38.93790411949158, 12.353085994720459]
# hard_rss = ['1.1MB', '290.82kB', '204.8kB', '86.02kB', '0B', '8.19kB', '0B', '0B', '4.1kB', '0B']
# hard_vms = ['1.31MB', '0B', '0B', '0B', '0B', '0B', '0B', '0B', '0B', '0B']
#
# simple_time = [10.47505497932434, 10.384736061096191, 66.9694173336029, 48.402596950531006, 23.384976863861084, 10.330721855163574, 18.659949779510498, 8.816908121109009, 36.289777755737305, 11.36506700515747]
# simple_rss = ['1.43MB', '94.21kB', '135.17kB', '12.29kB', '0B', '8.19kB', '0B', '4.1kB', '12.29kB', '0B']
# simple_vms = ['1.31MB', '0B', '0B', '0B', '0B', '0B', '0B', '0B', '0B', '0B']
#
# medium_time = [42.24830985069275, 77.35509920120239, 12.567631006240845, 57.34943675994873, 10.936491012573242, 11.946233034133911, 76.28027129173279, 9.657665967941284, 63.34622001647949, 14.077000856399536]
# medium_rss = ['1.59MB', '122.88kB', '0B', '24.58kB', '4.1kB', '0B', '20.48kB', '0B', '0B', '4.1kB']
# medium_vms = ['9.7MB', '0B', '0B', '0B', '0B', '0B', '0B', '0B', '0B', '0B']


