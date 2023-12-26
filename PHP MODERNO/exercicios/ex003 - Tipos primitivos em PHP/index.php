<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tipos primitivos em PHP</title>
</head>
<body>
    <h1>CURSO</h1>
    <?php 
    // 0x = hexadecimal, 0b = binário, 0 = octal
        // $inteiro1 = 300;
        // $inteiro2 = 0x1A;
        // $octal = 010;
        // echo "O valor da variável é $inteiro1 ";
        // echo "O valor da variável hexadecimal 0x1A é $inteiro2";
        // echo "o Valor octal é $octal";

        #COERÇÃO
        // Exemplo1
        // $coercao = (int) 3e2;
        // echo "Exemplo1 de coerção de FLOUT para INT ----";
        // var_dump($coercao);

        //Exemplo2
        // $coercao2 = (int) "950";
        // echo "Exemplo2 de coerção de STRING para INT ---- ";
        // var_dump($coercao2);

        // Exemplo3
        // $coercao3 = (real) "950";
        // echo "a variavel real não existe mais no php após 7.4" . $real

        //EXEMPLO ARRAY
        // $vet = [6, 5.5, false, "Maria"];
        // var_dump($vet);

        //EXEMPLO OBJECT
        // class Pessoa {
        //     private string $nome;
        // }
        // $p = new Pessoa;
        // var_dump($p);

        //double quoted
        // echo "PHP \u{1F418}";
        // echo 'PHP \u{1F418}';
        
        // $nome = "Wanderson";
        // $snome = "Teixeira";
        // echo "$nome " . '"Nenem" ' . "$snome ";
        // echo "$nome \"Nenem\" $snome";

    ?>
</body>
</html>