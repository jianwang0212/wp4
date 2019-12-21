import pandas as pd
from nltk.tokensize.punkt import PunktSentenceTokenizer, PunktParameters
tokenizer = PunktSentenceTokenizer()
df = pd.read_csv('batch3_no_eduction_no_health_1.csv')
df = df.dropna(subset=['JobText'])
ads = df.JobText.tolist()
token = 0
while True:
    print('>>>>>>>>>>>>>>>>>>>>>> START <<<<<<<<<<<<<<<<<<<<<<<<')
    import textwrap
    wrapper = textwrap.TextWrapper(replace_whitespace=False)
    for l in ads.pop().splitlines():
        # print(len(l))
        tokenizer.train(l)
        if len(l)<67:
            # print(token, len(l.split()))
            if len(l.split()) == 0 and token == 0:
                token = 1
                print((textwrap.dedent(l)))
            elif len(l.split()) == 0 and token == 1:
                continue
            else:
                token = 0
                print((textwrap.dedent(l)))
        else:
            lines = wrapper.wrap(l)
            for line in lines:
                print((textwrap.dedent(line)))

    print('>>>>>>>>>>>>>>>>>>>>>>> END <<<<<<<<<<<<<<<<<<<<<<<<<')
    input("Press Enter to continue...")

import textwrap
def test():
    # end first line with \ to avoid the empty line!
    s = '''\
    hello
      world
    '''
    print((s))          # prints '    hello\n      world\n    '
    print((textwrap.dedent(s)))  # prints 'hello\n  world\n'