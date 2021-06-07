import os

def merge_stats(stat1, stat2):
    result = {}
    key = 100
    for i in range(4):
        number = stat1[key][0] + stat2[key][0]
        extensions = list(
            set.union(
                set(
                    stat1[key][1]
                ),
                set(
                    stat2[key][1]
                )
            )
        )
        result.update({key: (number, extensions)})
    return result

def recursive_bypass(path):
    stats = {
        100: (0, []),
        1000: (0, []),
        10000: (0, []),
        100000: (0, []),
    }

    for obj in os.listdir(path):
        cur_path = os.path.join(path, obj)
        if os.path.isdir(cur_path):
            stats = merge_stats(recursive_bypass(cur_path), stats)
        else:
            size = os.stat(cur_path).st_size
            exten = os.path.splitext(os.path.basename(cur_path))[1]
            if size <= 100:
                key = 100
            elif size <= 1000:
                key = 1000
            elif size <= 10000:
                key = 10000
            else:
                key = 100000
            new_data = stats[key][0] + 1
            new_list = stats[key][1]
            if not exten in new_list:
                new_list.append(exten)
            stats.update({key: (new_data, new_list)})
    return stats

print(recursive_bypass('my_project'))