REPORT z_jcdm60.

* Hola, mundo!
WRITE 'Hola, mundo!'.

* Variables de diferentes tipos
DATA: my_string TYPE string VALUE 'Hola',
      my_integer TYPE i VALUE 10,
      my_float TYPE f VALUE 3.14,
      my_boolean TYPE abap_bool VALUE abap_true.

* Constante
CONSTANTS: my_constante_pi TYPE f VALUE '3.14159'.

* Condiciones
DATA: my_number TYPE i VALUE 6.
IF my_number < 5.
  WRITE 'El número es menor que 5'.
ELSEIF my_number = 5.
  WRITE 'El número es igual a 5'.
ELSE.
  WRITE 'El número es mayor que 5'.
ENDIF.

* Estructuras de datos
TYPES: BEGIN OF ty_structure,
         field1 TYPE i,
         field2 TYPE c LENGTH 10,
       END OF ty_structure.

DATA: my_array TYPE TABLE OF i WITH DEFAULT KEY INITIAL SIZE 5,
      my_lista TYPE TABLE OF string WITH DEFAULT KEY INITIAL SIZE 5,
      my_tupla TYPE ty_structure,
      my_conjunto TYPE TABLE OF i WITH DEFAULT KEY INITIAL SIZE 5,
      my_diccionario TYPE TABLE OF ty_structure WITH DEFAULT KEY INITIAL SIZE 5.

* Bucles
LOOP AT my_array INTO DATA(my_array_element).
  WRITE: / 'Array Element:', my_array_element.
ENDLOOP.

LOOP AT my_lista INTO DATA(my_lista_element).
  WRITE: / 'Lista Element:', my_lista_element.
ENDLOOP.

WHILE my_number < 5.
  WRITE: / my_number.
  ADD 1 TO my_number.
ENDWHILE.

* Funciones
FORM add USING a TYPE i b TYPE i RETURNING VALUE(my_result) TYPE i.
  my_result = a + b.
ENDFORM.

FORM hello USING my_nanem TYPE string.
  WRITE: 'Hola,', my_name.
ENDFORM.

FORM is_even USING my_number TYPE i RETURNING VALUE(my_result) TYPE abap_bool.
  IF my_number MOD 2 = 0.
    result = abap_true.
  ELSE.
    result = abap_false.
  ENDIF.
ENDFORM.

FORM sin_retorno.
  WRITE: 'Esta función no tiene retorno'.
ENDFORM.

* Clase
CLASS zcl_person DEFINITION.
  PUBLIC SECTION.
    METHODS: constructor IMPORTING name TYPE string age TYPE i,
             hello.
  PRIVATE SECTION.
    DATA: name TYPE string,
          age TYPE i.
ENDCLASS.

CLASS zcl_person IMPLEMENTATION.
  METHOD constructor.
    me->name = name.
    me->age = age.
  ENDMETHOD.

  METHOD hello.
    WRITE: 'Hola, soy', me->name.
  ENDMETHOD.
ENDCLASS.

* Control de excepciones
DATA: divisor TYPE i VALUE 0,
      my_result TYPE f.
TRY.
    my_result = 10 / divisor.
CATCH cx_sy_arithmetic_overflow INTO DATA(exc).
    WRITE: / 'Error: Overflow aritmético'.
CATCH cx_sy_zero_divide INTO DATA(exc).
    WRITE: / 'Error: División por cero'.
ENDTRY.