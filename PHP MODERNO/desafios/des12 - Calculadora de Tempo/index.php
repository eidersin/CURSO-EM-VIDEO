<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 12</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header><h1>Desafio 12</h1></header>
    <?php 
    $segundos = $_GET['segundos'] ?? 0;
    $sobra = $segundos;
    ?>
    <main>
        <h1>Calculadora de Tempo</h1>
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
        <label for="segundos">Qual é o total de segundos?</label>
        <input type="number" name="segundos" id="segundos" min="0" value=<?=$segundos?>>
        <input type="submit" value="Calcular">
        </form>
    </main>
    <?php
    // Total de Semanas
        $semana = (int) ($sobra / 604_800);
        $sobra = $sobra % 604_800;
    // Total de Dias 
        $dias = (int) ($sobra / 86_400);
        $sobra = $sobra % 86_400;
    // Total de Horas
        $horas = (int) ($sobra / 3_600);
        $sobra = $sobra % 3_600;
    // Total de Minutos
        $minutos = (int) ($sobra / 60);
        $sobra = $sobra % 60;
    //Total de Segundos
        $seg = $sobra;
    ?>
    <section>
        <h2>Totalizando tudo</h2>
        <p>Analisando o valor que você digitou, <strong><?=number_format($segundos, 0, ",", ".")?>
        segundos</strong> equivalem a um total de: <p>
        <ul>
            <li><?=$semana?> Semanas</li>
            <li><?=$dias?> Dias</li>
            <li><?=$horas?> Horas</li>
            <li><?=$minutos?> Minutos</li>
            <li><?=$seg?> Segundos</li>
        </ul>
    </section>
</body>
</html>