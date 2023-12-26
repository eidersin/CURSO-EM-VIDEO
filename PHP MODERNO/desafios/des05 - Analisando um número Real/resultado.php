<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 05</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<header><h1>Desafio 05</h1></header>
    <main>
        <h2>Analisador de Número Real</h2>
        <?php 
            $num = $_GET["n"] ?? 0;
            $int = (int) $num;
            $fra = $num - $int;
         
            echo "Analisando o número <strong>". number_format($num, 3, ",", ".") . "</strong> informado pelo usuário:</li>";
            echo "<ul><li>A parte inteira do número é <strong>" . number_format($num, 0, ",", ".") . "</strong></li>";
            echo "<li>O número fracionado é <strong>" . number_format($fra, 3, ",",".") . "</strong></li></ul>";
        ?>
            
            <button onclick="javascript:history.go(-1)">Calcular outro valor</button>
    </main>
</body>
</html>