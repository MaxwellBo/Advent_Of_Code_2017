import $file.Day0

val captcha = Day0.getDayInput(1).map(_.asDigit)

val partOne = (captcha :+ captcha.head).iterator.sliding(2, 1)
  .filter(xs => xs(0) == xs(1)).map(_(0)).sum

println(s"Part 1: $partOne") // 1150

val partTwo = captcha.zip(captcha.drop(captcha.length / 2) ++ captcha.take(captcha.length / 2))
  .filter { case (x, y) => x == y }.map(_._1).sum

println(s"Part 2: $partTwo") // 1064

