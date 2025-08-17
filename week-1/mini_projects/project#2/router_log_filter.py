# Open the router log file
with open("router_logs.txt", "r") as f:
    # Read the log file and filter for error lines
    for line in f:
        if "ERROR" in line:
           # Save the error line to a file
           with open("error_logs.txt", "a") as error_file:
                error_file.write(line)
