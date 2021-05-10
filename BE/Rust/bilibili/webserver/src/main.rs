use mylib::ThreadPool;
use std::fs;
use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};
use std::{thread, time};
use std::io;
use std::path::Path;

fn handle_client(mut stream: TcpStream) {
    let mut buffer = [0; 512];
    stream.read(&mut buffer).unwrap();

    let get = b"GET / HTTP/1.1\r\n";

    let (status_line, filename) = if buffer.starts_with(get) {
        ("HTTP/1.1 200 OK\r\n\r\n", "main.html")
    } else {
        ("HTTP/1.1 404 NOT FOUND\r\n\r\n", "404.html")
    };

    let contents = fs::read_to_string(filename).unwrap();
    let response = format!("{}{}", status_line, contents);

    stream.write(response.as_bytes()).unwrap();
    stream.flush().unwrap();

    let te = time::Duration::from_millis(4000);
    thread::sleep(te); //睡眠一段时间，模拟处理时间很长
}

fn main() -> std::io::Result<()> {
    let listener = TcpListener::bind("127.0.0.1:8080")?;

//    TODO 多开线程
//    for stream in listener.incoming(){
//        thread::spawn(||{
//            handle_client(stream.unwrap());
//        });
//    }

//    TODO handle
//    let mut thread_vec: Vec<thread::JoinHandle<()>> = Vec::new();
//    for stream in listener.incoming() {
//        let handle = thread::spawn(|| {
//            handle_client(stream.unwrap());
//        });
//        thread_vec.push(handle);
//    }
//
//    for handle in thread_vec {
//        handle.join();
//    }

//    TODO 线程池
    let pool = ThreadPool::new(4);

//    做个限制，收到4个消息后结束
    for stream in listener.incoming().take(4) {
        let stream = stream.unwrap();
        //thread pool
        pool.execute(|| {
            handle_client(stream)
        });
    }

    Ok(())
}

