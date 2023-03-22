from ekphrasis.classes.preprocessor import TextPreProcessor
from ekphrasis.classes.tokenizer import SocialTokenizer
from ekphrasis.dicts.emoticons import emoticons
import re

text_processor = TextPreProcessor(
    # terms that will be normalized
    normalize=['url', 'email', 'percent', 'money', 'phone', 'user',
        'time', 'url', 'date', 'number'],
    # terms that will be annotated
    annotate={"hashtag", "allcaps", "elongated", "repeated",
        'emphasis', 'censored'},
    fix_html=True,  # fix HTML tokens
    
    # corpus from which the word statistics are going to be used 
    # for word segmentation 
    segmenter="twitter", 
    
    # corpus from which the word statistics are going to be used 
    # for spell correction
    corrector="twitter", 
    
    unpack_hashtags=True,  # perform word segmentation on hashtags
    unpack_contractions=True,  # Unpack contractions (can't -> can not)
    spell_correct_elong=False,  # spell correction for elongated words
    
    # select a tokenizer. You can use SocialTokenizer, or pass your own
    # the tokenizer, should take as input a string and return a list of tokens
    tokenizer=SocialTokenizer(lowercase=True).tokenize,
    
    # list of dictionaries, for replacing tokens extracted from the text,
    # with other expressions. You can pass more than one dictionaries.
    dicts=[emoticons]
)

img_1 = re.compile('!\[(.*)\]\(.*\)')
link_1 = re.compile('\[(.*)\]\(.*\)')
link_2 = re.compile('\[(.*)\]: [^\s]+')
code_1 = re.compile('(:?`[^`]+`|```[^`]*```)')

def preprocess(title, body):
  doc = title + " " + body
  return clean_text(doc)

def clean_text(text):
  cleaned = re.sub(img_1, r'\1 <img>', text)
  cleaned = re.sub(link_1, r'\1 <url>', cleaned)
  cleaned = re.sub(link_2, r'\1 <url>', cleaned)
  cleaned = re.sub(code_1, '<code>', cleaned)
  ekph_cleaned = " ".join(text_processor.pre_process_doc(cleaned))
  return ekph_cleaned
