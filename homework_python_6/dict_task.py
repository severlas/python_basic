n_world: int
dict_ = {}
text_input = (input('Введите текст: \n')).split(' ')
for n_world in text_input:
    dict_[n_world] = dict_.get(n_world, 0)+1
print(dict_)
