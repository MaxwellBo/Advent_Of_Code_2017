import $file.Day0

val grid = Day0.getDayInput(2).split('\n').map(_.split('\t').map(_.toInt))

val partOne = grid.map(x => x.max - x.min).sum
println(s"Day 2-1: $partOne") // 21845

def evenlyDivides(row: Array[Int]): Int = 
  (for { x <- row; y <- row; if x % y == 0 && x != y } yield x / y).head

val partTwo = grid.map(evenlyDivides).sum
println(s"Day 2-2: $partTwo") // 191
