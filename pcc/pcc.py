import sys


def num(source):
    print("  push", int(source))


def mul(source):
    # 一番最後に出てくる*/を取り出す
    last_mul_index = max(
        len(source) - len(source.split("*")[-1]),
        len(source) - len(source.split("/")[-1])
    ) - 1
    if last_mul_index == -1:
        # */が見つからなかったらnumの処理を行う
        num(source)
        return

    left_source = source[:last_mul_index]
    right_source = source[last_mul_index + 1:]
    op = source[last_mul_index]
    mul(left_source)
    mul(right_source)
    print("  pop rdi")
    print("  pop rax")
    if op == "*":
        print("  mul rdi")
    else:
        print("  div rdi")
    print("  push rax")


def expr(source):
    # 一番最後に出てくる+-を取り出す
    last_adder_index = max(
        len(source) - len(source.split("+")[-1]),
        len(source) - len(source.split("-")[-1])
    ) - 1
    if last_adder_index == -1:
        # +-が見つからなかったら*/の処理を行う
        mul(source)
        return

    left_source = source[:last_adder_index]
    right_source = source[last_adder_index + 1:]
    op = source[last_adder_index]
    expr(left_source)
    expr(right_source)
    print("  pop rdi")
    print("  pop rax")
    if op == "+":
        print("  add rax, rdi")
    else:
        print("  sub rax, rdi")
    print("  push rax")


def main():
    source_path = sys.argv[1]
    with open(source_path) as f:
        source = f.readline()
    print(".intel_syntax noprefix")
    print(".globl main")

    print("main:")
    expr(source)
    print("  pop rax")
    print("  ret")


if __name__ == '__main__':
    main()
