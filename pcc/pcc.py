import sys


def main():
    source_path = sys.argv[1]
    with open(source_path) as f:
        source = f.readline()
    print(".intel_syntax noprefix")
    print(".globl main")
    print("main:")
    print("  mov rax, ", int(source))
    print("  ret")


if __name__ == '__main__':
    main()
