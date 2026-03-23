# filename = "/Volumes/My Shared Files/shared/thispc_host/data_analytics/chaya_mar_26/tutorial_9_handling/details.txt"
filename = "details.txt"

with open(filename) as obj:
    print("file is openned")
    # print(obj.readlines())
    for line in obj.readlines():
        print(line,end="")
    print()