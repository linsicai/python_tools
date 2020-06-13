import os

# 遍历指定目录文件
def iter_dir_file_path(dir):
    for root, dir_list, file_list in os.walk(dir):
        for file_name in file_list:
            path = os.path.join(root, file_name)
            if root.find("Thumb") > 0:
                continue

            yield path

# 取文件头几位
def get_head(n):
    heads = []
    with open(path, 'rb') as inf:
        for line in inf:
            for i, src in enumerate(line):
                if i >= n:
                    return heads
                heads.append(int(src))

# 计算魔术
def calc_magic_char(heads):
    a = heads[0] ^ 0xFF
    b = heads[1] ^ 0xD8
    if a == b:
        return True, a

    return False, None

def dat_to_image(path, out_dir):
    png_path = os.path.join(out_dir, os.path.basename(path) + ".png")

    # 自动计算魔术
    heads = get_head(2)
    if len(heads) != 2:
        print("bad dat file, path = {}".format(path))
        return
    succ, magic = calc_magic_char(heads)
    if not succ:
        print("parse fail, path = {}".format(path))
        return
    print("magic = {}".format(magic))

    with open(png_path, 'wb') as outf:
        with open(path, 'rb') as inf:
            for line in inf:
                for src in line:
                    dst = src ^ magic
                    outf.write(bytes([dst]))

in_dir = "Image"
out_dir = "Out"
paths = iter_dir_file_path(in_dir)
for i, path in enumerate(paths):
    if i % 100 == 0:
        print("#{}, path = {}".format(i, path))

    dat_to_image(path, out_dir)