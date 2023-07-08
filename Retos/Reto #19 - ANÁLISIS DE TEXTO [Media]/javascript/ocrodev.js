function textAnalysis(paragraph) {
  const words = paragraph.split(/[\s+]/)

  //? total de palabras
  const total_words = words.length 
  
  //? Longitud media de las palabras
  let length_acum = 0
  function searchAverageLength(wordArray, length) {
    if (length < 0) return 
    length_acum += wordArray[length].length
    searchAverageLength(wordArray, length-1)
  }
  searchAverageLength(words, words.length - 1)
  let average = length_acum / total_words
  
  //? total de oraciones
  const sentences = paragraph.split('.').length
  
  //? palabra mas larga  
  let largestWord = 0
  let largestWordString;
  function searchLargestWord(wordArray, length, largest) {  
    if (length < 0) return 
    largest = wordArray[length].length
    if (largest > largestWord) {
      largestWord = largest
      largestWordString = wordArray[length]
    }
    searchLargestWord(wordArray, length-1, largestWord)
  }
  searchLargestWord(words, words.length - 1, 0)

  
  return console.log( {
    words,
    total_words,
    average,
    total_entences:sentences,
    largest_word_characteres: largestWord,
    largest_word_string: largestWordString
  } )
}

const lorem = 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Iste velit iusto cum voluptate molestiae! Possimus, dicta? Dolores accusamus id aliquid incidunt maiores? Numquam dolores ipsa voluptas ipsum quis architecto doloremque!'

textAnalysis(lorem); 


