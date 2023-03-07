<?php

/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

class CheckHIP // Heterograma Isograma Pangrama
{
    private $text;
    private $isIso=false;
    private $isHet=false;
    private $isPan=false;
    private $counter=[];

    public function setText($text): self
    {
        $this->init();
        $this->text = $text;

        return $this;
    }

    public function getText(): string
    {
        return $this->text;
    }

    public function init(): void
    {
        //print("Inicializando...");
        $this->counter = [];
        for ($i=ord('a'); $i<=ord('z'); $i++) {
            $this->counter[chr($i)] = 0; //Contador
        }
        $this->counter[chr(195)] = 0;
        $this->text = null;
        $this->isIso = $this->isHet = $this->isPan = null;
    }

    public function analyze($text = null)
    {
        if (null != $text) {
            $this->setText($text);
        }

        // Cambiamos los acentos a sus correspondientes
        $search = ['á', 'Á', 'é', 'É', 'í', 'Í', 'ó', 'Ó', 'ú', 'Ú', 'ü', 'Ü', 'Ñ'];
        $replace = ['a', 'a', 'e', 'e', 'i', 'i', 'o', 'o','u','u','u','u', 'ñ'];
        $stripped = str_replace($search, $replace, strtolower($this->text));
        for ($i=0; $i<strlen($stripped); $i++) {
            if (isset($this->counter[$stripped[$i]])) {
                $this->counter[$stripped[$i]]++;
            }
        }
    }

    public function dumpCounter($all = true)
    {
        if ($all) {
            var_dump($this->counter);
        } else {
            foreach ($this->counter as $key => $item) {
                if ($item>0) {
                    printf("Item: %s, valor: %d\n", $key, $item);
                }
            }
        }
    }

    public function isHeterogram(): bool
    {
    /* Un heterograma (del griego héteros, 'diferente' y gramma, 'letra')
    es una palabra o frase que no contiene ninguna letra repetida. */
        if (null==$this->isHet) {
            $test = true;
            foreach ($this->counter as $letter => $times) {
                if ($times>1) {
                    $test = $this->isHet =false;
                    break;
                }
            }
            $this->isHet = $test;
        }

        return $this->isHet;
    }

    public function isIsogram(): bool
    {
        /*
        Un isograma (del griego isos, 'igual' y gramma, 'letra') es una palabra o frase
        en la que cada letra aparece el mismo número de veces.
        Si cada letra aparece solo una vez será un heterograma,
        si aparece dos, un isogroma de segundo orden y así sucesivamente.
        */
        if (null==$this->isIso) {
            $test = 0;
            $this->isIso = true;
            foreach ($this->counter as $item) {
                if ($item>0) {
                    if ($test===0) {
                        $test = $item;
                    } else {
                        if ($test != $item) {
                            $this->isIso = false;
                            break;
                        }
                    }
                }
            }
        }

        return $this->isIso;
    }

    public function isPangram(): bool
    {
        /*
        Un pangrama (del griego pan, 'todo' y gramma, 'letra') es una frase
        en la que aparecen todas las letras del abecedario.
        Si cada letra aparece sólo una vez, formando por tanto un heterograma,
        se le llama pangrama perfecto.
        */
        if (null==$this->isPan) {
            $test = true;
            foreach ($this->counter as $item) {
                if ($item<1) {
                    $test =false;
                    break;
                }
            }
            $this->isPan = $test;
        }

        return $this->isPan;
    }
}

$test = new CheckHIP();
$texts = [
    'hola la caña de España',
    'aaabbbccc',
    'caca',
    'hala',
    'centrifugado',
    'acondicionar',
    'Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.'
];
foreach ($texts as $text) {
    $test->setText($text);
    $test->analyze();
    //$test->dumpCounter(false);
    printf("Evaluando %s:\n", $text);
    print($test->isIsogram()?"Es isograma":"No es isograma") . "\n";
    print($test->isHeterogram()?"Es heterograma":"No es heterograma") . "\n";
    print($test->isPangram()?"Es pangrama":"No es pangrama") . "\n";
}
