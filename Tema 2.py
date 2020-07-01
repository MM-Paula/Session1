import textwrap
print(1)
def f():
    print('abc')
f()
def split_pairs(input):
    split = textwrap.wrap(input,2)

    if len(split[-1]) == 1:
        split[-1] += "_"
        return split

print(split_pairs('abcd'))
print(split_pairs('abc'))
print()

print(2)
def reverseWordSentence(Sentence):
    return ' '.join(word[::-1] for word in Sentence.split(" "))

Sentence = "This is an example!"
print(reverseWordSentence(Sentence))
Sentence = "double  spaces"
print(reverseWordSentence(Sentence))
print()

print(3)
class Human:
    pass
class Man(Human):
    pass
class Woman(Human):
    pass
def God():
    Adam = Man
    Eva = Woman
    return [Adam, Eva]




