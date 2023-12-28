pub fn decrementar(comienza: u8, segundos: u64) {
  for i in (0..=comienza).rev() {
    println!("{:?}", i);
    if i != 0 {
      thread::sleep(time::Duration::from_secs(segundos));
    }
  }
}
