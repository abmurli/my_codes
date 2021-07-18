A = "12:16"
B = "12:45"

beg_hr = str(A).split(":")[0]
beg_min = str(A).split(":")[1]
if beg_min[0] == "0":
    beg_min = beg_min[1]
rounds = 0
end_hr = str(B).split(":")[0]
end_min = str(B).split(":")[1]
set_min_min = 0
set_max_min = 0


def round_cal(set_min_min, set_max_min):
    if beg_hr == end_hr:
        count = 0
        min_diff = set_max_min - set_min_min
        if min_diff - 15 == 0:
            print("")
        while(min_diff != 0):
            min_diff = min_diff - 15
            count+=1
    print(f"round: {count}")


def get_min_max_hr(beg_hr, end_hr):
    hr_diff = int(end_hr) - int(beg_hr)
    return hr_diff


def get_min_max_min(beg_min, end_min):

    if int(beg_min) == 0:
        set_min_min = 0
    elif int(beg_min) <= 15:
        set_min_min = 15
    elif int(beg_min) <= 30:
        set_min_min = 30
    elif int(beg_min) <= 45:
        set_min_min = 45
    if int(end_min) <= 15:
        set_max_min = 0
    elif int(end_min) <= 30:
        set_max_min = 15
    elif int(end_min) <= 45:
        set_max_min = 30

    return set_min_min, set_max_min


def solution(A,B):
    if beg_hr == end_hr:
        set_min_min, set_max_min = get_min_max_min(beg_min, end_min)
        round_cal(set_min_min, set_max_min)
    else:
        if int(beg_hr) > int(end_hr):
            set_min_min, set_max_min = get_min_max_min(beg_min, end_min)
            diff_in_hours = get_min_max_hr(beg_hr, end_hr)
            total_count = int(diff_in_hours*4)
            print(total_count)

        else:
            set_min_min, set_max_min = get_min_max_min(beg_min, end_min)

solution(A,B)

