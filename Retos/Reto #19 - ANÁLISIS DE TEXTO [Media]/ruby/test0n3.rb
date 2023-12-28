# frozen_string_literal: true

# class TextAnalysis limited to process input with '.'
class TextAnalysis
  def initialize(text)
    @nro_sentences = text.length != text.count('.') ? text.count('.') : 0
    @text = text
  end

  def analyze
    words = @text.delete('.,;:?!').downcase.split(' ')
    words_count = 0
    sum_words_size = 0
    max_word = ''

    unless @nro_sentences.zero?
      words.each do |word|
        words_count += 1
        sum_words_size += word.length
        max_word = word if word.length > max_word.length
      end
    end

    { nro_words: words_count,
      words_mean_size: words_mean_size(sum_words_size, words_count),
      nro_sentences: @nro_sentences,
      longest_word: max_word }
  end

  def words_mean_size(sizes_total, words)
    return 0 if words.zero?

    sizes_total / words
  end
end
