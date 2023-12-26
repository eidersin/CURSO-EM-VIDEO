<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercícios 06</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <?php 
    $v1 = $_GET['v1'] ?? 0;
    $v2 = $_GET['v2'] ?? 0;
    ?>
    <main>
        <h1>Somador de valores</h1>
        <form action="<?=$_SERVER['PHP_SELF'] ?>" method="get">
        <label for="v1">Valor 01</label>
        <input type="number" name="v1" id="v1"  value="<?=$v1?>" min=0>
        <label for="v2">Valor 02</label>
        <input type="number" name="v2" id="v2"  value="<?=$v2?>" min=0>
        <input type="submit" value="Carcular">
        </form>
    </main>
    
    <section id=resultado>
    <h2>Resultado da soma</h2>
    <?php
    $resultado = $v1 + $v2; 
    echo "A soma entre os valor $v1 e $v2 é igual a <strong>$resultado</strong>";
    ?>
    </section>
</body>
</html>