use std::fs;
use std::io;
use std::path::Path;

fn visit_dirs(dir: &Path) -> io::Result<()> {
    if dir.is_dir() {
        for entry in fs::read_dir(dir)? {
            let entry = entry?;
            let path = entry.path();
            if path.is_dir() {
                visit_dirs(&path);
            } else {
                let c = fs::read_to_string(path).unwrap();
                println!("file = {}", c);
            }
        }
    }
    return Ok(());
}

fn main() {
// ^^^^^^^ `std::vec::Vec<u8>` cannot be formatted with the default formatter
    let context = fs::read("./test/hello").unwrap();
    println!("{:#?}", context);

    let context = fs::read_to_string("./test/hello").unwrap();
    println!("{:#?}", context);

    visit_dirs(Path::new("./test")).unwrap();

//    [
//    104,
//    101,
//    108,
//    108,
//    111,
//    32,
//    114,
//    117,
//    115,
//    116,
//    33,
//    10,
//]
//    "hello rust!\n"
//    file = hello rust!

}
