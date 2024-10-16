use std::fmt::Display;

fn main() {
    // addition
    let sum = 5 +10;

    // subtraction
    let difference = 95.5 - 4.3;

    // multiplication
    let product = 4 * 30;

    // division
    let quotient  = 56.7 / 32.2;
    let truncated = -5 / 3; // results in -1

    // remainder
    let remainder = 43 % 5;

    // tuples
    let tup: (i32, f64, u8) = (500, 6.4, 1);

    // print it all
    println!("Tup: {:?}", tup);
    println!("{sum}");
    println!("{difference}");
    println!("{product}");
    println!("{quotient}");
    println!("{truncated}");
    println!("{remainder}");

}
