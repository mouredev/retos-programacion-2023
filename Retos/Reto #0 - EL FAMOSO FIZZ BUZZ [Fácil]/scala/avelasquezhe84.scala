// Scala 3

@main def fizzbuzz() =
    (1 to 100).foreach(i => 
        if i % 15 == 0 then println("fizzbuzz")
        else if i % 3 == 0 then println("fizz")
        else if i % 5 == 0 then println("buzz")
        else println(i)
    )
