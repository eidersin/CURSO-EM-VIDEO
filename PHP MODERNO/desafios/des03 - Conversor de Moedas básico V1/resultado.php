<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 03</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Desafio 03</h1>
    </header>
    <main>
    <?php 
    $cotacao = $_GET["vdolar"] ?? 0;
    $real =  $_GET["vreal"] ?? 0;
    $dolar = $real / $cotacao;
    //Mostrar resultado simples
    echo "<p><strong>Formatação simples</strong><br>";
    echo "Seus R\$ " . number_format($real, 2, ",", ".") . " equivalem a <strong>US\$ " . number_format($dolar, 2, ",", ".") . "</strong></p>";

    // Formatação de moedas com internacionalização!
    echo "<p><strong>Formatação INTL (Internallization PHP)</strong><br>";
    $padrao = numfmt_create("pt_BR", NumberFormatter::CURRENCY);
    echo "Seus " . numfmt_format_currency($padrao, $real, "BRL") . " equivalem a <strong>" . numfmt_format_currency($padrao, $dolar, "USD") . "</strong></p>";


    ?>
        <button onclick="javascript:history.go(-1)">Calcular outro valor</button>

    </main>
</body>
</html>