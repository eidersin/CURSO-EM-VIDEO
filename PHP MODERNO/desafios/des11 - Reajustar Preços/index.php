<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 11</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <header><h1>Desafio 11</h1></header>
        <?php   
        $valor = $_GET['valor'] ?? 0;
        $percent = $_GET['percent'] ?? 0;
        ?>
    <main>
        <h1>Reajustador de Preços</h1>
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
        <label for="valor">Preço do Produto (R$):</label>
        <input type="number" name="valor" id="valor" min="0.10" value=<?=$valor?> step="0.01">
        <!-- Como colocar o range -->
            <label for="percent">Qual será o percentual de reajuste?(<strong><span id="p">?</span>%</strong>)</label>
            <input type="range" name="percent" id="percent" min="0" max="100" step="1" value=<?=$percent?> oninput="mudaValor()">

        <input type="submit" value="Reajustar">
    </form>
    </main>
    <?php 
        $vpercent = ($valor * $percent / 100);
        $resultado = $valor + $vpercent;
        ?>
    <section>
        <h1>Resultado do Reajuste</h1>
        </p>O produto que custava <strong>R$<?=number_format($valor, 2, ",", ".")?> Reais</strong>, com <strong><?=$percent?>% de aumento</strong> (R$<?=number_format($vpercent, 2, ",", ".")?>).</p> 
        <p>Vai passar a custar <strong>R$<?=number_format($resultado, 2, ",", ".")?></strong> a partir de agora.</p>
    </section>
    <script>
        // Declarações automáticas
        mudaValor()
        function mudaValor(){
            p.innerText = percent.value;

        }
    </script>
</body>
</html>