<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 02</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<header>
        <h1>Desafio 02</h1>
    </header>
<main>
    <?php
        $min = $_GET["min"];
        $max = $_GET["max"];
        
        $num = mt_rand($min, $max);
        echo "O número gerado foi: <strong>$num</strong>";
    ?>
        <button onclick="javascript:document.location.reload()">Gerar outro número</button>
        <button onclick="javascript:history.go(-1)">Voltar</button>
</main>
</body>
</html>