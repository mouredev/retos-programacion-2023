Hello World in Limbo.
Limbo is the programming language of the Inferno OS
(from Lucent Bell Labs).


implement Cmd;

include "sys.m";
include "draw.m";

Cmd : module {
    init : fn (ctxt : ref Draw->Context, args : list of string);
};

init(nil : ref Draw->Context, nil : list of string)
{
    sys := load Sys Sys->PATH;
    sys->print("Hello World\n");
}