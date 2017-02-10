import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-i", nargs="?")
parser.add_argument("-o", nargs="?")
args = parser.parse_args()

with open(args.i, "r") as ifile, open(args.o, "w") as ofile:
    print("{\n\t\"conversations\": [", file=ofile)
    index = 0
    for line in ifile:
        index += 1
        line = line.strip().replace('\\', '\\\\').replace('"', '\\"')
        if index % 2 == 1:
            if index != 1:
                ofile.write(",\n")
            ofile.write("\t\t[\n\t\t\t\"{}\",\n".format(line))
        else:
            ofile.write("\t\t\t\"{}\"\n\t\t]".format(line))
    print("\n\t]\n}", file=ofile)
