import $file.Day0
import scala.util.control.Breaks._
import scala.collection.mutable.WrappedArray

val blocks = new WrappedArray.ofInt(Day0.getDayInput(6).split('\t').map(_.toInt))

type Arr = scala.collection.mutable.WrappedArray.ofInt
var history = Set[Arr]()

do {
  history += blocks.clone

  var maxIndex = blocks.zipWithIndex.maxBy(_._1)._2

  var pointer = maxIndex

  do {
    pointer = if (pointer == blocks.length - 1) 0 else pointer + 1
    println(blocks.mkString(", "))
    blocks(pointer) += 1
    blocks(maxIndex) -= 1
  } while (blocks(maxIndex) > 0)

} while(!history.contains(blocks.clone))

println(s"Part 1: ${history.size}")
