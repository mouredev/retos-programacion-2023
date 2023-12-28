// OCaml


print_endline "Hello World!"
can be compiled into a bytecode executable:

$ ocamlc hello.ml -o hello
or compiled into an optimized native-code executable:

$ ocamlopt hello.ml -o hello
and executed:

$ ./hello
Hello World!
$