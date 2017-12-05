import $file.Day0

val wordArray = Day0.getDayInput(4).split('\n').map(_.split(' '))

def allDistinct(words: Array[String]) =
  words.distinct.size == words.size

def allDistinctAndUnique(words: Array[String]) = {
  allDistinct(words) && 
    (for { x <- words; y <- words; if x != y } yield !x.permutations.contains(y)).forall(identity)
}

val partOne = wordArray.filter(allDistinct).length
println(s"Part 1: $partOne") // 451

val partTwo = wordArray.filter(allDistinctAndUnique).length
println(s"Part 1: $partTwo") // 451
