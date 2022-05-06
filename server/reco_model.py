import sys
sys.path.append("./model/KoELECTRA/finetune/")
from model.KoELECTRA import finetune
from model.KoELECTRA.finetune import run_seq_cls


def to_txt(sentence: str):
    input_sentence = "0\t" + sentence + "\t0"
    with open("./model/KoELECTRA/finetune/data/nsmc/ratings_test.txt", "w") as f:
        f.write("id\tdocument\tlabel\n")
        f.write(input_sentence)

def recommand(sent: str):
    to_txt(sent)
    res = run_seq_cls.get_res()
    return res

if __name__=="__main__":
    print(__name__)
    recommand('좋은 아침입니다.')