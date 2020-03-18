import sys

# 1. Argument check
if(len(sys.argv) - 1 == 2 ): # input file path, output file path
    
    try:
        fi = open(sys.argv[1], "r")
        fo = open(sys.argv[2], "w")
    
    except: # Failed to read the input file
        print("Wrong arugments.")
        exit(0)
    

else: # User have to specify both an input file and an output file
    print("Argument format: python3 grapy.py [input file (log file)] [output file]")
    exit(0)

# 2. Read Input Log File

# flag turn on when Compaction stats line is read and turn off when Compaction stats line is not read.
flag = False

# last_flag has last status of flag
last_flag = True

uptime = ""



while (True):

    # Read one line
    line = fi.readline()

    if ("Uptime(secs)" in line):

        # Get uptime log
        # uptime = float(line.split(" ")[1])
        uptime = (line.split(" ")[1])
        # print("UPTIME " + uptime)

    if not line: #EOF
        print("Done.")
        exit(0)

    if ("** Compaction Stats [usertable] **" in line): 
        
        # Already read the same compaction stats
        if(last_flag):
            flag = False
        
        # First time to read this compaction stats
        else:
            flag = True


    
    if ("** File Read Latency Histogram By Level [usertable] **" in line):
        last_flag = flag
        flag = False

    if flag: # Compaction stats line is being reading.
        
        # fo.write(line)

        # Get rows in a table
        if ("Level" in line):
            fi.readline() # Read a dummy line before a table
            
            comp_row = uptime
            # print(uptime)

            for i in range(4): # L0 L1 L2 L3s
                row = fi.readline()
                # print(row)
                row_splited = (' '.join(row.split())).split(' ')
                # print(row_splited)
                # fo.write(row_splited[0] + " -> " + row_splited[14]+"\n")
                comp_row += " "+row_splited[19]

            comp_row += '\n'
            
            # fo.write(comp_row)

        if ("Flush" in line):
            flush = uptime + " " + (line.split(" ")[2]).split(",")[0] + '\n'
            fo.write(flush)

fi.close()
fo.close()