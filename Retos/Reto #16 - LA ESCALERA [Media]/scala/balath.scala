def drawStairs(n: Int): Unit = n match {
  case 0          => println("__")
  case n if n > 0 => upstairs(n)
  case _          => downstairs(-n)
}

val upstairs = (n: Int) => for {
  blanksLength <- (n * 2 to 0 by -2)
  step = if (blanksLength == n * 2) "_" else "_|"
} println(s"${" " * blanksLength}$step")

val downstairs = (n: Int) => for {
  blanksLength <- (0 to n * 2 by 2)
  step = if (blanksLength == 0) "_" else "|_"
} println(s"${" " * (blanksLength - 1)}$step")

drawStairs(-6)
drawStairs(0)
drawStairs(6)

// _
//  |_
//    |_
//      |_
//        |_
//          |_
//            |_
// __
//             _
//           _|
//         _|
//       _|
//     _|
//   _|
// _|
//
//Probar en: https://scastie.scala-lang.org/loEP587wSdmEb0VpHfqivA