import $file.Day0

val captcha = Day0.getDayInput(1).map(_.asDigit)

def zipWithOffset(offset: Int) = {
  captcha.zip(captcha.drop(offset) ++ captcha.take(offset))
    .filter { case (x, y) => x == y }.map(_._1).sum
}

val partOne = zipWithOffset(1)
println(s"Part 1: $partOne") // 1150

val partTwo = zipWithOffset(captcha.length / 2)
println(s"Part 2: $partTwo") // 1064
