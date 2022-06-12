import pickle
name = ["mohit", "bhaskar", "manish"]
skill = ["Python", "Python", "Java"]
dict1 = dict([(k,v) for k,v in zip(name, skill)])
with open("files/programming_powers.pkl", "wb") as p_file:
    pickle.dump(name, p_file)
    pickle.dump(skill, p_file)
    pickle.dump(dict1, p_file)