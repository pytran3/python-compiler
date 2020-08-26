import sys


def add(x):
    print("  add rax,", int(x))


def sub(x):
    print("  sub rax,", int(x))


def is_number_char(c):
    return ord('0') <= ord(c) <= ord("9")


def fetch_number(s):
    right = 0
    while right < len(s) and is_number_char(s[right]):
        right += 1
    if right == 0:
        raise Exception("予期せぬ文字から始まりました。: {}".format(s))
    return int(s[:right]), right  # 読み込んだ整数、読み込んだ文字数


def main():
    source_path = sys.argv[1]
    with open(source_path) as f:
        source = f.readline()
    print(".intel_syntax noprefix")
    print(".globl main")

    print("main:")
    number, index = fetch_number(source)
    print("  mov rax,", number)
    while index < len(source):
        # operatorをfetch
        if source[index] == "+":
            op = add
        elif source[index] == "-":
            op = sub
        else:
            raise Exception("予期せぬ文字から始まりました。: {}".format(source[index:]))
        index += 1
        # 数をfetch
        number, length = fetch_number(source[index:])
        index += length
        # 対応するアセンブリコードの出力
        op(number)

    print("  ret")


if __name__ == '__main__':
    main()
