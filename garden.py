import spacy

nlp = spacy.load('en_core_web_sm')

gardenpathSentences = [
    "After the young Londoner had visited his parents prepared to celebrate their anniversary",
    "I told the girl the cat scratched Bill would help her.",
    "I know the words to that song about the queen don’t rhyme.",
    "When John called his old mother was happy.",
    "The cotton clothes are made of grows in Mississippi."
]


for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("Sentence:", sentence)
    for entity in doc.ents:
        print([(i, i.label_, i.label) for i in doc.ents])
    print("\n")


# Actually, I don't see any surprising entities that were recognised but what I didn't expect is that it will
# recognise nothing in some sentences. Probably because these are Garden Path sentences that are difficult to parse.



