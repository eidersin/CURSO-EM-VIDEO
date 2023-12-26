<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 10</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<header><h1>Desafio 10</h1></header>
    <main>
        <?php 
        $nasc = $_GET['nasc'] ?? 2000;
        $ano = $_GET['ano'] ?? date('Y');
        ?>

        <h1>Calculando a sua idade</h1>
        <form action="<?=$_SERVER['PHP_SELF']?>">
        <label for="nasc">Em que ano você nasceu?</label>
        <input type="number" name="nasc" id="nasc" required min=1900 value=<?=$nasc?> max=<?=date('Y')?>>    
        <label for="ano">Quer saber sua idade em que ano? (Atualmente estamos em <strong><?=date('Y')?></strong>)</label>
        <input type="number" name="ano" id="ano" required value=<?=date('Y')?>>
        <input type="submit" value="Qual será minha idade?">            
    </form>
    </main>
    <section>
        <h1>Resultado</h1>
        <?php
        $idade = $ano - $nasc;
        echo "Quem nasceu em $nasc vai ter <strong> $idade anos </strong> em " . date('Y') . "!";
        ?>
    </section>
</body>
</html>