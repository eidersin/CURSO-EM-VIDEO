<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado</title>
    <link rel="stylesheet" href="style-cad.css">
</head>
<body>
    <header>
        <h1>Cadastro realizado com sucesso!</h1>
    </header>
    <main>
        <?php 
            $nome = $_GET["nome"] ?? "ERRO NOME";
            $sobrenome = $_GET["sobrenome"] ?? "ERRO SOBRENOME";
            echo "<p>Cadastro realizado com sucesso! <strong> $nome $sobrenome</strong>.";
        ?>
        <p><a href="javascript:history.go(-1)">Voltar para a página anterior.</a></p>
    </main>
</body>
</html>