# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

it_companies.add("Twitter")
it_companies.remove("Twitter")
it_companies
C= A.union(B)
C
A.issubset(B)
B.issubset(A)
A.isdisjoint(B)
B.isdisjoint(A)
age_set = set(age)
age_set
age
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.lower().split()
unique_words = set(words)

print(unique_words)
print("Number of unique words:", len(unique_words))