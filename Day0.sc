import scala.io.Source


def getDayInput(number: Int) = {
  val source = scala.io.Source.fromFile(s"inputs/Day_${number}.txt")
  try source.mkString.trim finally source.close()
}

def getDayInputByLine(number: Int) = {
  val source = scala.io.Source.fromFile(s"inputs/Day_${number}.txt").getLines
}

