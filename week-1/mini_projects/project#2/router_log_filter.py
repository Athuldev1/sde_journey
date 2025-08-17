def filter_logs(input_file, output_file, keywords):
    """Filter logs containing specific keywords and save to output_file."""
    with open(input_file, "r") as f, open(output_file, "w") as out:
        for line in f:
            if any(keyword in line for keyword in keywords):
                out.write(line)

filter_logs("router_logs.txt", "filtered_logs.txt", ["ERROR", "DOWN"])
# This code filters logs from "router_logs.txt" and saves lines containing "ERROR" or "DOWN" to "filtered_logs.txt".