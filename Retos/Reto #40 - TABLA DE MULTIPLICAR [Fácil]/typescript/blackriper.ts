
// metodos de trabajo 
interface Table {
  read_number(num: number): void
  print_table(): void
}
// implementar metodos de trabajo
class MultiplicationTables implements Table {

  private nu: number

  read_number(num: number): void {
    this.nu = num
  }
  print_table(): void {
    for (let n = 1; n <= 10; n++) {
      console.log(`${this.nu} x ${n}= ${this.nu * n}`)
    }
  }

}

const multtab = new MultiplicationTables()
multtab.read_number(5)
multtab.print_table()


