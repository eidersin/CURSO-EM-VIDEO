<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 04</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Desafio 04</h1>
    </header>
    <main>
    <?php

            // Valor REAL colocada no site
        $real = $_GET["vreal"] ?? 0;

            // Equivalente DOLAR colcoado no site
        $dolar = $_GET["vdolar"] ?? 0;

            // Cotação vinda do API do Banco Central
        $inicio = date("m-d-Y", strtotime("-4 days")) ;
        $fim = date("m-d-Y");
        $url = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial=\''. $inicio.'\'&@dataFinalCotacao=\''. $fim.'\'&$top=1&$orderby=cotacaoCompra%20desc&$format=json&$select=cotacaoCompra,dataHoraCotacao';
      
        $dados = json_decode(file_get_contents($url), true);
        $cotacaoapi = $dados["value"][0]["cotacaoCompra"];

        // Calculo cotação
        $cotacaosimples = $real / $dolar;
        $cotacaosite = $real / $cotacaoapi;

        // Mostrar resultado formatação INTL
        $padrao = numfmt_create("pt-BR", NumberFormatter::CURRENCY);
        
        
        echo "<strong>Valor Atual do Branco Central do Brasil. $cotacaoapi </strong>";
        echo "<p>Seus " . numfmt_format_currency($padrao, $real, "BRL") . " equivalem <strong>" . numfmt_format_currency($padrao, $cotacaosite, "USD") . "</strong> de acordo com a cotação do Branco Central do Brasil.</p>";
        echo "<strong>Valor solicitado para cotação ". number_format($dolar, 2, ",",".") ."</strong>";
        echo "<p>Seus " . numfmt_format_currency($padrao, $real, "BRL") . " equivalem a <strong>" . numfmt_format_currency($padrao, $cotacaosimples, "USD") . "</strong> de acordo com a cotação solicitada.</p>";
    ?>
        <button onclick="javascript:history.go(-1)">Calcular outro valor</button>

    </main>
</body>
</html>