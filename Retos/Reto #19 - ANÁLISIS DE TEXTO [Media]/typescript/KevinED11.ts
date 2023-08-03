

class AnalyzeText {
    text: string
    private _splitWords: string[]
    private _lenghtWords: number[]
    private _maxLenght: number

  constructor(text: string) {
    this.text = text
    this._splitWords = this.getSplitWords()
    this._lenghtWords = this.getLenghtWords()
    this._maxLenght = this.maxLenght()
  
   }

  private filterWords(text: string[]): string[] {
    return text.filter(Boolean)
      
    }

  private getSplitWords(): string[] {
     const words: string[] = this.text.split(" ")
     return this.filterWords(words)
      
    }
       

  private splitCharacters(): string[] {
    return this.text.split("")
    }

  private getLenghtWords(): number[] {
      return this.getSplitWords().map(word => word.length)
    }

  private maxLenght(): number {
    return Math.max(...this.getLenghtWords())
    }

  lenghtText(): number {
    return this.splitWords.length     
   }

  getAverageCharacters(): number {
    return this.getLenghtWords().reduce((acum, curr) => acum + curr, 0) / this.lenghtText()
      
    }

  getNumberOfSentences(): number {
    return this.splitCharacters().filter(char => char === ".").length

  }

  getLongestWord(): string[] {
    return this.splitWords.filter(word => word.length === this.maxLenght())     
   }

  public get splitWords(): string[] {
    return this._splitWords
  
   }

   public get LenghtWords(): number[] {
    return this._lenghtWords
     
   }

   public get MaxLenght(): number {
  return this._maxLenght
}
}



const main = () => {
  const analyze = new AnalyzeText("hola kevin dueñas dueñas .")
  console.log(analyze.lenghtText())
  console.log(analyze.getAverageCharacters())
  console.log(analyze.getLongestWord())
  console.log(analyze.splitWords)
  console.log(analyze.MaxLenght)
  console.log(analyze.getNumberOfSentences())
}
  

main()