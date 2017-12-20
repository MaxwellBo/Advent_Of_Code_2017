import $file.Day0
import $ivy.`com.lihaoyi::fastparse:1.0.0`
import fastparse.all._

sealed trait Thing
case class Group(contents: Seq[Thing]) extends Thing
case class Garbage(contents: String) extends Thing
case class Malformed() extends Thing

val things: P[Thing] = P( group | garbage | malformed )
val garbage: P[Thing] = P( "<" ~ P( negate | chomp ).rep ~ ">").map(x => Garbage(x.mkString("")))
val negate: P[String] = P( "!" ~ AnyChar ).map(_ => "")
val chomp: P[String] = P( CharsWhile(x => x != '>' && x != '!').! )
val group: P[Thing] = P( "{" ~ things.rep(sep=",") ~ "}").map(Group(_))
val malformed: P[Thing] = P( Pass ).map(_ => Malformed())

def score(level: Int)(thing: Thing): Int = thing match {
  case Malformed() => 0
  case Garbage(_) => 0
  case Group(contents) => level + contents.map(score(level + 1)).sum
}

def count(thing: Thing): Int = thing match {
  case Malformed() => 0
  case Garbage(contents) => contents.length
  case Group(contents) => contents.map(count).sum
}

val Parsed.Success(thing, _) = group.parse(Day0.getDayInput(9))
println(s"Part 1: ${score(1)(thing)}")
println(s"Part 2: ${count(thing)}")
