def find_line_containing_string(mac_prefix):
    with open('data/manuf.txt', 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
        for line in lines:
            if mac_prefix in line:
                return line.strip()
    return None


def get_mac_vendor(mac_prefix):
    result_line = find_line_containing_string(mac_prefix)

    if result_line:
        shorted_name = result_line.split('\t')
        return shorted_name[2]
    else:
        return "--"
