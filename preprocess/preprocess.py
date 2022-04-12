import kss
import re

def split_sentence(text: str) -> list:
    """
    텍스트를 입력하면 문장 단위로 끊어서 리스트 형태로 반환합니다.
    kss의 split_sentences를 이용합니다.
    """
    sentence_tokenized_text = []
    text = text.strip()
    for sent in kss.split_sentences(text):
        sentence_tokenized_text.append(sent.strip())
    return sentence_tokenized_text

def clean_punc(text: str) -> str:
    """
    특수문자를 제거하고, 이외의 다른 문자들을 제거한 후 str형태로 반환합니다.
    """
    punct = "/-'?!.,#$%\'()*+-/:;<=>@[\\]^_`{|}~" + '""“”’' + '∞θ÷α•à−β∅³π‘₹´°£€\×™√²—–&'
    mapping = {"‘": "'", "₹": "e", "´": "'", "°": "", 
                "€": "e", "™": "tm", "√": " sqrt ", "×": "x", 
                "²": "2", "—": "-", "–": "-", "’": "'", "_": "-", 
                "`": "'", '“': '"', '”': '"', '“': '"', "£": "e", 
                '∞': 'infinity', 'θ': 'theta', '÷': '/', 'α': 'alpha', 
                '•': '.', 'à': 'a', '−': '-', 'β': 'beta', '∅': '', 
                '³': '3', 'π': 'pi', }
    
    for p in mapping:
        text = text.replace(p, mapping[p])
    
    for p in punct:
        text = text.replace(p, f' {p} ')
    
    specials = {'\u200b': ' ', '…': ' ... ', '\ufeff': '', 'करना': '', 'है': ''}
    for s in specials:
        text = text.replace(s, specials[s])
    
    return text.strip()

def clean_text(text: str) -> str:
    """
    텍스트를 입력하면 여백과 태그를 제거합니다.
    """
    
    text = str(text[i])
    # review = re.sub(r'\d+','', str(texts[i]))# 숫자 제거
    # review = review.lower() # 소문자
    text = re.sub(r'<[^>]+>','',text) # HTML 태그 제거
    text = re.sub(r'\s+', ' ', text) # 두 칸 이상 여백 제거
    text = re.sub(r"^\s+", '', text) # 시작 여백 제거
    text = re.sub(r'\s+$', '', text) # 마지막 여백 제거
    
    return text