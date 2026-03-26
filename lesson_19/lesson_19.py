from datetime import datetime

KEY = "Key TSTFEED0300|7E3E|0400"

def analyze_heartbeat(input_file, output_file):
    # read file
    with open(input_file) as f:
        lines = f.readlines()

    # filtered by KEY
    filtered = []
    for line in lines:
        if KEY in line:
            filtered.append(line)

    # get timestamps Timestamp 05:45:40 Key
    times = []
    for line in filtered:
        if "Timestamp " in line:
            # e.g. '05:45:40'
            t = line.split("Timestamp ")[1][:8]
            times.append(datetime.strptime(t, "%H:%M:%S"))

    # main logic
    with open(output_file, "w") as out:
        for i in range(len(times) - 1):
            diff = abs((times[i] - times[i+1]).total_seconds())

            if 31 < diff < 33:
                out.write(f"WARNING {times[i].time()} diff={diff}\n")
            elif diff >= 33:
                out.write(f"ERROR {times[i].time()} diff={diff}\n")

analyze_heartbeat("hblog.txt", "hb_test.log")















with open("hblog.txt") as f:
    lines = f.readlines()


filtered = []

for line in lines:
    if KEY in line:
        filtered.append(line)

# get timestamps Timestamp 05:45:40 Key
times = []
for line in filtered:
    if "Timestamp " in line:
        # e.g. '05:45:40'
        t = line.split("Timestamp ")[1][:8]
        times.append(datetime.strptime(t, "%H:%M:%S"))

# main logic
with open("hb_test.log", "w") as out:
    for i in range(len(times) - 1):
        diff = abs((times[i] - times[i+1]).total_seconds())

        if 31 < diff < 33:
            out.write(f"WARNING {times[i].time()} diff={diff}\n")
        elif diff >= 33:
            out.write(f"ERROR {times[i].time()} diff={diff}\n")