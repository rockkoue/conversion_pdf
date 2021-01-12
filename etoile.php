<?php
$var = 6;
$var2 = $var;
$total2 = $var * 3;
$total = $var * 3;
$space1 = ' ';
$default1 = "*";
$space2 = '';
$default2 = '***';


for ($i = 0; $i < $var; $i++) {


    for ($j = 0; $j < $total; $j++) {
        echo $space1;
    }

    $start = $i > 0 ? '*' : '';

    echo $default1 . $space2 . $start . "\n";

    $start = $i > 0 ? ' ' : '';

    $default2 .= $i > 0 ? '**' : '';

    $space2 .= $start . $space1;
    $total = $total - 1;
}


echo $default2 . $space2 . $default2 . "\n";
$var_space = $default2 . $space2 . $default2;

$char = str_replace('*', ' ', substr($default2 . $space2 . $default2, 0, -4));
$char2 =  str_replace('*', ' ', $default2 . $space2 . $default2);
$other = "";
$other2 = "";
for ($s = 0; $s < $var2; $s++) {

    $default1 = ' ' . $default1;
    echo $default1 . $char . "*\n";
    $char = substr($char, 0, -2);
    $other .= ' ';
}

$default1 = '*';
$space = '';
$char .= $other . '   ';
for ($s = 1; $s < $var2; $s++) {

    $other = substr($other, 1);
    echo $other . $default1 . substr($char, 0, -strlen($other)) . $space . $default1 . "\n";
    // echo $other.$default1.$other2.$space.$default1."\n";
    $space = ' ' . $space;
}

echo $var_space;
