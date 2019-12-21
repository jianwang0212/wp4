import pandas as pd
import textwrap
import re
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
tokenizer = PunktSentenceTokenizer()
df = pd.read_csv('batch3_no_eduction_no_health_1.csv')
df = df.dropna(subset=['JobText'])
ads = df.JobText.tolist()
token = 0

list_sentences = []
list_categories = []

while True:

    print('\n >>>>>>>>>>>>>>>>>>>>>> START <<<<<<<<<<<<<<<<<<<<<<<< \n')

    wrapper = textwrap.TextWrapper(replace_whitespace=False)
    for l in ads.pop().splitlines():
        # print(len(l))
        tokenizer.train(l)
        out = (tokenizer.tokenize(l))
        for e in out:
            e = e.lower()
            months = re.compile("(\s+jan\s+)|(\s+feb\s+)|(\s+mar\s+)|\
                        (\s+apr\s+)| \
                        (\s+may\s+)|(\s+jun\s+)|(\s+jul\s+)|(\s+aug\s+)| \
                        (\s+sep\s+)|(\s+sept\s+)|(\s+oct\s+)\|(\s+nov\s+)| \
                        (\s+dec\s+)|(\s+january\s+)|(\s+february\s+)|\
                        (\s+march\s+)|\
                        (\s+april\s+)|(\s+may\s+)|(\s+june\s+)|(\s+july\s+)|\
                        (\s+august\s+)|(\s+september\s+)|(\s+october\s+)| \
                        (\s+november\s+)|(\s+december\s+)")
            numbers = re.compile("(\d+,\d+)| (\s+\d+\s+)|(\s+\d+\s+)|(\d+)|\
                                  (\d+th)| \
                                  (\d+am)|(\d+pm)|(\d+)")   
            numbers_pa = re.compile("(\d+pa) | (\d+\s+pa)")
            e = e.split(' ')
            e = [months.sub(" mtkn ", line) for line in e]
            e = [numbers.sub(" ntkn ", line) for line in e]
            e = [numbers_pa.sub(" ntkn ", line) for line in e]
            e = [re.sub(' +', ' ', line) for line in e]
            e = ' '.join(e)
            print('\n', textwrap.dedent(e))
            print('')
            while True:
                response = str(input("Does this passage contain information about ZHC? (y/n): "))
            #input("Press Enter to continue...")

                if response == 'y':
                    list_sentences.append(e)
                    list_categories.append('y')
                    break

                if response == 'n':
                    list_sentences.append(e)
                    list_categories.append('n')
                    break

                if response == 's':
                    df = pd.DataFrame({'sentences': list_sentences,
                                       'categories': list_categories})
                    df.to_csv('191126tags.csv')
                    print('Your inputs have been saved.')
                    exit()

            

    print('\n >>>>>>>>>>>>>>>>>>>>>>> END <<<<<<<<<<<<<<<<<<<<<<<<< \n')



import textwrap
def test():
    # end first line with \ to avoid the empty line!
    s = '''\
    hello
      world
    '''
    print((s))          # prints '    hello\n      world\n    '
    print((textwrap.dedent(s)))  # prints 'hello\n  world\n'