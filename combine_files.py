import nltk

filenames = [
    "246.txt",
    "276.txt",
    "286.txt",
    "344.txt",
    "372.txt",
    "383.txt",
    "388.txt",
    "392.txt",
    "556.txt",
    "665.txt"
]
with open("result.csv", "w") as f:
    for index, filename in enumerate(filenames):
        f.write(nltk.corpus.gutenberg.raw(filename))
        if index != (len(filenames) - 1):
            f.write(",")
