<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 08</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<header><h1>Desafio 08</h1></header>
    <main>
        <?php  
            $num = $_GET['num'] ?? 0;
        ?>
        <h1>Informe um número</h1>
        <form action="<?=$_SERVER['PHP_SELF'] ?>" method="get">
        <label for="num">Número</label>
        <input type="number" name="num" id="num" value=<?=$num?> step="0.01">
        <input type="submit" value="Calcular Raízes">
    </form>
    </main>
    <section>
        <h2>Resultado Final</h2>
        <?php 
        $rquadrada = $num ** (1/2);
        $rcubica = $num ** (1/3);

            echo "Analisando o <strong>número $num</strong>, temos:";
            echo "<ul>";
            echo "<li> A sua raiz quadrada é <strong>". number_format($rquadrada, 3, ",", ".") . "</strong> </li>";
            echo "<li> A sua raiz cúbica é <strong>" . number_format($rcubica, 3, ",", ".") . "</strong></li>";
            echo "</ul>";
        ?>
    </section>
</body>
</html>