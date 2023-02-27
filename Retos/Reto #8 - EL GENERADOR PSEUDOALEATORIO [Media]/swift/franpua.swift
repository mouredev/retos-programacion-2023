func randomNumbers() {
    
    let a = 123456789
    let c = 987654321
    let m = 101
    let semilla = Int(round(Date().timeIntervalSince1970 + 1000))
    
    let numeroSeudoAleatorio = (semilla * a + c ) % m
    
    print(numeroSeudoAleatorio)
}
for _ in 0..<10 {
    randomNumbers()
    Thread.sleep(forTimeInterval: 1.0)
}