import os
import math

# Byte order: little/big endian.
bo = "little"

def extract_depth_data(inpath, outpath):
    with open(inpath, "rb") as f:
        nframes = int.from_bytes(f.read(4), bo)
        ncols = int.from_bytes(f.read(4), bo)
        nrows = int.from_bytes(f.read(4), bo)

        with open(outpath, "w") as g:
            g.write(str(nframes) + ',' + str(nrows) + ',' + str(ncols) + '\n')
            
            for frameId in range(nframes):
                for i in range(nrows):
                    # Read and write depth data.
                    for j in range(ncols):
                        if j != 0:
                            g.write(',')
                        g.write(str(int.from_bytes(f.read(4), bo)))
                    g.write('\n')

                    # Simply skip Kinect skeleton data.
                    f.read(ncols)

def main():
    inpath = "../data/a04_s01_e01_depth.bin"
    outpath = "../output/raw_depth.txt"
    extract_depth_data(inpath, outpath)

if __name__ == "__main__":
    main()