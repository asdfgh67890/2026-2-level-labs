"""
BPE Tokenizer starter
"""

from lab_2_tokenize_by_bpe.main import (
    collect_frequencies,
    count_tokens_pairs,
    decode,
    get_vocabulary,
    merge_tokens,
    prepare_word,
    train,
)

# pylint:disable=too-many-locals, unused-variable


def main() -> None:
    """
    Launches an implementation
    """
    with open("lab_2_tokenize_by_bpe/assets/text.txt", "r", encoding="utf-8") as text_file:
        text = text_file.read()
    with open("lab_2_tokenize_by_bpe/assets/en_raw.txt", "r", encoding="utf-8") as text_file:
        text_reference_translation = text_file.read()
    with open("lab_2_tokenize_by_bpe/assets/en_encoded.txt", "r", encoding="utf-8") as text_file:
        translation_encoded_raw = text_file.read()

    print(prepare_word("farther", None, "</s>"))

    freqs = collect_frequencies(text, None, "</s>")
    if freqs is None:
        return

    pairs = count_tokens_pairs(freqs)
    if pairs is None:
        return

    merged = merge_tokens(freqs, list(pairs.keys())[0])
    if merged is None:
        return

    trained = train(freqs, 100)
    if trained is None:
        return

    vocab = get_vocabulary(trained, "<unk>")
    if vocab is None:
        return

    test_vocab = {"<unk>": 0, "</s>": 1, "far": 2, "th": 3, "est": 4}
    test_encoded = [2, 3, 4, 1]

    decoded_text = decode(test_encoded, test_vocab, "</s>")
    if decoded_text is None:
        return

    result = decoded_text

    print(f"Decoded: {result}")

    assert result, "Translation not working"


if __name__ == "__main__":
    main()
