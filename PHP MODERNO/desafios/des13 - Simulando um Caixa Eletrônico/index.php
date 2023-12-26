<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 13</title>
    <link rel="stylesheet" href="style.css">
    <style>
        img.nota {
            height: 50px;
            margin: 5px;
        }
    </style>
</head>
<body>
    <header><h1>Desafio 13</h1></header>
    <?php 
    $valor = $_GET['valor'] ?? 0;
    $sobra = $valor;
    ?>
    <main>
        <h1>Caixa Eletrônico</h1>
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
        <label for="valor">Qual valor você deseja sacar? (R$)</label>
        <input type="number" name="valor" id="valor" value=<?=$valor?> required min=0 step=1>
        <p>Notas disponíveis: R$100, R$50, R$20, R$10, R$5, R$2 e R$1</p>
        <input type="submit" value="Sacar">
        </form>
    </main>
    <?php 
        
        // Total de notas de 100
        $val100 = floor($sobra / 100);
        $sobra %= 100;
        // Total de notas de 50
        $val50 = floor($sobra / 50);
        $sobra %= 50;
        // Total de notas de 20
        $val20 = floor($sobra / 20);
        $sobra %= 20;
        // Total de notas de 10
        $val10 = floor($sobra / 10);
        $sobra %= 10;
        // Total de notas de 5
        $val5 = floor($sobra / 5);
        $sobra %= 5;
        // // Total de notas de 2
        $val2 = floor($sobra / 2);
        $sobra %= 2;
        // // Total de moedas de 1
        $val1 = floor($sobra / 1);
        $sobra %= 1;
        // Restante
        $restante = $sobra / 0.1;
        ?>
    <section>
    <h2>Saque de <?=number_format($valor, 2, ",", ".")?> realizado</h2>
        <p>O caixa eletrônico vai te entregar as seguintes notas:<p>
        <ul>
            <li><img src="notas/100-reais.jpg" alt="Nota de 100" class="nota">x<?=$val100?> </li>
            <li><img src="notas/50-reais.jpg" alt="Nota de 50" class="nota">x<?=$val50?> </li>
            <li><img src="notas/20-reais.jpg" alt="Nota de 20" class="nota">x<?=$val20?> </li>
            <li><img src="notas/10-reais.jpg" alt="Nota de 10" class="nota">x<?=$val10?> </li>
            <li><img src="notas/5-reais.jpg" alt="Nota de 5" class="nota">x<?=$val5?> </li>
            <li><img src="notas/2-reais.jpg" alt="Nota de 2" class="nota">x<?=$val2?> </li>
            <li><img src="notas/1-real.jpg" alt="Nota de 1" class="nota">x<?=$val1?> </li>
        </ul>
    </section>
</body>
</html>