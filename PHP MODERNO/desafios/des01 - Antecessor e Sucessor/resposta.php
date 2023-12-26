<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio PHP 01</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Desafio PHP 01</h1> 
    </header>
    <main>
    <p>        
                <?php
                $numero = $_GET["num"];
                $ant = $numero - 1;
                $suc = $numero + 1;
                
                echo "O Número é: <strong> $numero</strong><br>";
                echo "O Antecessor de $numero é <strong>$ant</strong><br>";
                echo "O Sucessor de $numero é <strong>$suc</strong><br>";
                ?>
    </p>
                <button onclick="javascript:history.go(-1)">Voltar</button>
    </main>
    
</body>
</html>