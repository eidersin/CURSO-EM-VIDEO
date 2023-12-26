<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 06</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<header><h1>Desafio 06</h1></header>
    <?php 
    $d1 = $_GET['d1'] ?? 0;
    $d2 = $_GET['d2'] ?? 1;
    ?>
    
    <main>
        <h1>Anatomia de uma Divisão</h1>
        <form action="<?=$_SERVER['PHP_SELF'] ?>" method="get">
        <label for="d1">Dividendo</label>
        <input type="number" name="d1" id="d1" value="<?=$d1?>" min=0>
        <label for="d2">Divisor</label>
        <input type="number" name="d2" id="d2" value="<?=$d2?>" min=1>
        <input type="submit" value="Calcular">   
    </form>
    </main>
    <section>
        <h2>Estrutura da Divisão</h2>
        <?php 
        // Cálculos
        $resultado = $d1 / $d2;
        $quociente = intdiv ($d1, $d2);
        $resto = $d1 % $d2;

        // echo "<ul>";
        // echo "<li>Dividendo: $d1 </li>";
        // echo "<li>Divisor: $d2 </li>";
        // echo "<li>Quociente: $quociente</li>";
        // echo "<li>Resto: $resto </li>";
        // echo "<br><li>Resultado real: $resultado </li>";
        // echo "</ul>";
        ?>
        <table class="divisao">
            <tr>
                <td><?=$d1?></td>
                <td><?=$d2?></td>
            </tr>
            <tr>
                <td><?=$resto?></td>
                <td><?=$quociente?></td>
            </tr>
        </table>
        <h3><br>Resultado Real</h3>
        <?=$resultado?>
    </section>
    
</body>
</html>