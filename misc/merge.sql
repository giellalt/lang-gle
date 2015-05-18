SELECT DISTINCT
    definitions.gle_words,
    definitions.gle_annotation_in_eng,
    definitions.eng,
    definitions.eng_pos,
    definitions.eng_annotation_in_eng,
    semantics.gle_semantics,
    semantics.gle_pos,
    semantics.eng_desc,
    semantics.gle_desc
FROM ./wordnet.tsv definitions JOIN ./wordnet.ga.tsv semantics ON (definitions.gle_words = semantics.gle_words)
