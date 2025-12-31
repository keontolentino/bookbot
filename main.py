from stats import count_char
from stats import count_words
from stats import sort_count
import sys

def main():
    print("Usage: python3 main.py <path_to_book>")
    cnt_chr = count_char(sys.argv[1])
    count_words(sys.argv[1])
    srt_cnt = sort_count(cnt_chr)
    for dct in srt_cnt:
            print(f"{dct['char']}: {dct['num']} ")

main()