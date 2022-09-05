import argparse


def main():
    argparser = argparse.ArgumentParser(
        description="Extract the sequences from a simple-fastq file")
    argparser.add_argument(
        "fastq",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()

    fastq = ""
    with open(args.fastq.name, "r") as file:
        fastq = file.read()

    reads = fastq.split("@")
    #print(reads)
    for i in range(1, len(reads)):
        _, seq, _ = reads[i].split("\n")
        print(seq)

    #print(f"Now I need to process the records in {args.fastq}")


if __name__ == '__main__':
    main()
