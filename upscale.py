#!/usr/bin/env python3 
# waifu2x-converter-cpp -j 2 --scale_ratio 2.0 --noise_level 2 -m noise_scale -o mpv-shot0011.png -i mpv-shot0011.jpg
import subprocess, sys, os
null = open(os.devnull, "w")
infile = sys.argv[1]
outfile = ".".join(sys.argv[1].split(".")[:-1]) + "-waifu2x.png"
noise_level = False
if len(sys.argv) == 3:
    if sys.argv[2] in ["0", "1", "2"]:
        print("Assuming you don't want to write to a file named " + sys.argv[2])
        noise_level = int(sys.argv[2])
    else:
        outfile = sys.argv[2]
if len(sys.argv) > 3:
    noise_level = int(sys.argv[3])
if not noise_level or noise_level == 0:
    noise_level = ["-m", "scale"]
else:
    noise_level = ["-m", "noise_scale", "--noise_level", str(noise_level)]
args = ["waifu2x-converter-cpp", "-j", "2", *noise_level, "-o", outfile, "-i", infile]
print(" ".join(args))
try:
    subprocess.check_call(args, stdout=null)
except:
    print("Failed. Check your waifu2x installation")
    null.close()
    sys.exit(1)
null.close()
print("Written to " + outfile)
