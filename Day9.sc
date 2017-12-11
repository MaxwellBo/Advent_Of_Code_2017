import $file.Day0
import $ivy.`com.lihaoyi::fastparse:1.0.0`
import fastparse.all._


val garbage: P[Int] = P( "<" ~ AnyChar.rep ~ ">").!.map( _ => 0)

val things: P[Int] = P( group | garbage ).!

val group: P[Int] = P( "{" ~ group.rep(sep=",") ~ "}")

val expr: P[Int] = P( group ~ End )

print(expr.parse(Day0.getDayInput(9)))
